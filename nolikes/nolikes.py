# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object(__name__)  # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'nolikes.db'),
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test.db',
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('NOLIKES_SETTINGS', silent=True)


db = SQLAlchemy(app)
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(80), unique=True, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    algo = db.Column(db.String(80), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    caption = db.Column(db.String(480))
    caption_im2txt = db.Column(db.String(480))

    def __init__(self, uuid, url, algo, caption, caption_im2txt, number):
        self.uuid = uuid
        self.url = url
        self.caption = caption
        self.caption_im2txt = caption_im2txt
        self.number = number
        self.algo = algo

    def __repr__(self):
        return '<Image uuid={} url={} caption={} caption_im2txt={} algo={} number={}>'.format(self.uuid, self.url, self.caption, self.caption_im2txt, self.algo, self.number)

# @app.route('/')
# def show_image():
    # db = get_db()
    # cur = db.execute('select title, text from entries order by id desc')
    # entries = cur.fetchall()
    # return render_template('show_entries.html', entries=entries)
