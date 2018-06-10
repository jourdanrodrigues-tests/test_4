import json
from http import HTTPStatus
from typing import List, Union, Dict, Any

from bson.json_util import dumps as mongo_dumps
from flask import jsonify
from flask.wrappers import Response as FlaskResponse


class Response:
    def __init__(self, data: Union[str, Dict[str, Any], List[Any]]):
        self.data = data

    def json(self, error=False, mongo_dump=True) -> FlaskResponse:
        data = {'message': self.data} if error else self.data

        # https://stackoverflow.com/a/27024423/4694834
        if mongo_dump:
            data = json.loads(mongo_dumps(data))

        return jsonify(data)

    def bad_request(self) -> tuple:
        return self.json(error=True), HTTPStatus.BAD_REQUEST

    def not_found(self) -> tuple:
        return self.json(error=True), HTTPStatus.NOT_FOUND

    @staticmethod
    def no_content() -> tuple:
        return '', HTTPStatus.NO_CONTENT
