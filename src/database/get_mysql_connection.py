import mysql.connectorcod


def get_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='A5bR8tL1pX9',
            database='sales_monitoring'
        )
        return connection
    except Exception as e:
        print("Erro ao conectar ao MySQL:", str(e))
        return None
