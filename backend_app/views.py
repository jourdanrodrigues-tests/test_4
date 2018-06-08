from functools import reduce

from bson import ObjectId
from flask import Blueprint, request

from .db import collection
from .utils import Response

blueprint = Blueprint('views', __name__)


@blueprint.route('/songs/', methods=['GET'])
def songs():
    columns = {
        '_id': 1,
        'title': 1,
        'level': 1,
        'artist': 1,
        'rating': 1,
        'released': 1,
        'difficulty': 1,
    }

    _songs = collection.find({}, columns)

    try:
        page = int(request.args.get('page'))
    except ValueError:
        return Response('Invalid valid for "page" param.').bad_request()
    except TypeError:  # When parameter is not present
        pass
    else:
        if page > 0:
            items_per_page = 10
            _songs = _songs.skip((page - 1) * items_per_page).limit(items_per_page)

    _songs = [
        {'id': str(song.pop('_id')), **song}
        for song in list(_songs)
    ]

    return Response(_songs).json(mongo_dump=False)


@blueprint.route('/songs/search/', methods=['GET'])
def songs_search():
    columns = {
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


@blueprint.route('/songs/avg/difficulty/', methods=['GET'])
def average_difficulty():
    columns = {'_id': 0, 'difficulty': 1}

    level = request.args.get('level')
    where = {}

    if level:
        where['level'] = int(level)

    _songs = list(map(lambda song: song['difficulty'], collection.find(where, columns)))

    average = round(reduce(lambda avg, value: avg + value, _songs) / len(_songs), 2) if _songs else 0

    return Response({'average': average}).json()


@blueprint.route('/songs/avg/rating/<string:song_id>/', methods=['GET'])
def average_rating(song_id):
    columns = {'_id': 0, 'rating': 1}

    where = {'_id': ObjectId(song_id)}

    songs_count = 0
    rating_sum = 0
    rating_max = 0
    rating_min = 0
    for song in collection.find(where, columns):
        # O(1)
        rating = song['rating']
        songs_count += 1
        rating_sum += rating
        rating_max = rating_max if rating_max > rating else rating
        rating_min = rating_min if rating_min < rating else rating

    average = round(rating_sum / songs_count, 2) if songs_count else 0

    return Response({
        'min': rating_min,
        'max': rating_max,
        'average': average,
    }).json()


@blueprint.route('/songs/rating/', methods=['POST'])
def set_rating():
    data = request.json

    where = {'_id': ObjectId(data.get('song_id', ''))}

    try:
        rating = int(data.get('rating'))  # Raises value error
        if 1 > rating or rating > 5:
            raise ValueError()
    except ValueError:
        return Response('Invalid valid for "rating" param.').bad_request()
    except TypeError:
        return Response('Required "rating" not sent').bad_request()

    query_result = collection.update_one(where, {'$set': {'rating': int(rating)}})

    if not query_result.matched_count:
        return Response('Song not found').not_found()

    return Response.no_content()
