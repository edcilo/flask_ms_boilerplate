from ms import app
from ms.controllers import homeController


@app.route('/')
def app_version():
    return homeController.index()
