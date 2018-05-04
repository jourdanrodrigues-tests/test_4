import json
import os
import re

from pymongo import MongoClient


def _get_collection():
    database_url = os.getenv('DATABASE_URL')

    if not database_url:
        raise EnvironmentError('DATABASE_URL is required to be set in the environment')

    connection = MongoClient(database_url)

    collection_name = 'songs'
    database_name = re.search(r'/(\w+)$', database_url).group(1)
    db_conn = connection[database_name]

    collections = db_conn.collection_names()
    if collection_name in collections:
        return db_conn[collection_name]

    _collection = db_conn[collection_name]

    json_path = os.path.join(os.path.dirname(__file__), 'songs.json')

    with open(json_path, 'r') as file:
        _songs = json.loads(file.read())

    _collection.insert_many(_songs)

    return _collection


collection = _get_collection()
