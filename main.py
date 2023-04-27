# Toastmasters APP (Delegación Semanal de  Roles)

#Flask

from flask import Flask
import  datetime
from flask import request, make_response, redirect,render_template  # Usado para obtener IP, redireccionar y renderizar los templates... 

app= Flask(__name__)

@app.route('/')  ## route recibe la ruta donde queremos correr la función
def Toastmaster():
    IP=request.cookies.get('user_ip')
    now = datetime.datetime.now()

    return render_template('index.html',time=now)

@app.route('/miembros')
def Socios():
    user_ip= request.remote_addr
    response= make_response(redirect('/'))
    response.set_cookie('user_ip',user_ip)
    return response
