from flask import Flask, render_template

from cliente import Cliente
from cliente_dao import ClienteDAO
from cliente_forma import ClienteForma

app = Flask(__name__)

titulo_app = 'Zona Fit (GYM)'


@app.route('/')
@app.route('/index.html')
def inicio():
    app.logger.debug('Entramos al path de inicio/')
    # Recuperamos los clientes de la BD
    clientes_db = ClienteDAO.seleccionar()
    # Creamos un formulario de cliente form vacio
    # creamos un objeto de la clase Cliente()
    cliente = Cliente()  # Utilizamos el objeto para rellenar los parametros del formulario
    cliente_forma = ClienteForma(obj=cliente)  # atravez de (obj) indicamos los parametros iniciales
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)


if __name__ == '__main__':
    app.run(debug=True)
