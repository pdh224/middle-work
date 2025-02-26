from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db=SQLAlchemy()
def create_app():
    app=Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_DATABASE_URI=
        f"sqlite:///{Path(__file__).parent.parent/'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
     )
    db.init_app(app)
    Migrate(app, db)
    from apps.talk import views as talk_views
    app.register_blueprint(talk_views.talk, url_prefix="/talk")
    return app