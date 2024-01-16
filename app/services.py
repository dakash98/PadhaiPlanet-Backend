import boto3 as boto3
from app.models import User
from sqlalchemy.sql import text
from app.config.mysql import db
from botocore.client import Config
from app.config.logger import logger
from botocore.exceptions import ClientError
# from app.config.secret_manager import secrets

AWS_BUCKET_NAME = "padhai-planet" # secrets['AWS_BUCKET_NAME']
AWS_S3_ENDPOINT = "s3.ap-south-1.amazonaws.com" # secrets['AWS_S3_ENDPOINT']
AWS_REGION = "ap-south-1"

class UserService():

    @staticmethod
    def create_user(name, email, phone, password, role):

        try:
            user = User.add_user(phone, email, name, password, role)
            return user
        except Exception as e:
            logger.error(f"User can't be stored, because exception raised : {e}", exc_info=True)
            return False
        
    @staticmethod
    def check_user_credentials(email_or_phone, password):
        
        try:
            if "@" in email_or_phone:
                user = User.query.filter_by(email=email_or_phone).first()
            else:
                user = User.query.filter_by(phone=email_or_phone).first()

            if User.verify_password(user.password, password):
                return user
            
            return False

        except Exception as e:
            logger.error(f"User can't be stored, because exception raised : {e}", exc_info=True)
            return False


class QuestionService():

    @staticmethod
    def get_all_question_papers(subject, medium, standard):

        question_paper_query = text("select id, year, file_name, solution_url from question_papers where subject = :subject and medium= :medium and standard = :standard;")
        question_papers = db.session.execute(question_paper_query, {"subject": subject, "medium": medium, "standard": standard}).all()

        papers_list = []
        
        for item in question_papers:
            id = item[0]
            year = item[1]
            name = item[2]
            question_url = item[2]
            solution_url = item[3]

            year_exists = next((p for p in papers_list if p["year"] == year), None)

            if year_exists:
                year_exists["papers"].append({
                    "id": id,
                    "name": name,
                    "question_url": QuestionService.create_presigned_url(question_url, "10"),
                    "solution_url": solution_url
                })
            else:
                papers_list.append({
                    "year": year,
                    "papers": [{
                        "id": id,
                        "name": name,
                        "question_url": QuestionService.create_presigned_url(question_url, "10"),
                        "solution_url": solution_url
                    }]
                })

        return papers_list
    
    @staticmethod
    def create_presigned_url(filenames, category, expiration=30):
        """Generate a presigned URL to share an S3 object
        :param bucket_name: string
        :param filenames: string
        :param expiration: Time in seconds for the presigned URL to remain valid
        :return: Presigned URL as string. If error, returns None.
        """

        # Generate a presigned URL for the S3 object
        s3_client = boto3.resource(
            "s3", region_name=AWS_REGION, config=Config(signature_version="s3v4")
        )
        try:
            file_url_list = []
            if filenames != "" and filenames is not None:
                filename_list = filenames.split(',')
                for filename in filename_list:
                    complete_file_path = category + "/" + filename
                    response = s3_client.meta.client.generate_presigned_url('get_object',
                                                                Params={'Bucket': AWS_BUCKET_NAME,
                                                                        'Key': complete_file_path},
                                                                ExpiresIn=expiration)
                    file_url_list.append(response)
        except ClientError as e:
            return "Error in file upload %s." % (str(e))

        return file_url_list
        
    # @staticmethod
    # def get_s3_urls(file_names: str) -> list:
    #     """ Returns list of s3 urls for profile images"""
    #     file_url_list = list()

    #     if file_names:
    #         file_name_list = file_names.split(',')

    #         for file_name in file_name_list:
    #             fileurl = QuestionService.get_question_paper_url(file_name)
    #             file_url_list.append(fileurl)

    #     return file_url_list

    # @staticmethod
    # def get_question_paper_url(file_name):
    #     """
    #     Returns the url of the avatar image.
            
    #         Parameters:-
    #             file_name(str): Name of the avatar image
    #             category(str): Folder in which image exists
            
    #         Returns:-
    #             file_url(str): Url of the file
    #     """
    #     complete_file_path = f"10/{file_name}"
    #     file_url = f"https://{AWS_BUCKET_NAME}.{AWS_S3_ENDPOINT}/{complete_file_path}"
    #     return file_url