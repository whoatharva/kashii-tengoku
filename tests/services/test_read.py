import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from app import app
from codes.models import db, Sweet
from codes.services import get_sweets, SAMPLE_SWEETS

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

def test_get_sweets_search():
    with app.app_context():
        sweets = get_sweets(query='Taiyaki', action='search')
        assert any('Taiyaki' in s.name for s in sweets)
        assert all('Taiyaki' in s.name for s in sweets)

def test_get_sweets_sort():
    with app.app_context():
        sweets = get_sweets(sort='price', action='sort')
        assert sweets[0].price <= sweets[-1].price 