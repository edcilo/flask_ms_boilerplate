from typing import Callable
from flaskFormRequest import FormRequest


class CreateForm(FormRequest):
    def rules(self) -> dict[str, Callable]:
        return {
        }
