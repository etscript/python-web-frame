#!/usr/bin/env python
#-*- coding: utf-8 -*-
from sqlalchemy import create_engine
import logging
from webdemo.db import models as db_models
import sqlalchemy.orm
from sqlalchemy.orm import exc
logger = logging.getLogger(__name__)
Domain = "sqlalchemy"


_ENGINE = None
_SESSION_MAKER = None


def get_engine():
    global _ENGINE
    if _ENGINE is not None:
        return _ENGINE
    _ENGINE = create_engine(
        "mysql+mysqldb://root:mysql@localhost:3306/wxapp?charset=utf8",
        echo=True)
    db_models.int_dbs(_ENGINE)
    return _ENGINE


def get_session_maker(engine):
    global _SESSION_MAKER
    if _SESSION_MAKER is not None:
        return _SESSION_MAKER
    _SESSION_MAKER = sqlalchemy.orm.sessionmaker(bind=engine)
    return _SESSION_MAKER


def get_session():
    engine = get_engine()
    maker = get_session_maker(engine)
    session = maker()
    return session


class Connection(object):

    def __init__(self):
        pass

    def get_user(self, openid):
        user = None
        query = get_session().query(
            db_models.db_User).filter_by(
            openid=openid)
        try:
            user = query.one()
        except exc.NoResultFound:
            logger.error("query by user_id not found ...")
        return user

    def list_users(self):
        users = dict()
        query = get_session().query(db_models.db_User)
        try:
            users = query.all()
        except exc.NoResultFound:
            logger.error("query all user occur error ...")
        return users

    def update_user(self, user):
        logger.info("user.user_id: %s" % (user.user_id))
        try:
            session = get_session()
            session.query(
                db_models.db_User).filter_by(
                user_id=user.user_id).update({"name": user.name,
                                              "gender": user.gender,
                                              "age": user.age,
                                              "email": user.email
                                              })
            session.flush()
            session.commit()
        except exc.NoResultFound:
            logger.error("update user occur error ...")

        return user # if success ,return the modify information

    def delete_user(self, user_id):
        logger.info("user.user_id: %s" % (user_id))
        try:
            session = get_session()
            user=session.query(
                db_models.db_User).filter_by(
                user_id=user_id).first()
            session.delete(user)
            session.flush()
            session.commit()
        except exc.NoResultFound:
            logger.error("delete user occur error ...")

    def add_user(self, user):
        # logger.info("user.nickname: %s" % (user.nickname))

        db_user = db_models.db_User(
            openid=user['openId'],
            nickname=user['nickName'],
            gender=user['gender'],
            country=user['country'],
            province=user['province'],
            city=user['city'],
        )
        try:
            session = get_session()
            session.add(db_user)
            session.flush()
            session.commit()
        except exc.NoResultFound:
            logger.error("add user occour error ...")

    def add_address(self, add):

        db_address = db_models.db_Address(
            openid=add.openid,
            province=add.province,
            city=add.city,
            area=add.area,
            address=add.address,
            tel=add.tel,
            name=add.name,
      )
        try:
            session = get_session()
            session.add(db_address)
            session.flush()
            session.commit()
        except exc.NoResultFound:
            logger.error("add address occour error ...")

    def get_address(self, id):
        add = None
        query = get_session().query(
            db_models.db_Address).filter_by(
            id=id)
        try:
            add = query.one()
        except exc.NoResultFound:
            logger.error("query by user_id not found ...")
        return add

    def list_addresses(self, openid):
        adds = dict()
        query = get_session().query(
            db_models.db_Address).filter_by(
            openid=openid)
        try:
            adds = query.all()
        except exc.NoResultFound:
            logger.error("query all addresses occur error ...")
        return adds

    def update_address(self, add):
        # logger.info("user.user_id: %s" % (user.user_id))
        try:
            session = get_session()
            session.query(
                db_models.db_Address).filter_by(
                id=add.id).update({"province": add.province,
                                        "city": add.city,
                                        "area": add.area,
                                        "address": add.address,
                                        "tel": add.tel,
                                        "name": add.name
                                        })
            session.flush()
            session.commit()
        except exc.NoResultFound:
            logger.error("update address occur error ...")

        return add # if success ,return the modify information

    def delete_address(self, id):
        # logger.info("user.user_id: %s" % (user_id))
        try:
            session = get_session()
            add=session.query(
                db_models.db_Address).filter_by(
                id=id).first()
            session.delete(add)
            session.flush()
            session.commit()
        except exc.NoResultFound:
            logger.error("delete address occur error ...")

    
