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


class AddressesController(rest.RestController):

    '''
       None 表示这个方法没有返回值
       status_code 表示这个API的响应状态码是201
       test eg:
       curl -X POST http://localhost:8080/v1/addresses -H "Content-Type: application/json" -d '{"phone": ["1000860","100876"], "age": 24, "user_id": "133", "name": "kile", "email": "111@163.com"}' -v

    '''
    @expose.expose(None, body=Address, status_code=201)
    def post(self, add):
        db_conn = request.db_conn
        db_conn.add_address(add)

    @expose.expose(Addresses)
    def get(self):
        openid = pecan.request.headers.get('openid')
        logger.info("Get all addresses Method is called ...")
        """

        address_info_list = [
            {
                'name': 'Alice',
                'age': 30,
            },
            {
                'name': 'Bob',
                'age': 40,
            }
        ]
        addresses_list = [Address(**address_info) for address_info in address_info_list]
        """
        db_conn = request.db_conn
        adds = db_conn.list_addresses(openid)
        if len(adds) == 0:
            return R_Address()
        addresses_list = []
        for add in adds:
            a = R_Address()
            a.id = add.id
            a.openid = add.openid
            a.province = add.province
            a.city = add.city
            a.area = add.area
            a.address = add.address
            a.tel = add.tel
            a.name = add.name

            addresses_list.append(a)
        return Addresses(addresses=addresses_list)

    @pecan.expose()
    def _lookup(self, id, *remainder):
        return AddressController(id), remainder


class AddressController(rest.RestController):

    def __init__(self, id):
        self.id = int(id)

    """
    test eg:
         http://127.0.0.1:8080/v1/addresses/id
    """
    @expose.expose(R_Address)
    def get(self):
        """
         logger.info("v1 AddressController Get Method is called ...")
        address_info = {
            'id': self.id,
            'name': 'Alice',
            'age': 30,
        }
        """
        # logger.info("user_id %s" % self.user_id)
        db_conn = request.db_conn
        add = db_conn.get_address(self.id)
        if add is None:
            logger.info("address by id is not found...")
            return R_Address()
        else:
            logger.info(
                "address by id is found ...%s %s %s " %
                (add.id, add.name, add.address))
            a = R_Address()
            a.id = add.id
            a.openid = add.openid
            a.province = add.province
            a.city = add.city
            a.area = add.area
            a.address = add.address
            a.tel = add.tel
            a.name = add.name
            return a

    """
    test eg:
         curl -X PUT http://localhost:8080/v1/users/12 -H "Content-Type: application/json" -d '{"user_id": "12","name": "Cook", "age":50}'
    """
    @expose.expose(R_Address, body=R_Address)
    def put(self, add):
        logger.info("v1 AddressController Put Method is called ...")
        """
            address_info = {
            'id': add.id,
            'name': add.name,
            'age': add.age
        }
        return R_Address(**address_info)
        """
        db_conn = request.db_conn
        r_add = db_conn.update_address(add)
        return r_add

    # """
    # test eg:
    #      curl -X DELETE http://localhost:8080/v1/users/123
    # """

    @expose.expose()
    def delete(self):
        logger.info("v1 AddressController Delete Method is called ...")
        # print('Delete address_id: %s' % self.id)
        db_conn = request.db_conn
        db_conn.delete_address(self.id)
