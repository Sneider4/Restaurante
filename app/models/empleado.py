from app import db 

class Empleado (db.Model):
    id_empleado = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    
    rol = db.Column(db.Integer, db.ForeignKey('rol.id_rol'))