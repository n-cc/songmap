import sqlite3
import argparse
import yaml
from songmap.db import SongDB

with open('config.yml') as config_file:
    config = yaml.safe_load(config_file)

db = SongDB(config['db_file'])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", help="add song to database", action="store_true")
    parser.add_argument("name", help="song name")
    parser.add_argument("artist", help="artist")
    parser.add_argument("album", help="album")
    parser.add_argument("date", help="date")
    parser.add_argument("url", help="url")

    args = parser.parse_args()

    if args.add:
        db.add_song((args.name, args.artist, args.album, args.date, args.url))

if __name__ == '__main__':
    main()
