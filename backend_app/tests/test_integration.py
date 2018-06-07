from threading import Thread

from ..app import flaskApp

PORT = 5123


class TestSongs:
    @classmethod
    def setup_class(cls):
        Thread(target=flaskApp.run, kwargs={'port': PORT}).start()

    def test_that_it_returns_right_amount_of_items_on_pagination(self):
        client = flaskApp.test_client()
        response = client.get('/songs/?page=1'.format(PORT))
        assert 10 == len(response.json)
