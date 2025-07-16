from codes.models import db, Sweet
import random

SAMPLE_SWEETS = [
    {"name": "Dango ( 6e3 50)", "price": 300},
    {"name": "Castella ( 30ab 30b9 30c6 30e9)", "price": 400},
    {"name": "Matcha Mochi ( 62b9 836 905)", "price": 350},
    {"name": "Ichigo Daifuku ( 304 306 305 392 798f)", "price": 450},
    {"name": "Dorayaki ( 306 389 713c 304)", "price": 320},
    {"name": "Taiyaki ( 305 304 713c 304)", "price": 380},
    {"name": "Kakig 4dri ( 304 304 6c37)", "price": 250},
    {"name": "Yokan ( 7f8a 7fb9)", "price": 300},
    {"name": "Purin ( 30d7 30ea 30f3)", "price": 280},
    {"name": "Manju ( 945 982d)", "price": 270},
]

def add_sweet(name, price, quantity):
    if Sweet.query.filter_by(name=name).first():
        return False, 'Sweet with this name already exists!'
    sweet = Sweet(name=name, price=price, quantity=quantity)
    db.session.add(sweet)
    db.session.commit()
    return True, 'Sweet added successfully!'

def insert_random_sweet():
    existing_names = {s.name for s in Sweet.query.all()}
    available = [s for s in SAMPLE_SWEETS if s["name"] not in existing_names]
    if not available:
        return False, 'All sample sweets are already in the shop!'
    sweet = random.choice(available)
    random_price = round(random.uniform(200, 600), 2)
    random_quantity = random.randint(5, 30)
    db.session.add(Sweet(name=sweet["name"], price=random_price, quantity=random_quantity))
    db.session.commit()
    return True, f'Added {sweet["name"]} to the shop with price {random_price} and quantity {random_quantity}!'
 