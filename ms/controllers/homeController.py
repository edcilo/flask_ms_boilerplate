from flask import jsonify
from ms import app


class HomeController():
    def index(self):
        return jsonify({
            'data': {
                'name': app.config.get('APP_NAME'),
                'version': app.config.get('APP_VERSION'),
            },
            'code': 200
        }), 200
