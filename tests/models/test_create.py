import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from app import app
from codes.models import db, Sweet

@pytest.fixture(autouse=True)
def setup_db():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield
        db.drop_all()

def test_create_sweet():
    with app.app_context():
        sweet = Sweet(name='Test Sweet', price=100, quantity=5)
        db.session.add(sweet)
        db.session.commit()
        found = Sweet.query.filter_by(name='Test Sweet').first()
        assert found is not None
        assert found.price == 100
        assert found.quantity == 5

def test_unique_name_constraint():
    with app.app_context():
        sweet1 = Sweet(name='Unique Sweet', price=100, quantity=5)
        db.session.add(sweet1)
        db.session.commit()
        sweet2 = Sweet(name='Unique Sweet', price=200, quantity=10)
        db.session.add(sweet2)
        with pytest.raises(Exception):
            db.session.commit() 