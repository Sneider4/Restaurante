from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.reserva import Reserva
from app import db

bp = Blueprint('reserva', __name__)

@bp.route('/Reserva')
def index():
    data = Reserva.query.all()
    return render_template('reserva/home.html', data=data)