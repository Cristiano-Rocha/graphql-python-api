from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:postgres@localhost:5432/blog-graphql-flask"
app.config["SQLALCHEMy_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "Hello World"
