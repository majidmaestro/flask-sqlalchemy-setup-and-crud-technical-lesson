from flask import Flask
from flask_migrate import Migrate

from models import db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


# Makes `db` and `Pet` available automatically inside `flask shell`
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Pet': Pet}


if __name__ == '__main__':
    app.run(port=5555, debug=True)
