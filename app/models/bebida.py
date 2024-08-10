from app import db 

class Bebida (db.Model):
    id_bebida = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    imagen =db.Column(db.String(200), nullable=True)