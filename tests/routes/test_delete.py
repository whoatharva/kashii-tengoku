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

def test_delete_sweet(client):
    with app.app_context():
        sweet = Sweet.query.filter_by(name=SAMPLE_SWEETS[0]['name']).first()
        sweet_id = sweet.id
    rv = client.post(f'/delete/{sweet_id}', follow_redirects=True)
    assert b'Sweet deleted!' in rv.data
    assert SAMPLE_SWEETS[0]['name'].encode() not in rv.data 