from app import db
from sqlalchemy import Sequence


class socio(db.Model):
    id=db.Column((db.Integer),primary_key=True,unique=True,autoincrement=True)
    name=db.Column((db.String(100)),unique=True)    
    def __init__(self,name):
        self.name=name
        


    