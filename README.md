# ☀️ Amaterasu - Framework de ETL em Python

> *"A Grande Deusa Augusta que ilumina o céu"* - Mitologia Japonesa

## O Conceito

Assim como **Amaterasu**, a deusa do sol na mitologia japonesa, traz luz e claridade ao universo, este projeto foi criado para **iluminar seus dados**, transformando informações brutas em conhecimento estruturado e acessível.

Amaterasu traz ordem ao caos cósmico através da sua luz. Da mesma forma, este framework transforma dados desorganizados em **pipelines eficientes de ETL, consultas estruturadas e relatórios precisos**.

---

## 🌟 Sobre o Projeto

**Amaterasu** é um framework Python para **construção de pipelines de ETL (Extract, Transform, Load)** com suporte a múltiplos bancos de dados. Ele fornece templates reutilizáveis e componentes prontos para:

- 🔄 **ETL Modular** - Classes base para Extração, Transformação e Carregamento de dados
- 🔍 **Consultas Estruturadas** - Template para criar consultas otimizadas e reutilizáveis
- 📊 **Relatórios Flexíveis** - Geração de relatórios em múltiplos formatos (Excel, CSV, PDF)
- 💾 **Multi-banco** - Suporte nativo para PostgreSQL e MongoDB
- ⚙️ **Utilities** - Ferramentas para timing, configuração de ambiente e operações comuns
- 🧪 **Pronto para Testes** - Integrado com pytest e cobertura de testes

---

## 📋 Estrutura do Projeto

```
amaterasu/
├── src/
│   ├── etl/
│   │   ├── __init__.py
│   │   └── template_etl.py          # Template base para ETL (MeuETL)
│   │
│   ├── consultas/
│   │   ├── __init__.py
│   │   └── template_consulta.py     # Template base para consultas (MinhaConsulta)
│   │
│   ├── relatorios/
│   │   ├── __init__.py
│   │   └── template_relatorio.py    # Template base para relatórios (MeuRelatorio)
│   │
│   └── utils/
│       ├── env_config.py             # Gerenciador de configurações de ambiente
│       ├── database/
│       │   ├── postgres_connection.py # Gerenciador de conexão PostgreSQL
│       │   └── mongodb_connection.py  # Gerenciador de conexão MongoDB
│       └── helpers/
│           └── timing.py             # Decorator para medir tempo de execução
│
├── dados/                            # Diretório para armazenamento de dados
├── sql/                              # Scripts SQL
├── tests/                            # Testes unitários
├── pyproject.toml                    # Configuração de tasks e formatação
├── requirements.txt                  # Dependências do projeto
├── start_project.ps1                 # Script de inicialização (Windows)
└── README.md                         # Este arquivo
```

---

## 🚀 Início Rápido

### Pré-requisitos
- **Python 3.12+**
- **pip** (gerenciador de pacotes)
- **pyenv-win** (recomendado, para gerenciar versões do Python no Windows)
- **PostgreSQL e/ou MongoDB** (opcional, conforme necessário)

### Instalação

#### 1. Execute o script de inicialização

No Windows PowerShell, na raiz do projeto:

```powershell
.\start_project.ps1
```

Este script automaticamente:
- ✅ Instala Python 3.12 via pyenv (se não estiver instalado)
- ✅ Cria um ambiente virtual (`venv`)
- ✅ Instala todas as dependências do `requirements.txt`
- ✅ Ativa o ambiente virtual

#### 2. Ou configure manualmente

```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt
```

### Configuração de Ambiente

1. **Crie um arquivo `.env` na raiz do projeto:**

```env
ENVIRONMENT=dev
DEBUG=True

# PostgreSQL
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=seu_banco
POSTGRES_USER=postgres
POSTGRES_PASSWORD=sua_senha

# MongoDB
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB=seu_banco_mongo

# API (opcional)
API_BASE_URL=https://api.exemplo.com
API_KEY=sua_chave_api
```

2. **As variáveis serão carregadas automaticamente pelo `env_config.py`:**

