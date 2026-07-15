"""
Utilitário para carregar queries SQL de arquivos

Fornece funções para ler e gerenciar queries SQL armazenadas em arquivos .sql
"""
from pathlib import Path
from typing import Dict, Optional


def load_sql_query(sql_file: str, sql_dir: str = 'sql') -> str:
    """
    Carrega uma query SQL de um arquivo

    Procura o arquivo em múltiplos locais:
    - Diretório 'sql' na raiz do projeto
    - Caminho relativo fornecido
    - Caminho absoluto

    Args:
        sql_file: Nome do arquivo SQL (ex: "id_assistidos_duplicados.sql")
        sql_dir: Diretório padrão onde estão os arquivos SQL

    Returns:
        str: Conteúdo do arquivo SQL

    Raises:
        FileNotFoundError: Se o arquivo não for encontrado

    Exemplo:
        query = load_sql_query("assistidos_duplicados.sql")
        results = conn.execute_query(query)
    """

    # Tenta vários caminhos possíveis
    possible_paths = [
        # Relativo à raiz do projeto
        Path(__file__).parent.parent.parent.parent / sql_dir / sql_file,
        # Diretório atual
        Path.cwd() / sql_dir / sql_file,
        # Caminho direto (se for absoluto)
        Path(sql_file) if Path(sql_file).is_absolute() else None,
        # Home do usuário
        Path.home() / sql_dir / sql_file,
    ]

    for path in possible_paths:
        if path and path.exists():
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return f.read().strip()
            except Exception as e:
                print(f'⚠️  Erro ao ler {path}: {e}')
                continue

    # Se chegou aqui, não encontrou em lugar nenhum
    raise FileNotFoundError(
        f'Arquivo SQL não encontrado: {sql_file}\n' f'Procurou em: {[str(p) for p in possible_paths if p]}'
    )


def load_sql_queries(sql_files: Dict[str, str], sql_dir: str = 'sql') -> Dict[str, str]:
    """
    Carrega múltiplas queries SQL de uma vez

    Args:
        sql_files: Dicionário {nome_variavel: arquivo.sql}
        sql_dir: Diretório padrão onde estão os arquivos SQL

    Returns:
        dict: Dicionário com queries carregadas

    Exemplo:
        queries = load_sql_queries({
            'duplicados': 'id_assistidos_duplicados.sql',
            'atendimentos': 'atendimentos.sql'
        })
        print(queries['duplicados'])
    """
    loaded_queries = {}

    for key, sql_file in sql_files.items():
        try:
            loaded_queries[key] = load_sql_query(sql_file, sql_dir)
        except FileNotFoundError as e:
            print(f"❌ Erro ao carregar query '{key}': {e}")
            loaded_queries[key] = None

    return loaded_queries


def minify_sql(sql: str) -> str:
    """
    Remove comentários e espaços desnecessários de uma query SQL

    Args:
        sql: Query SQL

    Returns:
        str: Query minificada
    """
    lines = []
    for line in sql.split('\n'):
        # Remove comentários
        line = line.split('--')[0]
        # Remove espaços extras
        line = line.strip()
        if line:
            lines.append(line)

    return ' '.join(lines)


if __name__ == '__main__':
    # Teste
    try:
        query = load_sql_query('id_assistidos_duplicados.sql')
        print('✅ Query carregada com sucesso!')
        print(f'Tamanho: {len(query)} caracteres')
        print('\nPrimeira linha:')
        print(query.split('\n')[0])
    except Exception as e:
        print(f'❌ Erro: {e}')
