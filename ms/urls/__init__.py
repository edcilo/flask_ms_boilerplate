from ms import app
from ms.controllers import homeController
from ms.decorators import middleware


@app.route('/')
def app_version():
    return homeController.index()
