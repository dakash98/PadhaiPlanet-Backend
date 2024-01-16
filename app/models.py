from app.config.mysql import db
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    email = db.Column('email', db.String(255))
    phone = db.Column('phone', db.Integer)
    password = db.Column('password', db.String(255))
    role = db.Column('role', db.String(255))
    created_at = db.Column('created_at', db.DateTime, server_default=db.func.now())
    updated_at = db.Column('updated_at', db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    @classmethod
    def add_user(cls, phone: int, email: str, name: str, password: str | None, role: str) -> object:
        new_user = cls(
            phone=phone,
            email=email,
            name=name,
            password=generate_password_hash(password, method='sha256') if password else None,
            role=role
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @classmethod
    def verify_password(cls, user_passwd: str, given_passwd: str) -> bool:
        return check_password_hash(user_passwd, given_passwd)

    @classmethod
    def update_password(cls, user_id: int, new_password: str) -> None:
        user = cls.find_by_id(user_id)
        user.password = generate_password_hash(new_password, method='sha256')
        db.session.commit()

    @classmethod
    def find_by_id(cls, user_id: int) -> object:
        return cls.query.filter_by(id=user_id).first()
    

class QuestionPapers(db.Model):
    __tablename__ = 'question_papers'

    id = db.Column('id', db.Integer, primary_key=True)
    year = db.Column('name', db.Integer)
    standard = db.Column('standard', db.String(55))
    medium = db.Column('medium', db.String(55))
    subject = db.Column('subject', db.String(255))
    file_name = db.Column('file_name', db.String(255))
    solution_url = db.Column('solution_url', db.String(255))
    created_at = db.Column('created_at', db.DateTime, server_default=db.func.now())
    updated_at = db.Column('updated_at', db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
