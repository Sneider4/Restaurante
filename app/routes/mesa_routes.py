from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.mesa import Mesa


from app import db

bp = Blueprint('mesa', __name__)

@bp.route('/Mesa')
def index():
    mesas = Mesa.query.all()
    return render_template('mesa/index.html', mesa=mesas)

@bp.route('/Mesa/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        numero_mesa = request.form['numero_mesa']
        capacidad = request.form['capacidad']
        estado = request.form['estado']

        new_mesa = Mesa(numero_mesa=numero_mesa, capacidad=capacidad, estado=estado)
        db.session.add(new_mesa)
        db.session.commit()
        
        return redirect(url_for('mesa.index'))

    return render_template('mesa/add_mesa.html')

@bp.route('/Mesa/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    mesa = Mesa.query.get_or_404(id)

    if request.method == 'POST':
        mesa.capacidad = request.form['capacidad']
        mesa.estado = request.form['estado']
        db.session.commit()
        return redirect(url_for('mesa.index'))

    return render_template('mesa/edit.html', mesa=mesa)

@bp.route('/Mesa/delete/<int:id>')
def delete(id):
    mesa = Mesa.query.get_or_404(id)
    
    db.session.delete(mesa)
    db.session.commit()

    return redirect(url_for('mesa.index'))