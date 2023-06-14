# Toastmasters APP (Delegación Semanal de  Roles)

#Flask

from flask import session,flash
import  datetime
from flask import request, make_response, redirect,render_template  # Usado para obtener IP, redireccionar y renderizar los templates... 

import unittest
from app import create_app
from app.forms import NewMember

app =create_app()




@app.cli.command()
def test():
     tests= unittest.TestLoader().discover('tests')
     unittest.TextTestRunner().run(tests)
@app.errorhandler(404)

def not_found(error):
    return render_template('404.html',error=error)


@app.route('/')  ## route recibe la ruta donde queremos correr la función
def Toastmaster():
    # IP=request.cookies.get('user_ip')   // cookie sin seguridad

    
    now = datetime.datetime.now()
   

    return render_template('index.html',time=now)
@app.route('/prueba')
def probando():
     response= make_response(redirect('/miembros'))
     return response
@app.route('/miembros', methods=["GET",'POST'])
# def Socios():
    
#     response= make_response(redirect('/'))
#     user_ip = request.remote_addr
#     session['user_ip']= user_ip
    
#     user_ip=session.get(user_ip)  
    
    
#     # response.set_cookie('user_ip',user_ip)
#     return response

def AddUser():
     now = datetime.datetime.now()
     new_member=(NewMember())
     username=session.get('username')

     if new_member.validate_on_submit():
          username= new_member.new_user.data
          session['username']= username
          flash('Nuevo socio registrado correctamente')
          


     return render_template('members.html',time=now,new_member=new_member,usuario=username) 



    