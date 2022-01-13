from .serializer import Serializer


class HomeSerializer(Serializer):
    response = {
        'name': str,
        'version': str,
    }
