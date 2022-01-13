from flask import request
from functools import wraps


def middleware(middlewareClass):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            middleware = middlewareClass()
            middleware.handler(request)

            return f(*args, **kwargs)
        return wrapper
    return decorator
