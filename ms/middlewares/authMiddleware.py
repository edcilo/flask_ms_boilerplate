from typing import Type
from flask import abort, Request
from ms.helpers.jwt import jwt
from .middleware import MiddlewareBase


class AuthMiddleware(MiddlewareBase):
    def handler(self, request: Type[Request]) -> None:
        auth = request.headers.get('Authorization')

        if not auth:
            abort(403)

        valid = jwt.check(auth)

        if not valid:
            abort(403)

        payload = jwt.decode(auth)

        setattr(request, 'auth', payload)
