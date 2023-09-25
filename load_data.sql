-- Carregar dados CSV1 em checkout_1
LOAD DATA INFILE '/var/lib/mysql-files/checkout_1.csv'
INTO TABLE checkout_1
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

-- Carregar dados CSV2 em checkout_2
LOAD DATA INFILE '/var/lib/mysql-files/checkout_2.csv'
INTO TABLE checkout_2
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

