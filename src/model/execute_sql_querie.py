import pandas as pd


def execute_query_and_get_dataframe(connector, query, table_name):
    try:
        # Executa a query no banco de dados
        cursor = connector.cursor()
        cursor.execute(query)

        # Recupera as colunas do resultado da query
        columns = [desc[0] for desc in cursor.description]

        # Recupera os dados e cria um DataFrame Pandas
        data = cursor.fetchall()
        dataframe = pd.DataFrame(data, columns=columns)

        return dataframe
    except Exception as e:
        print(f"Erro ao executar a query na tabela '{table_name}': {str(e)}")
        return None
