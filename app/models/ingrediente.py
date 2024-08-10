from app import db 

class Ingrediente (db.Model):
    id_ingrediente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    cantidad_disponible = db.Column(db.Integer, nullable=False)

    proveedor = db.Column(db.Integer, db.ForeignKey('proveedor.id_proveedor'))