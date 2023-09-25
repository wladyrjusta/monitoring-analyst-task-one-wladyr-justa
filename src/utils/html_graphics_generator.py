import matplotlib.pyplot as plt
import mpld3
from io import StringIO


def generate_html_graphic(dataframe, title):
    plt.figure(figsize=(10, 6))

    # Assume que a primeira coluna é a coluna X (eixo X)
    x_column = dataframe.columns[0]

    x_values = [f"{time}" for time in dataframe[x_column]]

    # Assume que todas as outras colunas são colunas Y (eixo Y)
    y_columns = dataframe.columns[1:]

    for column in y_columns:
        y_values = dataframe[column]
        plt.bar(x_values, y_values, label=column)

    plt.xlabel(x_column)
    plt.ylabel("Values")
    plt.title(title)
    plt.legend()
    plt.grid(True)

    # Salvar o gráfico como um arquivo HTML
    html_content = StringIO()

    # Aplicar um formato de data/hora específico ao eixo X do gráfico HTML
    ax = plt.gca()
    ax.xaxis.set_major_formatter(plt.FixedFormatter(x_values))

    mpld3.save_html(plt.gcf(), html_content)

    # Fechar a figura atual
    plt.close()

    return html_content.getvalue()
