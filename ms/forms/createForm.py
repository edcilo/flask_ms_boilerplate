from typing import Callable, Type

from flask import Request
from .form import FormRequest


class CreateForm(FormRequest):
    def rules(self, request: Type[Request]) -> dict[str, Callable]:
        return {
        }
