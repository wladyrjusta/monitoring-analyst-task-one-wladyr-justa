def generate_combined_html_page(graphic_data):
    # Crie o cabeçalho HTML
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Gráficos</title>
    </head>
    <body>
    """

    # Adicione os gráficos base64 e legendas em tags <p> à página HTML
    for data in graphic_data:
        title = data['title']
        image_base64 = data['image_base64']
        description = data['description']

        html_content += f"<h2>{title}</h2>"
        html_content += (
            f"<img src='data:image/png;base64,{image_base64}' alt='{title}'>"
        )
        html_content += f"<h2>{description}</h2>"

    # Feche o corpo e o HTML
    html_content += """
    </body>
    </html>
    """

    return html_content
