from flask import render_template, request
from codes.services import get_sweets
from flask import Blueprint

read_routes = Blueprint('read_routes', __name__)

@read_routes.route('/', methods=['GET'])
def index():
    query = request.args.get('q', '', type=str)
    sort = request.args.get('sort', 'name', type=str)
    action = request.args.get('action', '', type=str)
    sweets = get_sweets(query=query, sort=sort, action=action)
    return render_template('index.html', sweets=sweets, query=query, sort=sort)

@read_routes.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '', type=str)
    sort = request.args.get('sort', 'name', type=str)
    action = request.args.get('action', '', type=str)
    sweets = get_sweets(query=query, sort=sort, action=action)
    return render_template('_table.html', sweets=sweets) 