from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class NewMember(FlaskForm):
        new_user= StringField('Nombre del nuevo miembro',validators=[DataRequired()])
        password = PasswordField('Contraseña de registro',validators=[DataRequired()])
        create_user=SubmitField('Agregar Miembro')

