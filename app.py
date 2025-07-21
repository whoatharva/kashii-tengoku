from flask import Flask
from codes.models import db, Sweet
from codes.routes import create_routes, read_routes, update_routes, delete_routes
from codes.services import SAMPLE_SWEETS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sweets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'

db.init_app(app)
app.register_blueprint(create_routes)
app.register_blueprint(read_routes)
app.register_blueprint(update_routes)
app.register_blueprint(delete_routes)

@app.cli.command("init-db")
def init_db():
    with app.app_context():
        db.create_all()
        for s in SAMPLE_SWEETS:
            if not Sweet.query.filter_by(name=s['name']).first():
                db.session.add(Sweet(name=s['name'], price=s['price'], quantity=10))
        db.session.commit()
    print("Database initialized!")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=False)