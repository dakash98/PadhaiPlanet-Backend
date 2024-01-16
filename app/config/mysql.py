from flask_sqlalchemy import SQLAlchemy
# from app.config import secrets


DB_HOST = "127.0.0.1" # secrets["MYSQL_HOST"]
DB_USER = "akashdeep" # secrets["MYSQL_USER"]
DB_PASS = "akash123" # secrets["MYSQL_PASSWORD"]
DB_NAME =  "padhai_planet" # secrets["MYSQL_DATABASE"]
SQLALCHEMY_POOL_TIMEOUT = 100 # int(secrets["SQLALCHEMY_POOL_TIMEOUT"])  # Specifies the connection timeout in seconds for the pool
SQLALCHEMY_PRE_PING = True # bool(secrets["SQLALCHEMY_PRE_PING"])


class Config:
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_timeout': SQLALCHEMY_POOL_TIMEOUT, 'pool_pre_ping': SQLALCHEMY_PRE_PING}
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()
