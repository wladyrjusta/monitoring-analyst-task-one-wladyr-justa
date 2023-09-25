FROM mysql:8.0.32

# Definindo a senha do root do MySQL
ENV MYSQL_ROOT_PASSWORD=A5bR8tL1pX9

# Cria um banco de dados e uma tabela
ENV MYSQL_DATABASE=sales_monitoring

# Expõe a porta 3306 para acesso externo
EXPOSE 3306

# Copia os arquivos CSV para a pasta permitida e executa os comandos SQL
COPY checkout_1.csv /var/lib/mysql-files/
COPY checkout_2.csv /var/lib/mysql-files/
COPY create_table.sql /docker-entrypoint-initdb.d/
COPY load_data.sql /docker-entrypoint-initdb.d/
