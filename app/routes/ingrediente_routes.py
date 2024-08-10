from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.ingrediente import Ingrediente
from app import db

bp = Blueprint('ingrediente', __name__)

@bp.route('/Ingrediente')
def index():
    data = Ingrediente.query.all()
    return render_template('ingrediente/home.html', data=data)