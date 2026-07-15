"""
Configuração de Ambiente

Carrega variáveis de ambiente e configurações iniciais
"""
import os
from pathlib import Path


# Localiza o arquivo .env - procura em múltiplos lugares
def _find_env_file():
    possible_paths = [
        Path(__file__).parent.parent.parent.parent / '.env',  # /projeto/.env
        Path(__file__).parent.parent.parent / '.env',  # /amaterasu/.env
        Path.cwd() / '.env',  # diretório atual
    ]
    for path in possible_paths:
        if path.exists():
            return path
    return None


env_file = _find_env_file()

# Carrega o arquivo .env
if env_file:
    # Tenta usar dotenv se disponível
    try:
        from dotenv import load_dotenv

        load_dotenv(env_file)
    except (ImportError, AttributeError):
        # Se falhar, carrega manualmente
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip().strip('"\'')

# Config a partir de os.environ
config = os.environ

acesso_solar = {
    'dev': config.get('SOLAR_DEV'),
    'tst': config.get('SOLAR_TST'),
    'hml': config.get('SOLAR_HML'),
    'preprod': config.get('SOLAR_PREPROD'),
    'prod': config.get('SOLAR_PROD'),
}

acesso_procapi = {
    'dev': config.get('PROCAPI_DEV'),
    'tst': config.get('PROCAPI_TST'),
    'hml': config.get('PROCAPI_HML'),
    'preprod': config.get('PROCAPI_PREPROD'),
    'prod': config.get('PROCAPI_PROD'),
    'pg_prod': config.get('PROCAPI_PROD_PG'),
}

# Debug: Mostrar o que foi carregado
if __name__ == '__main__':
    print('📂 Arquivo .env encontrado:', env_file)
    print('\n🔍 Variáveis SOLAR carregadas:')
    for key, value in acesso_solar.items():
        if value:
            print(f'  ✅ {key}: {value[:50]}...')
        else:
            print(f'  ❌ {key}: None')