```python
from amaterasu.src.utils.env_config import POSTGRES_HOST, POSTGRES_DB, MONGODB_URI
```

---

## 💡 Exemplos de Uso

### 1. Criar um ETL

Herde da classe `MeuETL` e implemente os três métodos principais:

```python
from amaterasu.src.etl.template_etl import MeuETL

class MeuProcessoETL(MeuETL):
    def __init__(self):
        super().__init__()
        self.nome = "Importação de Dados"
    
    def extract(self):
        """Extrai dados de uma fonte (API, arquivo, banco, etc)"""
        print("Buscando dados da fonte...")
        dados = [
            {"id": 1, "nome": "João"},
            {"id": 2, "nome": "Maria"}
        ]
        return dados
    
    def transform(self, dados: list):
        """Transforma e valida os dados"""
        print(f"Transformando {len(dados)} registros...")
        # Adiciona campos, valida, limpa dados, etc
        dados_transformados = [
            {**d, "nome": d["nome"].upper()} 
            for d in dados
        ]
        return dados_transformados
    
    def load(self, dados: list):
        """Carrega os dados no banco de dados"""
        print(f"Carregando {len(dados)} registros...")
        # Conecta ao banco e insere dados
        registros_carregados = len(dados)
        return registros_carregados

# Executar
if __name__ == "__main__":
    etl = MeuProcessoETL()
    etl.executar()
```

### 2. Criar uma Consulta

```python
from amaterasu.src.consultas.template_consulta import MinhaConsulta
from amaterasu.src.utils.database.postgres_connection import PostgresConnection
from amaterasu.src.utils.env_config import get_database_url

class ConsultaPedidos(MinhaConsulta):
    def __init__(self):
        super().__init__()
        self.nome = "Consulta de Pedidos"
    
    def executar_consulta(self, parametros: dict = None):
        """Executa a consulta no banco de dados"""
        query = "SELECT * FROM pedidos WHERE status = :status"
        
        db_url = get_database_url("postgres")
        with PostgresConnection(db_url) as conn:
            resultados = conn.execute_query(query, parametros or {})
        
        return resultados

# Usar
if __name__ == "__main__":
    consulta = ConsultaPedidos()
    resultados = consulta.executar({"status": "pendente"})
    print(f"Encontrados {len(resultados)} pedidos pendentes")
```

### 3. Criar um Relatório

```python
from amaterasu.src.relatorios.template_relatorio import MeuRelatorio
import pandas as pd

class RelatorioVendas(MeuRelatorio):
    def __init__(self):
        super().__init__("Vendas Mensais", formato="excel")
    
    def coletar_dados(self):
        """Coleta dados para o relatório"""
        # Pode buscar de um banco de dados, arquivo, etc
        dados = {
            "linhas": [
                {"mês": "janeiro", "vendas": 10000},
                {"mês": "fevereiro", "vendas": 15000}
            ],
            "metadados": {"período": "2024"}
        }
        return dados
    
    def processar_dados(self, dados: dict):
        """Processa e agrega dados"""
        df = pd.DataFrame(dados["linhas"])
        df["total_acumulado"] = df["vendas"].cumsum()
        return df

# Gerar
if __name__ == "__main__":
    relatorio = RelatorioVendas()
    relatorio.gerar("vendas_2024.xlsx")
```

### 4. Usar o Decorator para Medir Tempo

```python
from amaterasu.src.utils.helpers.timing import medir_tempo
import time

@medir_tempo
def processar_dados_grandes():
    """Função que será cronometrada"""
    time.sleep(2)
    return "Processamento concluído"

# Output: processar_dados_grandes levou 2.00s
processar_dados_grandes()
```

---

## 🔧 Dependências Principais

