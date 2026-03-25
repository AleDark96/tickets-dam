from flask import Flask
from routes import register_routes
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
register_routes(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # crea las tablas
    app.run(debug=True)