from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.empleado import Empleado
from app import db

bp = Blueprint('empleado', __name__)


    

@bp.route('/empleado')
def index():
    data = Empleado.query.all()
    return render_template('empleado/home.html')