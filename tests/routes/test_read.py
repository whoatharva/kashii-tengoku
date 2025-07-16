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

def test_home_page_loads(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Kashii Tengoku' in rv.data
    assert b'Name' in rv.data

def test_search_sweet(client):
    rv = client.get('/search?q=Taiyaki&sort=name&action=search')
    assert b'Taiyaki' in rv.data
    assert b'Dango' not in rv.data

def test_sort_by_price(client):
    rv = client.get('/search?q=&sort=price&action=sort')
    assert b'Purin' in rv.data or b'Manju' in rv.data 