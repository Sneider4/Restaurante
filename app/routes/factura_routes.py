from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.factura import Factura
from app import db

bp = Blueprint('factura', __name__)

@bp.route('/Factura')
def index():
    data = Factura.query.all()
    return render_template('factura/home.html', data=data)