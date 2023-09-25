import matplotlib.pyplot as plt


def generate_graphic(dataframe, title, file_dir_path):
    plt.figure(figsize=(10, 6))

    # Assume que a primeira coluna é a coluna X (eixo X)
    x_column = dataframe.columns[0]

    # Assume que todas as outras colunas são colunas Y (eixo Y)
    y_columns = dataframe.columns[1:]

    for column in y_columns:
        # Converte os valores para strings
        x_values = dataframe[x_column].astype(str)
        y_values = dataframe[column]
        plt.bar(x_values, y_values, label=column)

    plt.xlabel(x_column)
    plt.ylabel("Values")
    plt.title(title)
    plt.legend()
    plt.grid(True)

    plt.savefig(f"{file_dir_path}/{title}.png")
