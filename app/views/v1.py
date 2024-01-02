import json
from flask import Response, request
from flask_restful import Resource
from app.services import QuestionService, UserService


def on_failure(msg: str = "Something went wrong!"):
    def decorate(f):
        def applicator(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception:
                # logger.error(traceback.format_exc())
                return Response(
                    response=json.dumps({"meta": {"status_code": 3000, 'success': True,
                                                  "message": msg}, "data": {}}, default=str),
                    status=500, headers={'content-type': 'application/json'}
                )
        return applicator
    return decorate


# class Login(Resource):

#     # @on_failure()
#     def post(self):
#         data = request.json
#         email_or_phone = data.get('email_or_phone')
#         password = data.get('password')

#         if not email_or_phone or not password:
#             return Response(
#                 response=json.dumps({"meta": {"status_code": 1001, 'success': False,
#                                               "message": "Fields Missing"}, "data": {"message": "Please provide missing fields."}}, default=str),
#                 status=200,
#                 headers={'content-type': 'application/json'}
#             )

#         is_user_credential_correct = UserService.check_user_credentials(email_or_phone, password)

#         msg = "User logged in" if is_user_credential_correct else "Invalid user"

#         return Response(
#             response=json.dumps({"meta": {"status_code": 2001, 'success': True,
#                                 "message": "msg"}, "data": msg}, default=str),
#             status=200,
#             headers={'content-type': 'application/json'})

class Login(Resource):

    # @on_failure()
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
        
        msg = "Invalid user"
        status_code = 2001
        user_id = None
        if email_or_phone == "9999999999" and password == "Padhaiplanet@123":
            msg = "User logged in"
            status_code = 2000
            user_id = 10201

        return Response(
            response=json.dumps({"meta": {"status_code": status_code, 'success': True,
                                "message": msg}, "data": {"user_id": user_id}}, default=str),
            status=200,
            headers={'content-type': 'application/json'})
    

class Logout(Resource):

    # @on_failure()
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
        status_code = 2001
        
        if int(user_id) > 0:
            msg = "Logged Out Successfully"
            status_code = 2000

        return Response(
            response=json.dumps({"meta": {"status_code": status_code, 'success': True,
                                "message": "msg"}, "data": msg}, default=str),
            status=200,
            headers={'content-type': 'application/json'})


class SignUp(Resource):

    # @on_failure()
    def post(self):
        data = request.json
        name = data.get('name')
        phone = data.get('phone')
        password = data.get('password')
        email = data.get('email')

        if not phone or not password or not email:
            return Response(
                response=json.dumps({"meta": {"status_code": 1001, 'success': False,
                                              "message": "Fields Missing"}, "data": {"message": "Please provide missing fields."}}, default=str),
                status=200,
                headers={'content-type': 'application/json'}
            )

        is_user_saved = UserService.create_user(name, email, phone, password)

        msg = "User saved successfully" if is_user_saved else "User can not be saved. Please try again later."

        return Response(
            response=json.dumps({"meta": {"status_code": 1000, 'success': True,
                                "message": "msg"}, "data": msg}, default=str),
            status=200,
            headers={'content-type': 'application/json'}
        )


class QuestionPapers(Resource):

    @on_failure()
    def get(self):
        query_params = request.args
        subject = query_params.get('subject')
        medium = query_params.get('medium')
        standard = query_params.get('standard')

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
                                "message": "msg"}, "data": question_papers}),
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
