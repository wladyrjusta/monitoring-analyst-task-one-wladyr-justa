from queries import SQL_queries
from database.get_mysql_connection import get_mysql_connection
from model.execute_sql_querie import execute_query_and_get_dataframe
from utils.png_graphics_generator import generate_graphic
from utils.html_graphics_generator import generate_html_graphic

CONNECTOR = get_mysql_connection()
TABLE_NAME = "checkout_2"

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

QUERIES_TO_EXECUTE = {
    'AVERAGE_LAST_WEEK_VALUES_ABOVE': (
        AVG_LAST_WEEK_VALUES_ABOVE_QUERY
    ),
    'AVERAGE_LAST_WEEK_VALUES_BELOW': (
        AVG_LAST_WEEK_VALUES_BELOW_QUERY
    ),
    'TODAY_VALUE_GREATER_THAN_TWICE_LAST_WEEK': (
        TODAY_VALUE_GREATER_THAN_TWICE_LAST_WEEK_QUERY
    ),
    'TODAY_VALUE_GREATER_THAN_SAME_DAY_LAST_WEEK': (
        TODAY_GREATER_THAN_SAME_DAY_LAST_WEEK_QUERY
    ),
    'DAILY_GROWTH_RATE': (
        DAILY_GROWTH_RATE_QUERY
    ),
    'WEEKLY_GROWTH_RATE': (
        WEEKLY_GROWTH_RATE_QUERY
    ),
}


def generate_graphics_checkout_2():
    html_content = []
    for query in QUERIES_TO_EXECUTE:
        data_frame = execute_query_and_get_dataframe(
            CONNECTOR,
            QUERIES_TO_EXECUTE[query],
            TABLE_NAME,
        )
        generate_graphic(
            data_frame,
            f"{query}",
            "src/graphics_checkout_2"
        )
        html_content.append(generate_html_graphic(data_frame, f"{query}"))
    return html_content
