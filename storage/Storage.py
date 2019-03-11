from .RedisStorage import RedisStorage
from exception import StorageException


class Storage:
    # Storage instance
    __storage = None

    # A list with valid storage engines
    __valid_engine = [
        'redis'
    ]

    def __init__(self, name):
        if name not in self.__valid_engine:
            raise StorageException('Invalid storage engine: %s' % name)

        if name == 'redis':
            storage = RedisStorage()
            self.__storage = storage.get_storage()

    def get_storage(self):
        return self.__storage
