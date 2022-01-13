import abc
from typing import Any, Callable, Type, Union
from flask_wtf import FlaskForm
from flask import Request


def strip_filter(value: Union[str, None]) -> Union[str, None]:
    if value is not None and hasattr(value, 'strip'):
        return value.strip()
    return value


class BaseForm(FlaskForm):
    class Meta:
        def bind_field(self, form, unbound_field, options):
            filters = unbound_field.kwargs.get('filters', [])
            filters.append(strip_filter)
            return unbound_field.bind(form=form, filters=filters, **options)


class FormRequest():
    def __init__(self, data: dict[str, Any], request: Type[Request]) -> None:
        self.request_data = data
        self.request = request
        self.attrs = list()
        self.form = self.initialize()

    @property
    def errors(self) -> Union[dict[str, Any], None]:
        return None if self.form is None else self.form.errors

    @property
    def data(self) -> dict[str, Any]:
        data = dict()
        for attr in self.attrs:
            data[attr] = getattr(self.form, attr).data
        return data

    def initialize(self) -> BaseForm:
        class Form(BaseForm):
            pass

        rules = self.rules(self.request)

        for attr, rule in rules.items():
            setattr(Form, attr, rule)
            self.attrs.append(attr)

        return Form(data=self.request_data, meta={'csrf': False})

    def validate(self) -> None:
        return self.form.validate()

    @abc.abstractmethod
    def rules(self, request: Type[Request]) -> dict[str, Callable]:
        pass
