from codes.models import db, Sweet

def purchase_sweet(sweet_id):
    sweet = db.session.get(Sweet, sweet_id)
    if not sweet:
        return False, 'Sweet not found.'
    if sweet.quantity < 1:
        return False, 'Out of stock!'
    sweet.quantity -= 1
    db.session.commit()
    return True, f'Purchased 1 {sweet.name}!'

def restock_sweet(sweet_id):
    sweet = db.session.get(Sweet, sweet_id)
    if not sweet:
        return False, 'Sweet not found.'
    sweet.quantity += 1
    db.session.commit()
    return True, f'Restocked 1 {sweet.name}!' 