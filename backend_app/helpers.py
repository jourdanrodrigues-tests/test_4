from pymongo.cursor import Cursor

from .db import songs_collection


class SongsAggregator:
    cursor = None
    __skip = 0
    __limit = 0
    __where = {}
    __lookup = {}
    __columns = {}
    __first = False

    def __init__(self, cursor: Cursor = None):
        self.cursor = cursor

    def evaluate(self) -> Cursor:
        if self.__lookup:
            return self.__aggregate()

        finder = songs_collection.find_one if self.__first else songs_collection.find

        cursor = finder(self.__where, self.__columns)

        if self.__skip:
            cursor = cursor.skip(self.__skip)
        if self.__limit:
            cursor = cursor.limit(self.__limit)

        return cursor

    def __aggregate(self):
        cursor = self.cursor or songs_collection
        args = []

        if self.__skip:
            args.append({'$skip': self.__skip})
        if self.__limit:
            args.append({'$limit': self.__limit})
        if self.__where:
            args.append({'$match': self.__where})
        if self.__lookup:
            args.append({'$lookup': self.__lookup})
        if self.__columns:
            args.append({'$project': self.__columns})

        result = cursor.aggregate(args)
        if self.__first:
            for first_result in result:
                return first_result
        else:
            return result

    def limit(self, number: int) -> 'SongsAggregator':
        self.__limit = number
        return self

    def first(self) -> 'SongsAggregator':
        self.__first = True
        return self

    def skip(self, number: int) -> 'SongsAggregator':
        self.__skip = number
        return self

    def filter(self, **where) -> 'SongsAggregator':
        self.__where.update(where)
        return self

    def select_fields(self, **fields) -> 'SongsAggregator':
        self.__columns.update(fields)
        return self

    def join_ratings(self) -> 'SongsAggregator':
        self.__lookup = {
            'from': 'ratings',
            'localField': '_id',
            'foreignField': 'song_id',
            'as': 'ratings',
        }
        return self
