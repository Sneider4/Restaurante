from app import db
from datetime import datetime

class Factura (db.Model):
    id_factura = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime(255), nullable=False)
    total = db.Column(db.Float, nullable=False)
    
    
    cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'))
    empleado = db.Column(db.Integer, db.ForeignKey('empleado.id_empleado'))
    mesa = db.Column(db.Integer, db.ForeignKey('mesa.id_mesa'))