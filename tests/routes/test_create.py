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

def test_add_sweet(client):
    rv = client.post('/add', data={
        'name': 'Test Sweet',
        'price': 123,
        'quantity': 5
    }, follow_redirects=True)
    assert b'Sweet added successfully!' in rv.data
    assert b'Test Sweet' in rv.data

def test_add_duplicate_sweet(client):
    client.post('/add', data={'name': 'Test Sweet', 'price': 123, 'quantity': 5})
    rv = client.post('/add', data={'name': 'Test Sweet', 'price': 123, 'quantity': 5}, follow_redirects=True)
    assert b'already exists' in rv.data

def test_insert_random_sweet(client):
    with app.app_context():
        Sweet.query.delete()
        db.session.add(Sweet(name='Only Sweet', price=100, quantity=1))
        db.session.commit()
    rv = client.post('/insert-random-sweet', follow_redirects=True)
    assert b'Added' in rv.data or b'already in the shop' in rv.data

def test_add_page_loads(client):
    rv = client.get('/add')
    assert rv.status_code == 200
    assert b'Add a New Sweet' in rv.data 