from app import db

class DetallePlato(db.Model):
   __tablename__ = 'detalle_plato'
   id_detalle = db.Column(db.Integer, primary_key=True,autoincrement=True)
   id_factura = db.Column(db.Integer, db.ForeignKey('factura.id_factura'))
   id_plato = db.Column(db.Integer, db.ForeignKey('plato.id_plato'))
   cantidad = db.Column(db.Integer, nullable=False)