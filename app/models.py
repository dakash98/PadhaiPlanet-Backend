# from app.config.mysql import db


# class User(db.Model):
#     __tablename__ = 'users'

#     id = db.Column('id', db.Integer, primary_key=True)
#     name = db.Column('name', db.String(255))
#     phone = db.Column('phone', db.Integer)
#     email = db.Column('email', db.String(255))
#     password = db.Column('password', db.String(255))
#     created_at = db.Column('createddate', db.DateTime, server_default=db.func.now())
#     updated_at = db.Column('updateddate', db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
