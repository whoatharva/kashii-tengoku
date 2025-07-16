import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from app import app
from codes.models import db, Sweet
from codes.services import purchase_sweet, restock_sweet, SAMPLE_SWEETS


#UPDATE TESTS
@pytest.fixture(autouse=True)
def setup_db():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.drop_all()
        db.create_all()
        for s in SAMPLE_SWEETS:
            db.session.add(Sweet(name=s['name'], price=s['price'], quantity=10))
        db.session.commit()
        yield
        db.drop_all()

def test_purchase_sweet():
    with app.app_context():
        sweet = Sweet.query.filter_by(name=SAMPLE_SWEETS[1]['name']).first()
        sweet_id = sweet.id
        success, msg = purchase_sweet(sweet_id)
        assert success
        sweet = db.session.get(Sweet, sweet_id)
        assert sweet.quantity == 9

def test_purchase_out_of_stock():
    with app.app_context():
        sweet = Sweet.query.filter_by(name=SAMPLE_SWEETS[2]['name']).first()
        sweet.quantity = 0
        db.session.commit()
        sweet_id = sweet.id
        success, msg = purchase_sweet(sweet_id)
        assert not success
        assert 'Out of stock' in msg

def test_restock_sweet():
    with app.app_context():
        sweet = Sweet.query.filter_by(name=SAMPLE_SWEETS[3]['name']).first()
        sweet_id = sweet.id
        orig_qty = sweet.quantity
        success, msg = restock_sweet(sweet_id)
        assert success
        sweet = db.session.get(Sweet, sweet_id)
        assert sweet.quantity == orig_qty + 1 