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
            "subject": ["hindi", "mathematics", "english", "science"],
            "standard": ['10'],
            "medium": ['english', 'marathi', 'semi-english']
        }
        return Response(
            response=json.dumps({
                "meta": {
                    "status_code": 1000,
                    'success': True,
                    "message": "msg"
                },
                "data": data
            }),
            status=200,
            headers={'content-type': 'application/json'}
        )
