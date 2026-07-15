"""
Template de Script ETL

Use este arquivo como base para criar novos scripts ETL
"""

class MeuETL:
    """
    Classe para processar ETL de uma fonte de dados
    
    Padrão de implementação:
    1. Extração (extract): Buscar dados da fonte
    2. Transformação (transform): Processar e validar dados
    3. Carregamento (load): Salvar no banco de dados
    """
    
    def __init__(self):
        """Inicializa o ETL"""
        self.nome = "Meu ETL"
        print(f"Iniciando {self.nome}")
    
    def extract(self):
        """
        Extrai dados da fonte
        
        Returns:
            list: Lista de dados extraídos
        """
        print("Extraindo dados...")
        # TODO: Implementar extração
        dados = []
        print(f"Extração concluída: {len(dados)} registros")
        return dados
    
    def transform(self, dados: list):
        """
        Transforma e valida os dados
        
        Args:
            dados: Dados a transformar
        
        Returns:
            list: Dados transformados
        """
        print(f"Transformando {len(dados)} registros...")
        # TODO: Implementar transformação
        dados_transformados = []
        print("Transformação concluída")
        return dados_transformados
    
    def load(self, dados: list):
        """
        Carrega os dados no banco de dados
        
        Args:
            dados: Dados a carregar
        
        Returns:
            int: Número de registros carregados
        """
        print(f"Carregando {len(dados)} registros...")
        # TODO: Implementar carregamento
        registros_carregados = 0
        print(f"Carregamento concluído: {registros_carregados} registros")
        return registros_carregados
    
    def executar(self):
        """Executa o pipeline completo de ETL"""
        try:
            dados = self.extract()
            dados_transformados = self.transform(dados)
            registros = self.load(dados_transformados)
            print(f"{self.nome} executado com sucesso!")
            return registros
        except Exception as e:
            print(f"Erro ao executar {self.nome}: {e}")
            raise

if __name__ == "__main__":
    etl = MeuETL()
    etl.executar()
