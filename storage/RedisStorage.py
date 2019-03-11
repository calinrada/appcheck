import redis
import os
from .AbstractStorage import AbstractStorage


class RedisStorage(AbstractStorage):

    __storage = None

    def __init__(self):

        self.__storage = redis.Redis(
            host=os.environ.get('STORAGE_ENGINE_HOST', 'unknown'),
            port=os.environ.get('STORAGE_ENGINE_PORT', -1),
            db=os.environ.get('STORAGE_ENGINE_DB_NAME', -1)
        )

    def get_storage(self):
        return self

    def get(self, key):
        return self.__storage.smembers(key)

    def set(self, key, value):
        return self.__storage.sadd(key, value)

    def exists(self, **kwargs):
        key = kwargs.pop('key')
        value = kwargs.pop('value')
        return self.__storage.sismember(key, value)
