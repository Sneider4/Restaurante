from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from app.models.plato import Plato
from app.models.bebida import Bebida   
from app.models.carrito import Carrito

from app import db
import os

bp = Blueprint('plato', __name__)

@bp.route('/home')
@login_required
def home():
    plato = Plato.query.all()
    bebida = Bebida.query.all()
    carrito = Carrito.query.filter_by(user_id=current_user.id).all()

    subtotal = sum(item.precio_unitario * item.cantidad for item in carrito)
    impuesto = subtotal * 0.19
    total = subtotal + impuesto
    return render_template('plato/home.html', platos=plato, bebidas=bebida, carrito=carrito, subtotal=subtotal, impuesto=impuesto, total=total)

@bp.route('/Plato')
def index():
    plato = Plato.query.all()
    bebida = Bebida.query.all()
    return render_template('plato/index.html', platos=plato, bebidas=bebida)

@bp.route('/Plato/add', methods=['GET', 'POST'])
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
        
        new_plato = Plato(nombre=nombre, precio=precio, descripcion=descripcion, imagen=imagen.filename)
        db.session.add(new_plato)
        db.session.commit()
        
        return redirect(url_for('plato.index'))

    return render_template('plato/add_producto.html')

@bp.route('/Plato/elegir')
def elegir():
    return render_template('plato/elegir.html')

@bp.route('/Plato/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    plato = Plato.query.get_or_404(id)

    if request.method == 'POST':
        plato.nombre = request.form['nombre']
        plato.descripcion = request.form['descripcion']
        plato.precio = request.form['precio']
        imagen = request.files.get('imagen')

        if imagen:
            filename = secure_filename(imagen.filename)
            imagen_path = os.path.join('static', 'images', filename)
            imagen.save(os.path.join(os.path.dirname(__file__), '..', imagen_path))
            ruta_imagen = imagen_path
        
        db.session.commit()
        return redirect(url_for('plato.index'))

    return render_template('plato/edit.html', plato=plato)

@bp.route('/Plato/delete/<int:id>')
def delete(id):
    plato = Plato.query.get_or_404(id)
    
    db.session.delete(plato)
    db.session.commit()

    return redirect(url_for('plato.index'))



