#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pecan
from pecan import rest
from wsme import types as wtypes
import logging
from webdemo.api import expose
from pecan import request
logger = logging.getLogger(__name__)

class Address(wtypes.Base):
    openid = wtypes.text
    province = wtypes.text
    city = wtypes.text
    area = wtypes.text
    address = wtypes.text
    tel = wtypes.text
    name = wtypes.text

class R_Address(wtypes.Base):
    openid = wtypes.text
    province = wtypes.text
    city = wtypes.text
    area = wtypes.text
    address = wtypes.text
    tel = wtypes.text
    name = wtypes.text
    id = int

class Addresses(wtypes.Base):
    addresses = [R_Address]


class CsController(rest.RestController):

    '''
       None 表示这个方法没有返回值
       status_code 表示这个API的响应状态码是201
       test eg:
       curl -X POST http://localhost:8080/v1/cs -H "Content-Type: application/json" -d '{"phone": ["1000860","100876"], "age": 24, "user_id": "133", "name": "kile", "email": "111@163.com"}' -v

    '''
    # @expose.expose(None, body=Address, status_code=201)
    # def post(self, add):
    #     db_conn = request.db_conn
    #     db_conn.add_address(add)

    @expose.expose(wtypes.text)
    def get(self):
        
        return ''

    