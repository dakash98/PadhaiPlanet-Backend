# from flask_sqlalchemy import SQLAlchemy
# from app.config import secrets


# DB_HOST = secrets["MYSQL_HOST"]
# DB_USER = secrets["MYSQL_USER"]
# DB_PASS = secrets["MYSQL_PASSWORD"]
# DB_NAME = secrets["MYSQL_DATABASE"]
# SQLALCHEMY_POOL_TIMEOUT = int(secrets["SQLALCHEMY_POOL_TIMEOUT"])  # Specifies the connection timeout in seconds for the pool
# SQLALCHEMY_PRE_PING = bool(secrets["SQLALCHEMY_PRE_PING"])


# class Config:
#     SQLALCHEMY_ENGINE_OPTIONS = {'pool_timeout': SQLALCHEMY_POOL_TIMEOUT, 'pool_pre_ping': SQLALCHEMY_PRE_PING}
#     SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


# db = SQLAlchemy()
