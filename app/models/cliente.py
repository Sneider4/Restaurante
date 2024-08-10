from app import db 

class Cliente (db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)