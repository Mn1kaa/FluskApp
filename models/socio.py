from app import db

class Socio(db.Model):
    def __init__(self,name):
        self.name=name
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column((db.String(100)),unique=True)

    