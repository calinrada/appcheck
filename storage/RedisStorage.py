import redis
import os
from .AbstractStorage import AbstractStorage


class RedisStorage(AbstractStorage):

    __storage = None

    def __init__(self):
        self.__storage = redis.Redis(
            host=os.environ.get('STORAGE_ENGINE_HOST', 'unknown'),
            port=os.environ.get('STORAGE_ENGINE_HOST', -1),
            db=os.environ.get('STORAGE_ENGINE_DB_NAME', -1)
        )

    def get_storage(self):
        return self.__storage

    def get(self, key):
        return self.__storage.get(key)

    def set(self, key, value):
        return self.__storage.set(key, value)
