from abc import ABC, abstractmethod


class AbstractStorage(ABC):

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass
