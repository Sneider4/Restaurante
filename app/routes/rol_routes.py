from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.rol import Rol
from app import db

bp = Blueprint('rol', __name__)

@bp.route('/Rol')
def index():
    data = Rol.query.all()
    return render_template('rol/home.html', data=data)