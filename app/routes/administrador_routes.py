from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.administrador import Administrador
from app import db

bp = Blueprint('administrador', __name__)

@bp.route('/administrador')
def index():
    data = Administrador.query.all()
    return render_template('administrador/index.html', data=data)