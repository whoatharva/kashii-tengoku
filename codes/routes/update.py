from codes.services import purchase_sweet as svc_purchase_sweet, restock_sweet as svc_restock_sweet
from codes.models import db, Sweet
from flask import Blueprint, redirect, url_for, flash

update_routes = Blueprint('update_routes', __name__)

@update_routes.route('/purchase/<int:sweet_id>', methods=['POST'])
def purchase_sweet(sweet_id):
    success, msg = svc_purchase_sweet(sweet_id)
    flash(msg, 'success' if success else 'danger')
    return redirect(url_for('read_routes.index'))

@update_routes.route('/restock/<int:sweet_id>', methods=['POST'])
def restock_sweet(sweet_id):
    success, msg = svc_restock_sweet(sweet_id)
    flash(msg, 'success' if success else 'danger')
    return redirect(url_for('read_routes.index')) 