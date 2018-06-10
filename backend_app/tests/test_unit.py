from http import HTTPStatus

from ..db import songs_collection
from ..app import flaskApp
from ..views import songs, songs_search, average_difficulty, set_rating


class TestSongs:
    def test_that_it_returns_ok_status(self, mocker):
        mocker.patch.object(songs_collection, 'find', return_value=[{'_id': 'some_id'}])

        with flaskApp.test_request_context():
            response = songs()

        assert HTTPStatus.OK == response.status_code

    def test_that_it_returns_data_from_collection(self, mocker):
        data = [{'_id': 'some_id', 'ratings': []}]
        mocker.patch.object(songs_collection, 'aggregate', return_value=data)

        with flaskApp.test_request_context():
            response = songs()

        assert response.json == [{'id': 'some_id', 'rating': None}]

    def test_when_wrong_page_parameter_is_sent_returns_bad_request_status(self, mocker):
        mocker.patch.object(songs_collection, 'find', return_value=[])

        with flaskApp.test_request_context() as context:
            context.request.args = {'page': '1page'}
            response = songs()

        assert response[1] == HTTPStatus.BAD_REQUEST


class TestSongsSearch:
    def test_when_message_param_is_sent_returns_ok_status(self, mocker):
        mocker.patch.object(songs_collection, 'find', return_value=[{'key': 'value'}])

        with flaskApp.test_request_context() as context:
            context.request.args = {'message': 'text'}

            response = songs_search()

        assert HTTPStatus.OK == response.status_code

    def test_when_message_param_is_sent_returns_data_from_collection(self, mocker):
        data = [{'key': 'value'}]
        mocker.patch.object(songs_collection, 'find', return_value=data)

        with flaskApp.test_request_context() as context:
            context.request.args = {'message': 'text'}

            response = songs_search()

        assert response.json == data

    def test_when_no_message_is_sent_returns_empty_list(self, mocker):
        mocker.patch.object(songs_collection, 'find')

        with flaskApp.test_request_context() as context:
            context.request.args = {}

            response = songs_search()

        assert response.json == []

    def test_when_no_message_is_sent_it_does_not_hit_database(self, mocker):
        mocked_find = mocker.patch.object(songs_collection, 'find')

        with flaskApp.test_request_context() as context:
            context.request.args = {}

            songs_search()

        assert not mocked_find.called

    def test_when_empty_message_is_sent_returns_empty_list(self, mocker):
        mocker.patch.object(songs_collection, 'find')

        with flaskApp.test_request_context() as context:
            context.request.args = {'message': ''}  # Query string as "?message="

            response = songs_search()

        assert response.json == []

    def test_when_empty_message_is_sent_it_does_not_hit_database(self, mocker):
        mocked_find = mocker.patch.object(songs_collection, 'find')

        with flaskApp.test_request_context() as context:
            context.request.args = {'message': ''}  # Query string as "?message="

            songs_search()

        assert not mocked_find.called


class TestAverageDifficulty:
    def test_that_it_returns_ok_status(self, mocker):
        data = [{'difficulty': 3}, {'difficulty': 2}, {'difficulty': 1}]
        # (3 + 2 + 1) / 3 == 2
        mocker.patch.object(songs_collection, 'find', return_value=data)

        with flaskApp.test_request_context() as context:
            context.request.args = {}

            response = average_difficulty()

        assert HTTPStatus.OK == response.status_code

    def test_that_the_calculation_works(self, mocker):
        data = [{'difficulty': 3}, {'difficulty': 2}, {'difficulty': 1}]
        # (3 + 2 + 1) / 3 == 2
        mocker.patch.object(songs_collection, 'find', return_value=data)

        with flaskApp.test_request_context() as context:
            context.request.args = {}

            response = average_difficulty()

        assert response.json['average'] == 2

    def test_when_no_level_is_sent_the_filter_is_empty(self, mocker):
        mocked_find = mocker.patch.object(songs_collection, 'find', return_value=[{'difficulty': 1}])

        with flaskApp.test_request_context() as context:
            context.request.args = {}

            average_difficulty()

        mocked_find.assert_called_once_with({}, {'_id': 0, 'difficulty': 1})

    def test_when_level_is_sent_the_filter_has_it(self, mocker):
        mocked_find = mocker.patch.object(songs_collection, 'find', return_value=[{'difficulty': 1}])

        with flaskApp.test_request_context() as context:
            context.request.args = {'level': '4'}

            average_difficulty()

        mocked_find.assert_called_once_with({'level': 4}, {'_id': 0, 'difficulty': 1})


class TestSetRating:
    def test_when_no_rating_is_sent_returns_bad_request_status(self):
        song_id = '53cb6b9b4f4ddef1ad47f943'

        with flaskApp.test_request_context(json={'song_id': song_id}):
            response = set_rating()

        status_code = response[1]

        assert HTTPStatus.BAD_REQUEST == status_code

    def test_when_rating_less_than_one_is_sent_returns_bad_request_status(self):
        song_id = '53cb6b9b4f4ddef1ad47f943'

        with flaskApp.test_request_context(json={'rating': 0, 'song_id': song_id}):
            response = set_rating()

        status_code = response[1]

        assert HTTPStatus.BAD_REQUEST == status_code

    def test_when_rating_greater_than_five_is_sent_returns_bad_request_status(self):
        song_id = '53cb6b9b4f4ddef1ad47f943'

        with flaskApp.test_request_context(json={'rating': 6, 'song_id': song_id}):
            response = set_rating()

        status_code = response[1]

        assert HTTPStatus.BAD_REQUEST == status_code

    def test_when_rating_is_sent_and_song_does_not_exist_returns_not_found_status(self, mocker):
        song_id = '53cb6b9b4f4ddef1ad47f943'

        mocker.patch.object(songs_collection, 'find', return_value=False)

        with flaskApp.test_request_context(json={'rating': 4, 'song_id': song_id}):
            response = set_rating()

        status_code = response[1]

        assert HTTPStatus.NOT_FOUND == status_code

    def test_when_rating_is_sent_and_song_id_exists_returns_ok_with_no_content_status(self, mocker):
        song_id = '53cb6b9b4f4ddef1ad47f943'

        with flaskApp.test_request_context(json={'rating': 4, 'song_id': song_id}):
            response = set_rating()

        status_code = response[1]

        assert HTTPStatus.NO_CONTENT == status_code
