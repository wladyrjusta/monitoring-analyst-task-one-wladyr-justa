from queries import SQL_queries
from database.get_mysql_connection import get_mysql_connection
from model.execute_sql_querie import execute_query_and_get_dataframe
from utils.png_graphics_generator import generate_graphic
from utils.html_graphics_generator import generate_combined_html_page

CONNECTOR = get_mysql_connection()
TABLE_NAME = "checkout_1"

AVG_LAST_WEEK_VALUES_ABOVE_QUERY = SQL_queries.AVG_LAST_WEEK_VALUES_ABOVE
AVG_LAST_WEEK_VALUES_BELOW_QUERY = SQL_queries.AVG_LAST_WEEK_VALUES_BELOW
TODAY_VALUE_GREATER_THAN_TWICE_LAST_WEEK_QUERY = (
    SQL_queries.TODAY_VALUE_GREATER_THAN_TWICE_LAST_WEEK
)
TODAY_GREATER_THAN_SAME_DAY_LAST_WEEK_QUERY = (
    SQL_queries.TODAY_GREATER_THAN_SAME_DAY_LAST_WEEK
)
DAILY_GROWTH_RATE_QUERY = SQL_queries.DAILY_GROWTH_RATE
WEEKLY_GROWTH_RATE_QUERY = SQL_queries.WEEKLY_GROWTH_RATE

QUERIES_TO_EXECUTE = [
    {'AVERAGE_LAST_WEEK_VALUES_ABOVE': (
        AVG_LAST_WEEK_VALUES_ABOVE_QUERY
    ),
     'description': (
        "Esta consulta traz todos os dados da tabela que possuem o valor da"
        + "coluna 'avg_last_week'" + "maior do que a média dos valores dessa"
        + "coluna na mesma tabela. Em outras palavras, ela retorna "
        + "registros com um desempenho superior à média semanal anterior."
    )},
    {'AVERAGE_LAST_WEEK_VALUES_BELOW': (
        AVG_LAST_WEEK_VALUES_BELOW_QUERY
    ),
     'description': (
        "Esta consulta traz todos os dados da tabela que possuem o valor da"
        + "coluna 'avg_last_week'" + "abaixo do que a média dos valores dessa"
        + "coluna na mesma tabela. Em outras palavras, ela retorna "
        + "registros com um desempenho inferior à média semanal anterior."
    )},
    {'TODAY_VALUE_GREATER_THAN_TWICE_LAST_WEEK': (
        TODAY_VALUE_GREATER_THAN_TWICE_LAST_WEEK_QUERY
    ),
     'description': (
        "Essa consulta retorna todos os dados da tabela em que o valor da"
        + "coluna 'today' seja maior do que o dobro da média dos valores da"
        + " coluna 'avg_last_week' na mesma tabela. Em resumo, ela identifica "
        + "registros onde as transações diárias estão mais de duas vezes acima"
        + " da média semanal anterior."
    )},
    {'TODAY_VALUE_GREATER_THAN_SAME_DAY_LAST_WEEK': (
        TODAY_GREATER_THAN_SAME_DAY_LAST_WEEK_QUERY
    ),
     'description': (
        "Essa consulta retorna todos os dados da tabela em que o valor da "
        + " coluna 'today' seja maior do que o valor correspondente na coluna "
        + "'same_day_last_week'. Em resumo, ela seleciona registros onde as "
        + "transações diárias superaram as transações do mesmo"
        + "  dia da semana anterior."
    )},
    {'DAILY_GROWTH_RATE': (
        DAILY_GROWTH_RATE_QUERY
    ),
     'description': (
        "Esta consulta retorna a variação diária de transações, calculada em "
        + "relação ao horário anterior. Em resumo, ela fornece informações "
        + "detalhadas sobre a quantidade de transações por dia e a média do "
        + "crescimento diário em relação ao período anterior de 24 horas."
    )},
    {'WEEKLY_GROWTH_RATE': (
        WEEKLY_GROWTH_RATE_QUERY
    ),
     'description': (
        "Esta consulta retorna a variação semanal de transações, calculada em "
        + "relação ao mesmo horário sete dias atrás.Ela fornece uma análise do"
        + " crescimento semanal das transações, permitindo identificar se "
        + "houve aumento ou diminuição nas transações em relação aos valores "
        + "da semana anterior para cada horário registrado."
    )}
]


def generate_graphics_checkout_1():
    graphic_data = []
    for query_data in QUERIES_TO_EXECUTE:
        query_name = next(iter(query_data))
        query_description = query_data['description']
        query_sql = query_data[query_name]
        data_frame = execute_query_and_get_dataframe(
            CONNECTOR,
            query_sql,
            TABLE_NAME,
        )
        # gera graficos no formato .png e salva no diretório
        # passado como terceiro parâmetro
        data = generate_graphic(
            data_frame,
            f"{query_name}",
            f"{query_description}"
        )
        # gera graficos no formato .html e retorna-os
        # paraserem consumidos pelo endpoint POST/checkout_graphics
        graphic_data.append(data)
    html_content = generate_combined_html_page(graphic_data)
    return html_content
