from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from app.models.bebida import Bebida
from app import db
import os

bp = Blueprint('bebida', __name__)

@bp.route('/bebida')
def home():
    bebida = Bebida.query.all()
    return render_template('bebida/home.html', bebidas=bebida)

@bp.route('/Bebida/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        imagen = request.files['imagen'] 

        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'images', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            ruta_imagen = imagen_path

        else:
            ruta_imagen = None
        
        new_bebida = Bebida(nombre=nombre, precio=precio, descripcion=descripcion, imagen=imagen.filename)
        db.session.add(new_bebida)
        db.session.commit()
        
        return redirect(url_for('plato.index'))

    return render_template('bebida/add_bebida.html')

@bp.route('/Bebida/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    bebida = Bebida.query.get_or_404(id)

    if request.method == 'POST':
        bebida.nombre = request.form['nombre']
        bebida.descripcion = request.form['descripcion']
        bebida.precio = request.form['precio']
        imagen = request.files.get('imagen')

        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'images', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            ruta_imagen = imagen_path
        
        db.session.commit()
        return redirect(url_for('plato.index'))

    return render_template('bebida/edit.html', bebida=bebida)

@bp.route('/Bebida/delete/<int:id>')
def delete(id):
    bebida = Bebida.query.get_or_404(id)
    
    db.session.delete(bebida)
    db.session.commit()

    return redirect(url_for('plato.index'))

