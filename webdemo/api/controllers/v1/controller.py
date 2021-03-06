#!/usr/bin/env python
#-*- coding: utf-8 -*-
from pecan import rest
from wsme import types as wtypes
from webdemo.api import expose
from webdemo.api.controllers.v1 import users as v1_users
from webdemo.api.controllers.v1 import addresses as v1_addresses
from webdemo.api.controllers.v1 import customer_service as v1_cs
import logging
logger = logging.getLogger(__name__)


class v1Controller(rest.RestController):
    users = v1_users.UsersController()
    addresses = v1_addresses.AddressesController()
    cs = v1_cs.CsController()
    """
    test eg:
         http://127.0.0.1:8080/v1/
    """
    @expose.expose(wtypes.text)
    def get(self):
        logger.info("v1Controller Method Get is called ...")
        return "python-web-frame: pecan & wsme by v1Controller"
    
    