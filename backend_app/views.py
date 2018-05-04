from functools import reduce

from bson import ObjectId
from flask import Blueprint, request

from .utils import get_collection, Response

blueprint = Blueprint('views', __name__)

collection = get_collection()


@blueprint.route('/api/songs/', methods=['GET'])
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

    _songs = collection.find({}, columns)
    return Response(_songs).json()


@blueprint.route('/api/songs/search/', methods=['GET'])
def songs_search():
    columns = {
        '_id': 1,  # More explicit
        'title': 1,
        'level': 1,
        'artist': 1,
        'rating': 1,
        'released': 1,
        'difficulty': 1,
    }
    # Wondering why this is named "message" in the requirements
    to_search = request.args.get('message')

    if not to_search:
        return Response([]).json()  # Saving a query

    search_query = {'$regex': r'.*{}.*'.format(to_search)}
    where = {
        '$or': [
            {'title': search_query},
            {'artist': search_query},
        ]
    }

    _songs = collection.find(where, columns)

    return Response(_songs).json()


@blueprint.route('/api/songs/avg/difficulty/', methods=['GET'])
def average_difficulty():
    columns = {'_id': 0, 'difficulty': 1}

    level = request.args.get('level')
    where = {}

    if level:
        where['level'] = int(level)

    _songs = list(map(lambda song: song['difficulty'], collection.find(where, columns)))

    average = round(reduce(lambda avg, value: avg + value, _songs) / len(_songs), 2) if _songs else 0

    return Response({'average': average}).json()


@blueprint.route('/api/songs/rating/<int:song_id>/', methods=['POST'])
def set_rating(song_id):
    where = {'_id': ObjectId(str(song_id))}
    rating = request.json.get('rating')

    if not rating:
        return Response('Required "rating" not sent').bad_request()

    query_result = collection.update_one(where, {'$set': {'rating': rating}})

    if not query_result.matched_count:
        return Response('Song not found').not_found()

    return Response.no_content()
