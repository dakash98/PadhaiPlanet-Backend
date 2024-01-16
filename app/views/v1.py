import json
from flask_restful import Resource
from flask import Response, request
from app.config.logger import logger
from app.constants import STANDARD, SUBJECT, MEDIUM
from app.services import QuestionService, UserService


def on_failure(msg: str = "Something went wrong!"):
    def decorate(f):
        def applicator(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error raised : {e}")
                return Response(
                    response=json.dumps({"meta": {"status_code": 3000, 'success': True,
                                                  "message": msg}, "data": {}}, default=str),
                    status=500, headers={'content-type': 'application/json'}
                )
        return applicator
    return decorate


class Login(Resource):

    @on_failure()
    def post(self):
        data = request.json
        email_or_phone = data.get('email_or_phone')
        password = data.get('password')

        if not email_or_phone or not password:
            return Response(
                response=json.dumps({"meta": {"status_code": 1001, 'success': False,
                                              "message": "Fields Missing"}, "data": {"message": "Please provide missing fields."}}, default=str),
                status=200,
                headers={'content-type': 'application/json'}
            )

        user = UserService.check_user_credentials(email_or_phone, password)

        msg, user_id, success, status_code = "Invalid user", None, False, 1001

        if user:
            msg = "User logged in"
            user_id = user.id
            success = True
            status_code = 1000

        return Response(
            response=json.dumps({"meta": {"status_code": status_code, 'success': success,
                                "message": msg}, "data": {"user_id": user_id}}, default=str),
            status=200,
            headers={'content-type': 'application/json'})


class Logout(Resource):

    @on_failure()
    def post(self):
        data = request.json
        user_id = data.get("user_id")

        if not user_id:
            return Response(
                response=json.dumps({"meta": {"status_code": 1001, 'success': False,
                                              "message": "Fields Missing"}, "data": {"message": "Please provide missing fields."}}, default=str),
                status=200,
                headers={'content-type': 'application/json'}
            )
        
        msg = "Invalid user"
        status_code = 1001
        success = False
        
        if int(user_id) > 0:
            msg = "Logged Out Successfully"
            status_code = 1000
            success = True

        return Response(
            response=json.dumps({"meta": {"status_code": status_code, 'success': success,
                                "message": msg}, "data": {}}, default=str),
            status=200,
            headers={'content-type': 'application/json'})


class SignUp(Resource):

    @on_failure()
    def post(self):
        data = request.json
        name = data.get('name')
        phone = data.get('phone')
        password = data.get('password')
        email = data.get('email')
        role = data.get('role')

        if not phone or not password or not email:
            return Response(
                response=json.dumps({"meta": {"status_code": 1001, 'success': False,
                                              "message": "Fields Missing"}, "data": {"message": "Please provide missing fields."}}, default=str),
                status=200,
                headers={'content-type': 'application/json'}
            )

        user = UserService.create_user(name, email, phone, password, role)

        msg = "User can not be saved. Please try again later."
        user_id = None
        status_code = 1001
        success = False

        if user:
            msg = "User saved successfully"
            user_id = user.id
            status_code = 1000
            success = True

        return Response(
            response=json.dumps({"meta": {"status_code": status_code, 'success': success,
                                "message": msg}, "data": {"user_id": user_id}}, default=str),
            status=200,
            headers={'content-type': 'application/json'}
        )


class QuestionPapers(Resource):

    @on_failure()
    def get(self):
        query_params = request.args
        subject = SUBJECT[query_params.get('subject')]
        medium = MEDIUM[query_params.get('medium')]
        standard = STANDARD[query_params.get('standard')]

        if not subject or not medium or not standard:
            return Response(
                response=json.dumps({"meta": {"status_code": 1001, 'success': False,
                                              "message": "Fields Missing"}, "data": {"message": "Please provide missing fields."}}, default=str),
                status=200,
                headers={'content-type': 'application/json'}
            )

        question_papers = QuestionService.get_all_question_papers(
            subject, medium, standard)
        return Response(
            response=json.dumps({"meta": {"status_code": 1000, 'success': True,
                                "message": ""}, "data": question_papers}),
            status=200,
            headers={'content-type': 'application/json'}
        )


class InputConfig(Resource):

    @on_failure()
    def get(self):
        data = {
            "subject": [{"key": "english", "value": "English"}, {"key": "hindi_full", "value": "Hindi (Full)"}, {"key": "hindi_half", "value": "Hindi (Composite/Half)"}, {"key": "sanskrit_full", "value": "Sanskrit (Full)"},
                        {"key": "sanskrit_half", "value": "Sanskrit (Half/Composite)"}, {"key": "marathi", "value": "Marathi"}, {"key": "history_and_political_science", "value": "History and Political Science"}, {"key": "geography", "value": "Geography"},
                        {"key": "math_1", "value": "Mathematics 1"}, {"key": "math_2", "value": "Mathematics 2"}, {"key": "science_1", "value": "Science and Technology 1"}, {"key": "science_2", "value": "Science and Technology 2"}],
            "standard": [{"key": "10", "value": "10th"}],
            "medium": [{"key": "english", "value": "English"}, {"key": "marathi", "value": "Marathi"}, {"key": "semi_english", "value": "Semi-English"}]
        }
        return Response(
            response=json.dumps({
                "meta": {
                    "status_code": 1000,
                    'success': True,
                    "message": ""
                },
                "data": data
            }),
            status=200,
            headers={'content-type': 'application/json'}
        )
