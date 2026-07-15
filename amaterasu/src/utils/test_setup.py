"""
Script para testar a estrutura e dependências do projeto
"""
import sys
from pathlib import Path

# Adiciona o diretório do projeto ao path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))


def test_imports():
    """Testa se todos os módulos podem ser importados"""
    print('Testando importações...')

    try:
        from amaterasu.src.utils.env_config import ENVIRONMENT

        print('✓ env_config importado com sucesso')
    except Exception as e:
        print(f'✗ Erro ao importar env_config: {e}')

    try:
        from amaterasu.src.etl.template_etl import MeuETL

        print('✓ template_etl importado com sucesso')
    except Exception as e:
        print(f'✗ Erro ao importar template_etl: {e}')

    try:
        from amaterasu.src.consultas.template_consulta import MinhaConsulta

        print('✓ template_consulta importado com sucesso')
    except Exception as e:
        print(f'✗ Erro ao importar template_consulta: {e}')

    try:
        from amaterasu.src.relatorios.template_relatorio import MeuRelatorio

        print('✓ template_relatorio importado com sucesso')
    except Exception as e:
        print(f'✗ Erro ao importar template_relatorio: {e}')

    print('\n✓ Testes de importação concluídos!')


if __name__ == '__main__':
    test_imports()
