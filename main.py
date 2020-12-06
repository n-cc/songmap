import sqlite3
import yaml
from flask import Flask
from flask import render_template

app = Flask(__name__)
db_file = 'db.sqlite3'

with open('config.yml') as config_file:
    config = yaml.safe_load(config_file)

@app.route('/')
def home():
    songs=get_songs()
    return render_template('home.html', songs=songs, config=config)

@app.route('/songs/<song_id>')
def songs(song_id):
    id = int(song_id.strip('.html'))
    songs=get_songs()
    if not songs[id]:
        abort(404)
    else:
        return render_template('song.html', song=songs[id], config=config)

def init_db():
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        if conn:
            c = conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS songs (id integer PRIMARY KEY, name text NOT NULL, artist text NOT NULL, album text, date text NOT NULL, url text);')
            return conn

def get_songs():
    songs = {}
    conn = init_db()
    c = conn.cursor()
    c.execute('SELECT * FROM songs')
    rows = c.fetchall()
    for row in rows:
        songs.update({ row[0]: { 'id': row[0], 'name': row[1], 'artist': row[2], 'album': row[3], 'date': row[4], 'url': row[5] } })
    return songs

def add_song(song):
    conn = init_db()
    c = conn.cursor()
    c.execute('INSERT INTO songs(name,artist,album,date,url) VALUES(?,?,?,?,?)', song)
    conn.commit()
