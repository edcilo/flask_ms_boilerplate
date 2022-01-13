import os
from dotenv import load_dotenv
from ms import app


load_dotenv()


from .appConfig import app_config
from .dbConfig import db_config


app.config.update(**app_config)
app.config.update(**db_config)
