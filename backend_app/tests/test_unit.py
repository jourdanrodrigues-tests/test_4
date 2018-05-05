from http import HTTPStatus

from ..db import collection
from ..app import flaskApp
from ..views import songs, songs_search, average_difficulty, set_rating


class TestSongs:
    def test_that_it_returns_ok_status(self, mocker):
        mocker.patch.object(collection, 'find', return_value=[{'key': 'value'}])

        with flaskApp.app_context():
            response = songs()

        assert response.status_code == HTTPStatus.OK

    def test_that_it_returns_data_from_collection(self, mocker):
        data = [{'key': 'value'}]
        mocker.patch.object(collection, 'find', return_value=data)

        with flaskApp.app_context():
            response = songs()

        assert response.json == data


class TestSongsSearch:
    def test_when_message_param_is_sent_returns_ok_status(self, mocker):
        mocker.patch.object(collection, 'find', return_value=[{'key': 'value'}])

        with flaskApp.test_request_context() as context:
            context.request.args = {'message': 'text'}

            response = songs_search()

        assert response.status_code == HTTPStatus.OK

    def test_when_message_param_is_sent_returns_data_from_collection(self, mocker):
        data = [{'key': 'value'}]
        mocker.patch.object(collection, 'find', return_value=data)

        with flaskApp.test_request_context() as context:
            context.request.args = {'message': 'text'}

            response = songs_search()

        assert response.json == data

    def test_when_no_message_is_sent_returns_empty_list(self, mocker):
        mocker.patch.object(collection, 'find')

        with flaskApp.test_request_context() as context:
            context.request.args = {}

            response = songs_search()

        assert response.json == []

    def test_when_no_message_is_sent_it_does_not_hit_database(self, mocker):
        mocked_find = mocker.patch.object(collection, 'find')

        with flaskApp.test_request_context() as context:
            context.request.args = {}

            songs_search()

        assert not mocked_find.called

    def test_when_empty_message_is_sent_returns_empty_list(self, mocker):
        mocker.patch.object(collection, 'find')

        with flaskApp.test_request_context() as context:
            context.request.args = {'message': ''}  # Query string as "?message="

            response = songs_search()

        assert response.json == []

    def test_when_empty_message_is_sent_it_does_not_hit_database(self, mocker):
        mocked_find = mocker.patch.object(collection, 'find')

        with flaskApp.test_request_context() as context:
            context.request.args = {'message': ''}  # Query string as "?message="

            songs_search()

        assert not mocked_find.called


class TestAverageDifficulty:
    def test_that_it_returns_ok_status(self, mocker):
        data = [{'difficulty': 3}, {'difficulty': 2}, {'difficulty': 1}]
        # (3 + 2 + 1) / 3 == 2
        mocker.patch.object(collection, 'find', return_value=data)

        with flaskApp.test_request_context() as context:
            context.request.args = {}

            response = average_difficulty()

        assert response.status_code == HTTPStatus.OK

    def test_that_the_calculation_works(self, mocker):
        data = [{'difficulty': 3}, {'difficulty': 2}, {'difficulty': 1}]
        # (3 + 2 + 1) / 3 == 2
        mocker.patch.object(collection, 'find', return_value=data)

        with flaskApp.test_request_context() as context:
            context.request.args = {}

            response = average_difficulty()

        assert response.json['average'] == 2

    def test_when_no_level_is_sent_the_filter_is_empty(self, mocker):
        mocked_find = mocker.patch.object(collection, 'find', return_value=[{'difficulty': 1}])

        with flaskApp.test_request_context() as context:
            context.request.args = {}

            average_difficulty()

        mocked_find.assert_called_once_with({}, {'_id': 0, 'difficulty': 1})

    def test_when_level_is_sent_the_filter_has_it(self, mocker):
        mocked_find = mocker.patch.object(collection, 'find', return_value=[{'difficulty': 1}])

        with flaskApp.test_request_context() as context:
            context.request.args = {'level': '4'}

            average_difficulty()

        mocked_find.assert_called_once_with({'level': 4}, {'_id': 0, 'difficulty': 1})


class TestSetRating:
    def test_when_no_rating_is_sent_returns_bad_request_status(self):
        song_id = '53cb6b9b4f4ddef1ad47f943'

        with flaskApp.test_request_context(json={}):
            response = set_rating(song_id)

        status_code = response[1]

        assert status_code == HTTPStatus.BAD_REQUEST

    def test_when_rating_is_sent_and_song_does_not_exist_returns_not_found_status(self, mocker):
        song_id = '53cb6b9b4f4ddef1ad47f943'

        class UpdateResultMock:
            matched_count = 0

        mocker.patch.object(collection, 'update_one', return_value=UpdateResultMock())

        with flaskApp.test_request_context(json={'rating': 4}):
            response = set_rating(song_id)

        status_code = response[1]

        assert status_code == HTTPStatus.NOT_FOUND

    def test_when_rating_is_sent_and_song_id_exists_returns_ok_with_no_content_status(self, mocker):
        song_id = '53cb6b9b4f4ddef1ad47f943'

        class UpdateResultMock:
            matched_count = 1

        mocker.patch.object(collection, 'update_one', return_value=UpdateResultMock())

        with flaskApp.test_request_context(json={'rating': 4}):
            response = set_rating(song_id)

        status_code = response[1]

        assert status_code == HTTPStatus.NO_CONTENT
