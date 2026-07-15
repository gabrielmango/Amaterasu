from dotenv import dotenv_values, load_dotenv

load_dotenv()

config = dotenv_values('.env')

acesso_solar = {
    'dev': config['SOLAR_DEV'],
    'tst': config['SOLAR_TST'],
    'hml': config['SOLAR_HML'],
    'preprod': config['SOLAR_PREPROD'],
    'prod': config['SOLAR_PROD'],
}

acesso_procapi = {
    'dev': config['PROCAPI_DEV'],
    'tst': config['PROCAPI_TST'],
    'hml': config['PROCAPI_HML'],
    'preprod': config['PROCAPI_PREPROD'],
    'prod': config['PROCAPI_PROD'],
    'pg_prod': config['PROCAPI_PROD_PG'],
}
