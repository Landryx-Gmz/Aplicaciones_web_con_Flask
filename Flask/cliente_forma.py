from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


# Clase que define un formulario web usando Flask-WTF, una extensión de Flask que facilita el manejo de formularios con validación integrada.
class ClienteForma(FlaskForm):
    # Tipos de campos que se usarán en el formulario
    nombre = StringField('Nombre', validators=[DataRequired()])  # - StringField: para texto.
    apellido = StringField('Apellido',
                           validators=[DataRequired()])  # - DataRequired: si el campo está vacío, se genera un error.
    membresia = IntegerField('Membresia', validators=[DataRequired()])  # - IntegerField: para números enteros.

    # Boton
    guardar = SubmitField('Guardar')  # - SubmitField: para el botón de envío.
