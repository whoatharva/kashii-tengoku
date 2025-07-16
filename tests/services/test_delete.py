import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from app import app
from codes.models import db, Sweet
from codes.services import delete_sweet, SAMPLE_SWEETS

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

def test_delete_sweet():
    with app.app_context():
        sweet = Sweet.query.filter_by(name=SAMPLE_SWEETS[0]['name']).first()
        sweet_id = sweet.id
        success, msg = delete_sweet(sweet_id)
        assert success
        assert Sweet.query.get(sweet_id) is None 