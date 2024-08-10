from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from app.models.carrito import Carrito
from app.models.plato import Plato
from app.models.bebida import Bebida
from flask_login import login_required,current_user
from app import db
from flask import redirect, url_for, request

bp = Blueprint('carrito', __name__)



@bp.route('/agregar_al_carrito/<int:producto_id>/<string:tipo>', methods=['POST'])
@login_required
def agregar_al_carrito(producto_id, tipo):
    if tipo == 'plato':
        producto = Plato.query.get_or_404(producto_id)
    elif tipo == 'bebida':
        producto = Bebida.query.get_or_404(producto_id)
    else:
        flash('Tipo de producto no válido', 'danger')
        return redirect(url_for('home'))

    # Verificar si el producto ya está en el carrito
    item_existente = Carrito.query.filter_by(
        user_id=current_user.id,
        producto_id=producto_id,
        producto_tipo=tipo
    ).first()

    if item_existente:
        # Si el ítem ya existe, puedes actualizar la cantidad si es necesario
        item_existente.cantidad += 1
    else:
        # Crear un nuevo ítem de carrito
        nuevo_item = Carrito(
            user_id=current_user.id,
            producto_id=producto_id,
            producto_tipo=tipo,
            cantidad=1,
            precio_unitario=producto.precio,
            nombre=producto.nombre
        )
        db.session.add(nuevo_item)

    db.session.commit()
    flash(f'{producto.nombre} ha sido agregado al carrito', 'success')
    return redirect(url_for('plato.home'))
