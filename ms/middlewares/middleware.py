from typing import Type
from flask import Request
from abc import ABC, abstractmethod


class MiddlewareBase(ABC):
    @abstractmethod
    def handler(self, request: Type[Request]) -> None:
        pass
