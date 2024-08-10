from app import db 

class Rol (db.Model):
    id_rol = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(255), nullable=False, unique=True)