from app import db 

class Mesa (db.Model):
    id_mesa = db.Column(db.Integer, primary_key=True)
    numero_mesa = db.Column(db.Integer, nullable=False, unique=True)
    capacidad = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(20), nullable=False, default='disponible')