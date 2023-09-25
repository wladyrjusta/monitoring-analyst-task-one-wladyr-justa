from flask import Flask
from controller.generate_graphic_controller import (
    generate_graphic_endpoint_checkout_1, generate_graphic_endpoint_checkout_2
)

app = Flask(__name__)


# Rota para gerar gráfico checkout_1
@app.route('/generate_graphic/checkout_1')
def generate_graphic_route_checkout_1():
    return generate_graphic_endpoint_checkout_1()


# Rota para gerar gráfico checkout_2
@app.route('/generate_graphic/checkout_2')
def generate_graphic_route_checkout_2():
    return generate_graphic_endpoint_checkout_2()


if __name__ == '__main__':
    app.run(debug=True)
