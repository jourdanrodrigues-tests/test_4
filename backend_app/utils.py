import json
from http import HTTPStatus

from bson.json_util import dumps as mongo_dumps
from flask import jsonify
from flask.wrappers import Response as FlaskResponse


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
