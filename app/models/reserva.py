from app import db 
from datetime import datetime

class Reserva (db.Model):
    id_reserva = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    hora = db.Column(db.String(255), nullable=False)
    
    cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'))
    mesa = db.Column(db.Integer, db.ForeignKey('mesa.id_mesa'))