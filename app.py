from flask import Flask, request, render_template, redirect, session, url_for
from database import db_session, init_db
from models.user import User
import hashlib,secrets

init_db()

app = Flask(__name__)
app.secret_key = secrets.token_hex()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
