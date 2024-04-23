
from . import members
from flask import render_template,abort
from flask import request,session,flash
from models.socio import socio
from app.forms import NewMember
import datetime 
from app import db
from sqlalchemy.exc import IntegrityError


import random
import re





DTM_PASSWORD = 'DCP_DTM_VERACRUZ'



@members.route("/add", methods=["GET", "POST"])



# def Socios():

#     response= make_response(redirect('/'))
#     user_ip = request.remote_addr
#     session['user_ip']= user_ip

#     user_ip=session.get(user_ip)


#     # response.set_cookie('user_ip',user_ip)
#     return response


def AddUser():
    now = datetime.datetime.now()
    new_member = NewMember()
    username = session.get("username")
  
    

    if new_member.validate_on_submit():
        username = new_member.new_user.data
        new_user = request.form['new_user']
        password = request.form['password']

        if DTM_PASSWORD==password:
            session["username"] = username 
            member=socio(new_user)
            try:
                db.session.add(member)
                db.session.commit()
            except IntegrityError as e:
                
                return render_template(
        "members.html",error=e,new_member=new_member
    )
    
                
                
           
            flash("Nuevo socio registrado correctamente")
            return render_template(
        "members.html",contraseña=password, time=now, new_member=new_member, usuario=username
    )

        else:
             flash("Contraseña incorrecta... no se ha podido guardar al nuevo miembro")
             return render_template(
        "members.html",contraseña=password, time=now, new_member=new_member, usuario=username
    )
        
   
   

    return render_template(
        "members.html", time=now, new_member=new_member, usuario=username
    )
@members.route("/chosenMembers", methods=["GET"])  ## route recibe la ruta donde queremos correr la función
def chosen_members():
    print("LAKSJDLASKDJKLS")
    
    arreglo_nombres_aleatorio=[]
    array_members=db.session.query(socio.name).all()
    now = datetime.datetime.now()
    longitud_arreglo_nombres=len(array_members)
    if len(array_members)<6:
        return {'plantilla':'Error'}
    while len(arreglo_nombres_aleatorio)<=6:
        numero_aleatorio=random.randint(0,longitud_arreglo_nombres-1    )
        if not array_members[numero_aleatorio] in arreglo_nombres_aleatorio:
            arreglo_nombres_aleatorio.append(array_members[numero_aleatorio])
            
        else:
            continue

    arreglo_nombres_aleatorio2=list(arreglo_nombres_aleatorio)
    arreglo_final=[]
    
    

    for element in arreglo_nombres_aleatorio2:
        element=str(element)
        arreglo_final.append(re.findall(r"[a-zA-Z ]+.\b",element))
    
    diccionario_final={'persona1':str(arreglo_final[0]).strip("['']"),
                       'persona2':str(arreglo_final[1]).strip("['']"),
                       'persona3':str(arreglo_final[2]).strip("['']"),
                       'persona4':str(arreglo_final[3]).strip("['']"),
                       'persona5':str(arreglo_final[4]).strip("['']"),
                       'persona6':str(arreglo_final[5]).strip("['']"),
                       'persona7':str(arreglo_final[6]).strip("['']")}
    
    
        
        
    
    
    return {'plantilla':render_template("index.html", time=now,members=diccionario_final)}

