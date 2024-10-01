from abc import ABC, abstractmethod


class Page(ABC):

    def serve(self):
        pass