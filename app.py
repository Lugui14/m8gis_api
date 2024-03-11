from flask import Flask
from db import db
from blueprints import register_blueprints

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/m8gis'
db.init_app(app)

register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
