from codes.models import db, Sweet
import random

SAMPLE_SWEETS = [
    {"name": "Dango (団子)", "price": 300},
    {"name": "Castella (カステラ)", "price": 400},
    {"name": "Matcha Mochi (抹茶餅)", "price": 350},
    {"name": "Ichigo Daifuku (いちご大福)", "price": 450},
    {"name": "Dorayaki (どら焼き)", "price": 320},
    {"name": "Taiyaki (たい焼き)", "price": 380},
    {"name": "Kakigōri (かき氷)", "price": 250},
    {"name": "Yokan (羊羹)", "price": 300},
    {"name": "Purin (プリン)", "price": 280},
    {"name": "Manju (饅頭)", "price": 270},
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
 