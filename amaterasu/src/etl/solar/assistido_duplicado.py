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
        self.query_atendimento = load_sql_query('atendimento_assistido.sql')
        self.ids_assistidos_sem_atendimento = []

    def extrair_assistidos_duplicados(self):
        """Extrai IDs de assistidos duplicados usando query SQL"""
        with PostgresConnection(acesso_solar['prod']) as conn:
            self.assistidos_duplicados = conn.execute_query(self.query_duplicados)

    def valida_assistido_possui_atendimentos(self):
        """Valida se assistido possui atendimentos"""
        with PostgresConnection(acesso_solar['prod']) as conn:
            for assistido in self.assistidos_duplicados:
                id_assistido = assistido['id_assistido']
                query_atendimento = self.query_atendimento.format(id_assistido=id_assistido)
                atendimentos = conn.execute_query(query_atendimento)
                if not atendimentos:
                    self.ids_assistidos_sem_atendimento.append(id_assistido)

    def executar(self):
        self.extrair_assistidos_duplicados()
        self.valida_assistido_possui_atendimentos()


if __name__ == '__main__':
    etl = AssistidosDuplicadosETL()
    etl.executar()
