from flask import Flask

def create_app():
    app = Flask(__name__)

    from target.home.routes import home
    app.register_blueprint(home)
    
    return app