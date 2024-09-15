from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mariadb://admin:Classified17@localhost/gamelib"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
import routes

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
