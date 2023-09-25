-- Criação da tabela para o primeiro CSV (checkout_1), se ela não existir
CREATE TABLE IF NOT EXISTS checkout_1 (
    time VARCHAR(5) NOT NULL,
    today INT NOT NULL,
    yesterday INT NOT NULL,
    same_day_last_week INT NOT NULL,
    avg_last_week DECIMAL(5, 2),
    avg_last_month DECIMAL(5, 2)
);

-- Criação da tabela para o segundo CSV (checkout_2), se ela não existir
CREATE TABLE IF NOT EXISTS checkout_2 (
    time VARCHAR(5) NOT NULL,
    today INT NOT NULL,
    yesterday INT NOT NULL,
    same_day_last_week INT NOT NULL,
    avg_last_week DECIMAL(5, 2),
    avg_last_month DECIMAL(5, 2)
);
