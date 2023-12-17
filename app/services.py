# from models import User
# from config.mysql import db
from app.config.logger import logger

class UserService():

    @staticmethod
    def create_user(name, email, phone, password):

        # try:
        #     user_data = {
        #         "name": name,
        #         "email": email,
        #         "phone": phone, 
        #         "password": password
        #     }
        #     user = User(**user_data)
        #     db.session.add(user)
        #     db.session.commit()
        #     return user
        # except Exception as e:
        #     logger.error(f"User can't be stored, because exception raised : {e}", exc_info=True)
        #     return False
        
        return True




class QuestionService():

    @staticmethod
    def get_all_question_papers(subject, medium, standard):

        #TODO
        # Write query to fetch all the question papers 
        
        papers = [
            {
                "year": 2022,
                "papers": [
                    {"name": "Paper 1", "url": "https://www.africau.edu/images/default/sample.pdf"},
                    {"name": "Paper 2", "url": "https://www.africau.edu/images/default/sample.pdf"}
                ]
            },
            {
                "year": 2021,
                "papers": [
                    {"name": "Paper 1", "url": "https://www.africau.edu/images/default/sample.pdf"},
                    {"name": "Paper 2", "url": "https://www.africau.edu/images/default/sample.pdf"}
                ]
            }
        ]

        return papers

        