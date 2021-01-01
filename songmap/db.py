import sqlite3

class SongDB:
    def __init__(self, db_file):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        finally:
            if self.conn:
                c = self.conn.cursor()
                c.execute('CREATE TABLE IF NOT EXISTS songs (id integer PRIMARY KEY, name text NOT NULL, artist text NOT NULL, album text, date text NOT NULL, url text);')

    def get_songs(self):
        songs = {}
        c = self.conn.cursor()
        c.execute('SELECT * FROM songs')
        rows = c.fetchall()
        for row in rows:
            songs.update({ row[0]: { 'id': row[0], 'name': row[1], 'artist': row[2], 'album': row[3], 'date': row[4], 'url': row[5] } })
        return songs

    def add_song(self, song):
        c = self.conn.cursor()
        c.execute('INSERT INTO songs(name,artist,album,date,url) VALUES(?,?,?,?,?)', song)
        self.conn.commit()
