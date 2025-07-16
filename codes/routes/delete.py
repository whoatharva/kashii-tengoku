from flask import redirect, url_for, flash
from codes.services import delete_sweet as svc_delete_sweet
from codes.models import db, Sweet
from flask import Blueprint

delete_routes = Blueprint('delete_routes', __name__)

@delete_routes.route('/delete/<int:sweet_id>', methods=['POST'])
def delete_sweet(sweet_id):
    success, msg = svc_delete_sweet(sweet_id)
    flash(msg, 'info' if success else 'danger')
    return redirect(url_for('read_routes.index')) 