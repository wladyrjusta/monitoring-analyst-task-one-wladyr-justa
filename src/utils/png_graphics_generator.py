import matplotlib.pyplot as plt
import io
import base64


def generate_graphic(dataframe, title, description):
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

    # Salvar o gráfico em memória
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)

    # Converter a imagem para base64
    image_base64 = base64.b64encode(buffer.read()).decode()
    buffer.close()

    # Crie um dicionário com as informações do gráfico
    graphic_data = {
        'title': title,
        'description': description,
        'image_base64': image_base64
    }

    return graphic_data
