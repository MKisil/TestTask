from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flasgger import Swagger

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name='default'):
    app = Flask(__name__)

    from app.config import config
    app.config.from_object(config[config_name])

    db.init_app(app)
    ma.init_app(app)

    swagger = Swagger(app, template={
        "info": {
            "title": "Test Task",
            "description": "REST API for managing users",
            "version": "1.0.0"
        },
        "tags": [
            {
                "name": "Users",
                "description": "API for users"
            }
        ]
    })

    from app.users.routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/users')

    with app.app_context():
        db.create_all()

    return app
