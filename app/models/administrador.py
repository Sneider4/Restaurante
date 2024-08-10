from app import db 

class Administrador (db.Model):
    id_administrador = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)

    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id_rol'))
    rol = db.relationship('Rol', backref=db.backref('administradores', lazy=True))