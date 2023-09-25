from flask import Flask
from view.generate_graphics_checkout_1 import generate_graphics_checkout_1
from view.generate_graphics_checkout_2 import generate_graphics_checkout_2
from flask import Response

app = Flask(__name__)


@app.route('/generate_graphic/checkout_1')
def generate_graphic_endpoint_checkout_1():
    # Gere o gráfico HTML
    html_graphic = generate_graphics_checkout_1()

    # Retorne o gráfico HTML como resposta
    return Response(html_graphic, content_type='text/html')


@app.route('/generate_graphic/checkout_2')
def generate_graphic_endpoint_checkout_2():
    # Gere o gráfico HTML
    html_graphic = generate_graphics_checkout_2()

    # Retorne o gráfico HTML como resposta
    return Response(html_graphic, content_type='text/html')


if __name__ == '__main__':
    app.run(debug=True)
