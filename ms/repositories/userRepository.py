from ms.models import User
from .repository import Repository


class UserRepository(Repository):
    def get_model(self) -> User:
        return User
