from threading import Thread

from ..db import songs_collection
from ..app import flaskApp

Thread(target=flaskApp.run, kwargs={'port': 5123}).start()


class TestSongs:
    def test_that_it_returns_right_amount_of_items_on_pagination(self):
        client = flaskApp.test_client()
        response = client.get('/songs/?page=1')

        assert 10 == len(response.json)


class TestAverageRating:
    def test_that_it_returns_average_min_and_max(self):
        song = songs_collection.find_one({}, {'_id': 1})
        client = flaskApp.test_client()
        response = client.get('/songs/avg/rating/{}/'.format(song['_id']))

        assert 'min' in response.json
        assert 'max' in response.json
        assert 'average' in response.json
