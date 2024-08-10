from app import db 

class Orden_detalle (db.Model):
    id_orden_detalle = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.String(255), nullable=False)

    plato = db.Column(db.Integer, db.ForeignKey('plato.id_plato'), nullable=False)
    bebida = db.Column(db.Integer, db.ForeignKey('bebida.id_bebida'), nullable=False)
