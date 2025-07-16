from flask import render_template, request, redirect, url_for, flash
from codes.services import add_sweet as svc_add_sweet, insert_random_sweet as svc_insert_random_sweet
from codes.models import db, Sweet
from flask import Blueprint

create_routes = Blueprint('create_routes', __name__)

@create_routes.route('/add', methods=['GET', 'POST'])
def add_sweet():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        success, msg = svc_add_sweet(name, price, quantity)
        flash(msg, 'success' if success else 'danger')
        if success:
            return redirect(url_for('read_routes.index'))
        return redirect(url_for('create_routes.add_sweet'))
    return render_template('add.html')

@create_routes.route('/insert-random-sweet', methods=['POST'])
def insert_random_sweet():
    success, msg = svc_insert_random_sweet()
    flash(msg, 'success' if success else 'info')
    return redirect(url_for('read_routes.index')) 