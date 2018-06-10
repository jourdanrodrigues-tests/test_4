import json
from functools import reduce
from http import HTTPStatus
from typing import List, Union, Dict, Any

from bson.json_util import dumps as mongo_dumps
from flask import jsonify
from flask.wrappers import Response as FlaskResponse
from pymongo.cursor import Cursor


class Response:
    def __init__(self, data: Union[str, Dict[str, Any], List[Any], Cursor]):
        self.data = data

    def json(self, error=False) -> FlaskResponse:
        # https://stackoverflow.com/a/27024423/4694834
        data = json.loads(mongo_dumps(self.data)) if isinstance(self.data, Cursor) else self.data
        data = {'message': data} if error else data
        return jsonify(data)

    def bad_request(self) -> tuple:
        return self.json(error=True), HTTPStatus.BAD_REQUEST

    def not_found(self) -> tuple:
        return self.json(error=True), HTTPStatus.NOT_FOUND

    @staticmethod
    def no_content() -> tuple:
        return '', HTTPStatus.NO_CONTENT


def get_average(a_list: List[Union[int, float]], key: str = None) -> float:
    total_items = len(a_list)
    total_value = reduce(lambda total, value: total + (value[key] if key else value), a_list, 0)
    return round(total_value / total_items, 2)
