from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    base_dir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(
        __name__,
        static_folder=os.path.join(base_dir, '..', 'static'),
        template_folder=os.path.join(base_dir, '..', 'templates'),
    )
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.main_routes import main_bp
    app.register_blueprint(main_bp)

    return app