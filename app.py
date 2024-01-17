import os
from models import db
from config import LocalDevelopmentConfig
from flask import Flask


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(LocalDevelopmentConfig)
    print("Local Developent Executed")
    db.init_app(app)
    print("App Initialized")
    return app

app = create_app()
#api = Api(app)
app.app_context().push()

#db.drop_all()
db.create_all()


print("app working good")

from routes import *

if __name__ == '__main__':
  # Run the Flask app
  app.run(debug = True)
