from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db 

class Carrito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    producto_id = db.Column(db.Integer, nullable=False)
    producto_tipo = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, default=1)
    precio_unitario = db.Column(db.Float, nullable=False)


    def __repr__(self):
        return f'<Carrito {self.producto_id} - {self.producto_tipo}>'