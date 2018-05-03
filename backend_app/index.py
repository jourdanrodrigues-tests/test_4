import os
import re

from flask import Flask
from flask_cors import cross_origin
from pymongo import MongoClient

from .utils import get_collection, json_response

DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    raise EnvironmentError('DATABASE_URL is required to be set in the environment')

connection = MongoClient(DATABASE_URL)


DATABASE_NAME = re.search(r'/(\w+)$', DATABASE_URL).group(1)
songs_collection = get_collection(connection[DATABASE_NAME])

app = Flask(__name__)


@app.route('/api/songs/')
@cross_origin()
def songs():
    columns = {
        '_id': 0,
        'title': 1,
        'level': 1,
        'artist': 1,
        'rating': 1,
        'released': 1,
        'difficulty': 1,
    }
    _songs = list(songs_collection.find({}, columns))
    return json_response(_songs)
