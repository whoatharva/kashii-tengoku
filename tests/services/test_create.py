import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from app import app
from codes.models import db, Sweet
from codes.services import add_sweet, insert_random_sweet, SAMPLE_SWEETS

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

def test_add_sweet():
    with app.app_context():
        success, msg = add_sweet('Service Sweet', 123, 5)
        assert success
        sweet = Sweet.query.filter_by(name='Service Sweet').first()
        assert sweet is not None
        assert sweet.price == 123
        assert sweet.quantity == 5

def test_add_duplicate_sweet():
    with app.app_context():
        add_sweet('Service Sweet', 123, 5)
        success, msg = add_sweet('Service Sweet', 123, 5)
        assert not success
        assert 'already exists' in msg

def test_insert_random_sweet():
    with app.app_context():
        Sweet.query.delete()
        db.session.add(Sweet(name='Only Sweet', price=100, quantity=1))
        db.session.commit()
        success, msg = insert_random_sweet()
        assert success or 'already in the shop' in msg 