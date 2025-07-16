from flask import Flask
from codes.models import db, Sweet
from codes.routes import create_routes, read_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sweets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'

db.init_app(app)
app.register_blueprint(create_routes)
app.register_blueprint(read_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)