from sqlalchemy.ext import declarative
from sqlalchemy import Index
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative.declarative_base()


def int_dbs(_ENGINE):
    Base.metadata.create_all(_ENGINE)


def drop_dbs(_ENGINE):
    Base.metadata.drop_all(_ENGINE)


class db_User(Base):

    __tablename__ = 'user'
    __table_args__ = (
        Index('ix_user_openid', 'openid'),
    )
    id = Column(Integer, primary_key=True)
    openid = Column(String(255))
    nickname = Column(String(128))
    gender = Column(String(64))
    country = Column(String(128))
    #province = db.Column(db.String(128), index = True, unique = True)
    province = Column(String(128))
    city = Column(String(128))
    #created_time = db.Column(db.DateTime)
    #updated_time = db.Column(db.DateTime)

    # telephone = relationship(
    #     "db_Telephone",
    #     order_by="db_Telephone.id",
    #     back_populates="user" ,
    #     cascade="save-update, merge, delete")

    def __repr__(self):
        return "<User(openid='%s', nickname='%s', gender='%s',country='%s',province='%s',city='%s')>" % (
            self.openid, self.nickname, self.gender, self.country, self.province, self.city)

    # def __init__(self, openid, nickname, gender, country, province, city, telephone):
    def __init__(self, openid, nickname, gender, country, province, city):
        self.openid = openid
        self.nickname = nickname
        self.gender = gender
        self.country = country
        self.province = province
        self.city = city


class db_Telephone(Base):

    __tablename__ = 'telephone'
    id = Column(Integer, primary_key=True)
    telnumber = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    # user = relationship("db_User", back_populates="telephone")

    def __repr__(self):
        return "<Tele(telephone='%s')>" % self.telnumber
