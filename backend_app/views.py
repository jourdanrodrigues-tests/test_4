from bson import ObjectId
from flask import Blueprint, request

from .db import songs_collection, ratings_collection
from .helpers import SongsAggregator
from .utils import Response, get_average

blueprint = Blueprint('views', __name__)


@blueprint.route('/songs/', methods=['GET'])
def songs():
    aggregator = SongsAggregator().select_fields(
        _id=1,
        title=1,
        level=1,
        artist=1,
        ratings=1,
        released=1,
        difficulty=1,
    ).join_ratings()

    try:
        page = int(request.args.get('page'))
    except ValueError:
        return Response('Invalid valid for "page" param.').bad_request()
    except TypeError:  # When parameter is not present
        pass
    else:
        if page > 0:
            items_per_page = 10
            aggregator.skip((page - 1) * items_per_page).limit(items_per_page)

    data = []
    for song in aggregator.evaluate():
        ratings = song.pop('ratings', None)
        data.append({
            'id': str(song.pop('_id')),
            'rating': get_average(ratings) if ratings else None,
            **song,
        })

    return Response(data).json()


@blueprint.route('/songs/search/', methods=['GET'])
def songs_search():
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
    data = SongsAggregator().filter(**where).select_fields(
        title=1,
        level=1,
        artist=1,
        ratings=1,
        released=1,
        difficulty=1,
    ).evaluate()

    return Response(data).json()


@blueprint.route('/songs/avg/difficulty/', methods=['GET'])
def average_difficulty():
    columns = {'_id': 0, 'difficulty': 1}

    level = request.args.get('level')
    where = {}

    if level:
        where['level'] = int(level)

    _songs = list(map(lambda song: song['difficulty'], songs_collection.find(where, columns)))

    average = get_average(_songs) if _songs else 0

    return Response({'average': average}).json()


@blueprint.route('/songs/avg/rating/<string:song_id>/', methods=['GET'])
def average_rating(song_id):

    ratings_count = 0
    rating_sum = 0
    rating_max = 0
    rating_min = 0

    aggregator = SongsAggregator().join_ratings()

    song = aggregator.filter(_id=ObjectId(song_id)).select_fields(_id=0, ratings=1).first().evaluate()

    for rating in song['ratings']:
        # O(1)
        ratings_count += 1
        rating_sum += rating
        rating_max = rating_max if rating_max > rating else rating
        rating_min = rating_min if rating_min < rating else rating

    average = round(rating_sum / ratings_count, 2) if ratings_count else 0

    return Response({
        'min': rating_min,
        'max': rating_max,
        'average': average,
    }).json()


@blueprint.route('/songs/rating/', methods=['POST'])
def set_rating():
    data = request.json

    song_id = ObjectId(data.get('song_id', ''))
    if not songs_collection.find({'_id': {'$exists': True, '$in': [song_id]}}):
        return Response('Song not found').not_found()

    try:
        rating = int(data.get('rating'))  # Raises value error
        if 1 > rating or rating > 5:
            raise ValueError()
    except ValueError:
        return Response('Invalid valid for "rating" param.').bad_request()
    except TypeError:
        return Response('Required "rating" not sent').bad_request()

    ratings_collection.insert({
        'value': rating,
        'song_id': song_id,
    })

    return Response.no_content()
