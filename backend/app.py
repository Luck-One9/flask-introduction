import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = bool(os.getenv('FLASK_DEBUG')) or False
CORS(app, origins=[os.getenv('DEV_FRONTEND_URL') or "http://localhost:3000"])

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/api/name")
def api_name():
    return "Flask"