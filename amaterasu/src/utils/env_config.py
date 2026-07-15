"""
Configuração de Ambiente

Carrega variáveis de ambiente e configurações iniciais
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega arquivo .env
env_file = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_file)

# Configurações de Ambiente
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev").lower()
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Banco de Dados - PostgreSQL
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
POSTGRES_DB = os.getenv("POSTGRES_DB", "seu_banco")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")

# Banco de Dados - MongoDB
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DB = os.getenv("MONGODB_DB", "seu_banco_mongo")

# API/Integração
API_BASE_URL = os.getenv("API_BASE_URL", "")
API_KEY = os.getenv("API_KEY", "")

# Data
DATA_DIR = Path(__file__).parent.parent.parent / "dados"
DATA_DIR.mkdir(exist_ok=True)

def get_database_url(database_type="postgres"):
    """
    Constrói URL de conexão com o banco de dados
    
    Args:
        database_type: 'postgres' ou 'mongodb'
    
    Returns:
        str: URL de conexão
    """
    if database_type == "postgres":
        return f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    elif database_type == "mongodb":
        return MONGODB_URI
    else:
        raise ValueError(f"Database type '{database_type}' não suportado")
