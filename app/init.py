from flask import Flask
from app.api.routes import api_bp
from app.auth.auth import jwt

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    
    jwt.init_app(app)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
