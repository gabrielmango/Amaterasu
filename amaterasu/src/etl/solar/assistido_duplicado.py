from amaterasu.src.etl.template_etl import MeuETL
from amaterasu.src.utils.database.postgres_connection import PostgresConnection
from amaterasu.src.utils.env_config import acesso_solar
from amaterasu.src.utils.helpers.sql_loader import load_sql_query


class AssistidosDuplicadosETL(MeuETL):
    def __init__(self):
        super().__init__()
        self.nome = 'Assistidos Duplicados ETL'
        self.assistidos_duplicados = None
        self.query_duplicados = load_sql_query('id_assistidos_duplicados.sql')

    def extrair_assistidos_duplicados(self):
        """Extrai IDs de assistidos duplicados usando query SQL"""
        with PostgresConnection(acesso_solar['prod']) as conn:
            self.assistidos_duplicados = conn.execute_query(self.query_duplicados)

        print(self.assistidos_duplicados)

    def valida_assistido_possui_atendimentos(self):
        """Valida se assistido possui atendimentos"""
        pass

    def executar(self):
        self.extrair_assistidos_duplicados()


if __name__ == '__main__':
    etl = AssistidosDuplicadosETL()
    etl.executar()
