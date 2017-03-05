from sqlalchemy.ext import declarative
from sqlalchemy import Index
from sqlalchemy import Column, Integer, String

Base = declarative.declarative_base()


def int_dbs(_ENGINE):
    Base.metadata.create_all(_ENGINE)


def drop_dbs(_ENGINE):
    Base.metadata.drop_all(_ENGINE)


class db_User(Base):

    __tablename__ = 'user'
    __table_args__ = (
        Index('ix_user_user_id', 'user_id'),
    )
    id = Column(Integer, primary_key=True)
    user_id = Column(String(255), nullable=False)
    name = Column(String(64), nullable=False, unique=True)
    gender = Column(String(64), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(255))

    def __repr__(self):
        return "<User(user_id='%s', name='%s', gender='%s',age='%s',email='%s')>" % (
            self.user_id, self.name, self.gender, self.age, self.email)

    def __init__(self, user_id, name, gender, age, email):
        self.user_id = user_id
        self.name = name
        self.gender = gender
        self.age = age
        self.email = email