| Pacote | Versão | Descrição |
|--------|--------|-----------|
| `python-dotenv` | 1.0.0 | Carrega variáveis de ambiente de arquivos `.env` |
| `psycopg2-binary` | 2.9.9 | Adaptador PostgreSQL para Python |
| `pymongo` | 4.6.0 | Driver MongoDB |
| `pandas` | 2.1.0 | Manipulação e análise de dados |
| `openpyxl` | 3.1.0 | Geração e leitura de arquivos Excel |
| `sqlalchemy` | (implícito) | ORM e query builder |
| `pytest` | 7.4.0 | Framework de testes |
| `pytest-cov` | 4.1.0 | Medição de cobertura de testes |
| `black` | 23.11.0 | Formatador de código (PEP 8) |
| `flake8` | 6.1.0 | Linter para Python |
| `isort` | 5.12.0 | Organizador automático de imports |
| `taskipy` | 1.12.2 | Task runner para automação |

---

## ✨ A Filosofia Amaterasu

Assim como a deusa que traz luz após a escuridão, este projeto funciona com os seguintes princípios:

1. **Clareza** - Código legível e bem documentado
2. **Modularidade** - Templates reutilizáveis para diferentes tipos de tarefas
3. **Acessibilidade** - Fácil de usar e estender
4. **Transformação** - Dados brutos → Conhecimento estruturado
5. **Confiabilidade** - Tratamento robusto de erros e logging

---

## ⚙️ Tarefas Disponíveis

Use `taskipy` para executar tarefas comuns:

```powershell
# Ver todas as tarefas disponíveis
task --list

# Formatar código (black + isort)
task format

# Gerar requirements.txt
task requirements

# Configurar Git (nome e email global)
task config_git

# Executar pre-commit (format + requirements + config git)
task pre_commit
```

Veja `pyproject.toml` para detalhes das configurações.

---

## 🧪 Testes

Execute os testes com pytest:

```powershell
# Rodar todos os testes
pytest tests/

# Rodar com mais verbosidade
pytest tests/ -v

# Gerar relatório de cobertura
pytest tests/ --cov=amaterasu

# Rodar um arquivo específico
pytest tests/test_etl.py
```

---

## 📝 Verificar Integridade do Projeto

Execute o script de teste de setup para verificar se todas as importações funcionam:

```powershell
python amaterasu/src/utils/test_setup.py
```

Este script testa se todos os módulos podem ser importados corretamente:
- ✓ env_config
- ✓ template_etl
- ✓ template_consulta
- ✓ template_relatorio

---

## 🛠️ Desenvolvimento Local

### Formatação de Código

```powershell
# Formatar com black
black amaterasu/ tests/

# Organizar imports com isort
isort amaterasu/ tests/

# Combinar ambos
task format
```

### Validação de Código

```powershell
# Lint com flake8
flake8 amaterasu/ tests/

# Verificar tipo (se tiver type hints)
mypy amaterasu/ --ignore-missing-imports
```

---

## 🌏 Referência Mitológica

**Amaterasu-ōmikami** (天照大神) é a deusa suprema na mitologia japonesa, responsável pela iluminação do universo. Segundo a lenda, quando ela se escondeu em uma caverna, o mundo foi envolvido em completa escuridão. Os campos apodreceram, o caos reinou. Através de engenho e perseverança, os deuses a trouxeram de volta, restaurando a luz.

Este ciclo reflete perfeitamente o processo de ETL:
- 🌑 **Escuridão**: Dados desorganizados e sem sentido
- 🔄 **Transformação**: Processamento e refinamento (os deuses trabalhando)
- ☀️ **Iluminação**: Dados estruturados em conhecimento valioso

---

## 📚 Próximos Passos

1. Customize os templates `MeuETL`, `MinhaConsulta` e `MeuRelatorio` para suas necessidades
2. Configure seu `.env` com credenciais de banco de dados
3. Implemente suas conexões de banco de dados
4. Crie seus próprios pipelines herdando dos templates
5. Adicione testes para garantir qualidade

---

## 📝 Licença

Este projeto é fornecido como-está para fins de aprendizado e desenvolvimento.

---

## 👤 Autor

Desenvolvido com ☀️ e inspirado na mitologia japonesa.

---

> *"Assim como Amaterasu ilumina o céu, que este framework ilumine o caminho de seus dados."*

**Versão:** 1.0.0  
**Status:** Em Desenvolvimento ⚡  
**Última atualização:** 2024
