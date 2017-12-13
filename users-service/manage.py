from flask.cli import FlaskGroup
from project import app


def create_app(script_info=None):
    return app


cli = FlaskGroup(create_app=create_app)

if __name__ == '__main__':
    cli()
