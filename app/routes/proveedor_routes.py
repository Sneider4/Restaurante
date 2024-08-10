from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.proveedor import Proveedor
from app import db

bp = Blueprint('proveedor', __name__)

@bp.route('/Proveedor')
def index():
    data = Proveedor.query.all()
    return render_template('proveedor/home.html', data=data)