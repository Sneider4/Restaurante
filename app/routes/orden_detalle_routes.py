from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.orden_detalle import Orden_detalle
from app import db

bp = Blueprint('orden_detalle', __name__)

@bp.route('/Orden_detalle')
def index():
    data = Orden_detalle.query.all()
    return render_template('orden_detalle/home.html', data=data)