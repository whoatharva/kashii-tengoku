from codes.models import Sweet

def get_sweets(query=None, sort='name', action=None):
    sweets_query = Sweet.query
    if action == 'search' and query:
        sweets_query = sweets_query.filter(Sweet.name.op('REGEXP')(f'(?i){query}'))
        sweets_query = sweets_query.order_by(Sweet.name.asc())
    elif action == 'sort':
        if sort == 'name':
            sweets_query = sweets_query.order_by(Sweet.name.asc())
        elif sort == 'quantity':
            sweets_query = sweets_query.order_by(Sweet.quantity.asc())
        elif sort == 'price':
            sweets_query = sweets_query.order_by(Sweet.price.asc())
    else:
        sweets_query = sweets_query.order_by(Sweet.name.asc())
    return sweets_query.all() 