import json
import os
import re
from typing import Optional

from pymongo import MongoClient
from pymongo.collection import Collection

_DATABASE_URL = os.getenv('DATABASE_URL')

if not _DATABASE_URL:
    raise EnvironmentError('DATABASE_URL is required to be set in the environment')

_DATABASE_NAME = re.search(r'/(\w+)$', _DATABASE_URL).group(1)
_DB_CONNECTION = MongoClient(_DATABASE_URL)[_DATABASE_NAME]


def _get_collection(collection_name: str, get_or_create: bool = False) -> Optional[Collection]:
    collections = _DB_CONNECTION.collection_names()

    if get_or_create or collection_name in collections:
        return _DB_CONNECTION[collection_name]


def _get_songs_collection() -> Collection:
    collection = _get_collection('songs')

    if collection:
        return collection

    collection = _DB_CONNECTION['songs']

    json_path = os.path.join(os.path.dirname(__file__), 'songs.json')

    with open(json_path, 'r') as file:
        _songs = json.loads(file.read())

    collection.insert_many(_songs)

    return collection


songs_collection = _get_songs_collection()
ratings_collection = _get_collection('ratings', get_or_create=True)
