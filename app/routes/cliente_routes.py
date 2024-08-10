from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.cliente import Cliente
from app import db
    
bp = Blueprint('cliente', __name__)

@bp.route('/Cliente')
def index():
    data = Cliente.query.all()
    return render_template('cliente/home.html', data=data)