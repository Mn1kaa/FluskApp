# Toastmasters APP (Delegación Semanal de  Roles)

#Flask

from flask import Flask,session
from flask_bootstrap import Bootstrap
import  datetime
from flask import request, make_response, redirect,render_template  # Usado para obtener IP, redireccionar y renderizar los templates... 
from flask import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField()
from wtforms.validators import DataRequired
app= Flask(__name__)
bootsrap = Bootstrap(app)

app.config['SECRET_KEY']= 'Secreto'

@app.errorhandler(404)

def not_found(error):
    return render_template('404.html',error=error)


@app.route('/')  ## route recibe la ruta donde queremos correr la función
def Toastmaster():
    # IP=request.cookies.get('user_ip')   // cookie sin seguridad

    
    now = datetime.datetime.now()
   

    return render_template('index.html',time=now)

@app.route('/miembros')
def Socios():
    
    response= make_response(redirect('/'))
    user_ip = request.remote_addr
    session['user_ip']= user_ip
    
    user_ip=session.get(user_ip)  
    
    
    # response.set_cookie('user_ip',user_ip)
    return response

class NewMember(FlaskForm):
    new_user= StringField('Nombre del nuevo miembro',validators=DataRequired())
    password = PasswordField('Contraseña de registro',validators=(DataRequired))
    create_user=SubmitField('Agregar Miembro')