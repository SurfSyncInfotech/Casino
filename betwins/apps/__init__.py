import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module


db = SQLAlchemy()

def register_extensions(app):
    db.init_app(app)

apps = ('pages',)

def register_blueprints(app):
    for module_name in apps:
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app):

    @app.before_request
    def initialize_database():
        try:
            db.create_all()
        except Exception as e:

            print('> Error: DBMS Exception: ' + str(e) )

            # fallback to SQLite
            basedir = os.path.abspath(os.path.dirname(__file__))
            app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')

            print('> Fallback to SQLite ')
            db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def register_template_globals(app):
    from apps import content

    assets = app.config.get('ASSETS_ROOT', '/static')

    def img(path):
        return '{}/images/{}'.format(assets, path)

    app.jinja_env.globals.update(
        site=content.SITE,
        nav=content.NAV,
        content=content,
        img=img,
    )


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_template_globals(app)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    return app
