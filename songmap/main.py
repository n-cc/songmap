import sqlite3
import yaml
from flask import Flask
from flask import render_template
from db import SongDB

with open('config.yml') as config_file:
    config = yaml.safe_load(config_file)

app = Flask(__name__)

@app.route('/')
def home():
    db = SongDB(config['db_file'])
    songs=db.get_songs()
    return render_template('home.html', songs=songs, config=config)

@app.route('/songs/<song_id>')
def songs(song_id):
    db = SongDB(config['db_file'])
    print(song_id)
    id = int(song_id.strip('.html'))
    songs=db.get_songs()
    if not songs[id]:
        abort(404)
    else:
        return render_template('song.html', song=songs[id], config=config)
