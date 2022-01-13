import jwt
from typing import Any, Union
from ms import app
from .time import epoch_now


class JwtHelper():
    def __init__(self, key: str = None,
                 algorithms: str = 'HS256',
                 token_lifetime: int = 43200,
                 refresh_token_lifetime: int = 86400,
                 token_type: str = 'Bearer') -> None:
        self.key = key
        self.algorithms = algorithms
        self.token_type = token_type
        self.token_lifetime = token_lifetime
        self.refresh_token_lifetime = refresh_token_lifetime

    def encode(self, payload: dict, lifetime: int) -> str:
        payload['exp'] = epoch_now() + lifetime
        encoded = jwt.encode(payload, self.key, algorithm=self.algorithms)
        return encoded

    def decode(self, token: str) -> dict[str, Any]:
        token = token.replace(self.token_type, '').strip()
        payload = jwt.decode(token, self.key, algorithms=self.algorithms)
        return payload

    def get_tokens(self, payload: dict[str, Any]) -> dict[str, str]:
        token = self.encode(payload, self.token_lifetime)
        refresh_token = self.encode(payload, self.refresh_token_lifetime)
        return {
            'token': token,
            'refresh_token': refresh_token,
        }

    def check(self, token: str) -> bool:
        try:
            payload = self.decode(token)
            return epoch_now() <= payload['exp']
        except (jwt.InvalidSignatureError,
                jwt.DecodeError,
                jwt.ExpiredSignatureError,
                KeyError):
            return False


jwt = JwtHelper(key=app.config.get('SECRET_KEY'))
