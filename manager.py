import os
from flask_script import Manager

from apis import bp_api_v1
from app import create_app

app = create_app(object)
app.register_blueprint(bp_api_v1,url_prefix='/api/v1')

app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    
if __name__ == '__main__':
    manager.run()