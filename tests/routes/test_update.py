import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from app import app, db
from codes.models import Sweet
from codes.routes import SAMPLE_SWEETS

@pytest.fixture(autouse=True)
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.drop_all()
        db.create_all()
        for s in SAMPLE_SWEETS:
            db.session.add(Sweet(name=s['name'], price=s['price'], quantity=10))
        db.session.commit()
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.drop_all()

def test_purchase_sweet(client):
    with app.app_context():
        sweet = Sweet.query.filter_by(name=SAMPLE_SWEETS[1]['name']).first()
        sweet_id = sweet.id
    rv = client.post(f'/purchase/{sweet_id}', follow_redirects=True)
    assert b'Purchased 1' in rv.data
    with app.app_context():
        sweet = db.session.get(Sweet, sweet_id)
        assert sweet.quantity == 9

def test_purchase_out_of_stock(client):
    with app.app_context():
        sweet = Sweet.query.filter_by(name=SAMPLE_SWEETS[2]['name']).first()
        sweet.quantity = 0
        db.session.commit()
        sweet_id = sweet.id
    rv = client.post(f'/purchase/{sweet_id}', follow_redirects=True)
    assert b'Out of stock!' in rv.data

def test_restock_sweet(client):
    with app.app_context():
        sweet = Sweet.query.filter_by(name=SAMPLE_SWEETS[3]['name']).first()
        sweet_id = sweet.id
        orig_qty = sweet.quantity
    rv = client.post(f'/restock/{sweet_id}', follow_redirects=True)
    assert b'Restocked 1' in rv.data
    with app.app_context():
        sweet = db.session.get(Sweet, sweet_id)
        assert sweet.quantity == orig_qty + 1 