# Toastmasters APP (Delegación Semanal de  Roles)

# Flask
from flask_wtf import FlaskForm
from flask import session, flash,request
import datetime
from flask import (
    request,
    make_response,
    redirect,
    render_template,
)  # Usado para obtener IP, redireccionar y renderizar los templates...W
import unittest
from app import create_app
import os
print(os.environ)



app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)


@app.route("/")  ## route recibe la ruta donde queremos correr la función
def Toastmaster():
    # IP=request.cookies.get('user_ip')   // cookie sin seguridad

    now = datetime.datetime.now()

    return render_template("index.html", time=now,members=[])



@app.route("/prueba")
def probando():
    response = make_response(redirect("/miembros"))
    return response



if __name__ == "__main__":
    app.run(host=os.environ.get("HOSTNAME"), port=os.environ.get("PORT"))




