from flask import Flask, render_template, url_for, redirect

from cliente import Cliente
from cliente_dao import ClienteDAO
from cliente_forma import ClienteForma

app = Flask(__name__)

# Creamos nuestra clave secreta para evitar vulneravilidad y poder procesar los campos con WTF
app.config['SECRET_KEY'] = 'llave_secreta_123'  # llave antivulnerabilidad tipo CSRF

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


# Nuevo decorador para ruta de boton guardar
@app.route('/guardar', methods=['POST'])
def guardar():
    # Creamos los objetos de cliente inicialmente (objetos vacios)
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    # validamos si los valosres del formulario son validos con : .validate_on_submit()
    if cliente_forma.validate_on_submit():
        # Llenamos el objeto cliente con  los valores del formulario con: .populate_obj(cliente)
        cliente_forma.populate_obj(cliente)
        # Guardamos el nuevo cliente en la BD
        ClienteDAO.insertar(cliente)
    # Redireccionar a la pagina de inicio con: redirect(url_for('nombre_metodo'))
    return redirect(url_for('inicio'))


# Decorador para ruta limpiar
@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))


if __name__ == '__main__':
    app.run(debug=True)
