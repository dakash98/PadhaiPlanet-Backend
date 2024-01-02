from flask_restful import Api
from app.views.v1 import QuestionPapers, SignUp, InputConfig, Login, Logout


def initialize_routes(api: Api):
    """ Initialized all the v1 routes related to User. """

    api.prefix = '/v1'

    # OTP
    api.add_resource(QuestionPapers, '/get-question')

    api.add_resource(SignUp, '/signup')

    api.add_resource(Login, '/login')

    api.add_resource(Logout, '/logout')

    api.add_resource(InputConfig, '/config')