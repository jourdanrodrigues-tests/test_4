import json
import os

from bson.json_util import dumps as mongo_dumps
from flask import jsonify
from flask.wrappers import Response

COLLECTION = 'songs'


def get_collection(db_conn):
    collections = db_conn.collection_names()
    if COLLECTION in collections:
        return db_conn[COLLECTION]

    collection = db_conn[COLLECTION]

    json_path = os.path.join(os.path.dirname(__file__), 'songs.json')

    with open(json_path, 'r') as file:
        _songs = json.loads(file.read())

    collection.insert_many(_songs)

    return collection


def json_response(data: dict or list) -> Response:
    # https://stackoverflow.com/a/27024423/4694834
    return jsonify(json.loads(mongo_dumps(data)))
