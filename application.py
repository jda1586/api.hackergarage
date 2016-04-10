#!/usr/bin/python
# coding=utf-8

from flask.ext.api import FlaskAPI
from conf.config import LocalConfig
from modules.authentication import authentication, auth
from modules.authors import authors
from modules import mongo

application = FlaskAPI(__name__)
application.config.from_object(LocalConfig)

application.register_blueprint(authentication, url_prefix='/authentication')
application.register_blueprint(authors, url_prefix='/authors')

mongo.init_app(application)


@application.route('/')
@auth.login_required
def index_testing():
    return {'status': 'OK'}


if __name__ == "__main__":
    application.run(
        host=application.config['HOST'],
        debug=application.config['DEBUG'],
        port=application.config['PORT'],
    )
