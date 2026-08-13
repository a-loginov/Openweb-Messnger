import config
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
















if __name__ == '__main__':
    app.run(debug=True, port=9080, host='0.0.0.0')