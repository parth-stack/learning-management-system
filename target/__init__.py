from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db.init_app(app)
    app.config['SECRET_KEY'] = 'zR0pu1dXbAOhlC-sRX5SzQ'
    bcrypt.init_app(app)

    from target.home.routes import home
    app.register_blueprint(home)
    from target.users.routes import users
    app.register_blueprint(users)
    from target.dash.routes import dash
    app.register_blueprint(dash)
    from target.admin.routes import admin
    app.register_blueprint(admin)
    from target.errors.handlers import errors
    app.register_blueprint(errors)
    
    with app.app_context():
        db.create_all()

    return app