from waitress import serve
from flask import Flask
from flask_cors import CORS

from api.safe_bump_blueprint import safe_bump_blueprint

app = Flask(__name__)
app.register_blueprint(safe_bump_blueprint)

CORS(app)

if __name__ == "__main__":
    app.run()

