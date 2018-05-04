import json
import os
import re
from http import HTTPStatus

from bson.json_util import dumps as mongo_dumps
from flask import jsonify
from flask.wrappers import Response as FlaskResponse
from pymongo import MongoClient

DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    raise EnvironmentError('DATABASE_URL is required to be set in the environment')

connection = MongoClient(DATABASE_URL)

COLLECTION = 'songs'
DATABASE_NAME = re.search(r'/(\w+)$', DATABASE_URL).group(1)
db_conn = connection[DATABASE_NAME]


def get_collection():
    collections = db_conn.collection_names()
    if COLLECTION in collections:
        return db_conn[COLLECTION]

    collection = db_conn[COLLECTION]

    json_path = os.path.join(os.path.dirname(__file__), 'songs.json')

    with open(json_path, 'r') as file:
        _songs = json.loads(file.read())

    collection.insert_many(_songs)

    return collection


class Response:
    def __init__(self, data: str or dict or list):
        self.data = data

    def json(self, error=False) -> FlaskResponse:
        data = {'message': self.data} if error else self.data
        # https://stackoverflow.com/a/27024423/4694834
        return jsonify(json.loads(mongo_dumps(data)))

    def bad_request(self) -> tuple:
        return self.json(), HTTPStatus.BAD_REQUEST

    def not_found(self) -> tuple:
        return self.json(), HTTPStatus.NOT_FOUND

    @staticmethod
    def no_content() -> tuple:
        return '', HTTPStatus.NO_CONTENT
