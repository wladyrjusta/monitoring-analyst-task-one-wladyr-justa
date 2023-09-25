table_name = "checkout_1"

# Find Values Above the Average
# Encontre valores acima da média

AVG_LAST_WEEK_VALUES_ABOVE = (
    f"SELECT * FROM {table_name} WHERE avg_last_week > "
    f"(SELECT AVG(avg_last_week) FROM {table_name});"
)

# Find Values Below the Average
# Encontre valores abaixo da média

AVG_LAST_WEEK_VALUES_BELOW = (
    f"SELECT * FROM {table_name} WHERE avg_last_week < "
    f"(SELECT AVG(avg_last_week) FROM {table_name});"
)

# Find Records with Exceptions
# Encontre registros com exceções
# today value greater than twice the avg_last_week value
# valor de hoje maior que duas vezes o valor de avg_last_week

TODAY_VALUE_GREATER_THAN_TWICE_LAST_WEEK = (
    f"SELECT * FROM {table_name} WHERE today > (2 * avg_last_week);"
)

# Find Differences Between today and same_day_last_week
# Encontre diferenças entre hoje e same_day_last_week
# Find records where today is greater than same_day_last_week
# Encontre registros onde hoje é maior que same_day_last_week

TODAY_GREATER_THAN_SAME_DAY_LAST_WEEK = (
    f"SELECT * FROM {table_name} WHERE today > same_day_last_week;"
)

# Daily Growth Rate
# Taxa de crescimento diário
# This query calculates the daily growth in the "today" metric by subtracting
# the previous day's value from the current day's value
# Esta consulta calcula o crescimento diário na métrica "hoje" subtraindo
# o valor do dia anterior do valor do dia atual

DAILY_GROWTH_RATE = (
    f"SELECT time, today, today - LAG(today) OVER (ORDER BY time) "
    f"AS daily_growth FROM {table_name};"
)

# Weekly Growth Rate
# Taxa de crescimento semanal
# This query calculates the weekly growth in the "today" metric
# by subtracting the value from the same day of the previous week
# from the current day's value
# Esta consulta calcula o crescimento semanal na métrica "hoje" subtraindo
# o valor do mesmo dia da semana anterior do valor do dia atual

WEEKLY_GROWTH_RATE = (
    f"SELECT time, today, today - LAG(today, 7) OVER (ORDER BY time) "
    f"AS weekly_growth FROM {table_name};"
)
