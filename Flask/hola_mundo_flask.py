# from flask import Flask  # Importacion del modulo Flask
#
# app = Flask(__name__)  # - Creando la aplicación web.
#
#
# # ---Definir una ruta (endpoint)---
#
# # - decorador que le dice a Flask: “Cuando el usuario visite la raíz del sitio (/), ejecuta la función inicio()”.
#
# @app.route('/')  # url: http://localhost:5000/
# # Agregamos otra ruta:
# @app.route('/index.html')  # url http://localhost:5000/index.html
# def inicio():
#     app.logger.debug(
#         'Entramos en el path de inicio /')  # -Escribe un mensaje en el log en nivel debug. Útil para desarrolladores que quieren saber qué está pasando internamente.
#
#     return '<p>Hola Mundo</p>'  # -Envía una respuesta HTML al navegador. En este caso, un simple párrafo con el texto "Hola Mundo".
#
#
# # Ejecutar la aplicación
# if __name__ == '__main__':
#     app.run(debug=True)  # - inicia el servidor de desarrollo de Flask:
