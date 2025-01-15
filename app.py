from flask import Flask
from rutas.rutas_bebidas import bp_bebidas
from rutas.rutas_clientes import bp_clientes

app = Flask(__name__)

app.register_blueprint(bp_bebidas)
app.register_blueprint(bp_clientes)

if __name__ == "__main__":
    app.run(debug=True)