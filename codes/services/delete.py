from codes.models import db, Sweet

def delete_sweet(sweet_id):
    sweet = db.session.get(Sweet, sweet_id)
    if not sweet:
        return False, 'Sweet not found.'
    db.session.delete(sweet)
    db.session.commit()
    return True, 'Sweet deleted!' 