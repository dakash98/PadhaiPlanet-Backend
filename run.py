""" This python file is entrypoint for the application.
It should be run directly only for development environment.
In production this app should be run with gunicorn wsgi server. """

import json
from flask import Flask, Response
from flask_cors import CORS
from flask_restful import Api

from app.config.logger import logger  # Don't remove this, It configures the Flask's inbuilt logger
# from app.config.mysql import db
# from app.config.secret_manager import secrets
# from app.responses import Responses
from app.routes import initialize_routes

# app configurations
application = Flask(__name__)
# application.config.from_object('app.config.mysql.Config')
CORS(application)

# initialize db instance
# db.init_app(application)
# application.config['SQLALCHEMY_ECHO'] = True


# @application.after_request
# def after_request(response):
#     db.session.close()
#     return response


# v1 api configuration
api_routes = Api(application)
initialize_routes(api_routes)

@application.route('/user/health-check')
def health_check():
    """ Root route to check app health """
    
    return Response(
            response=json.dumps({"meta": {"status_code": 1000, 'success': True,
                                "message": "msg"}, "data": {}}, default=str),
            status=200,
            headers={'content-type': 'application/json'}
        )


if __name__ == '__main__':
    application.run(port=8000, debug=True)