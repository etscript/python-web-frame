#!/usr/bin/env python
#-*- coding: utf-8 -*-
from pecan import rest
from wsme import types as wtypes
from webdemo.api import expose
from webdemo.api.controllers.v1 import controller as v1_controller
import logging
logger = logging.getLogger(__name__)


class RootController(rest.RestController):
    v1 = v1_controller.v1Controller()

    """
    test eg:
         http://127.0.0.1:8080/
    """
    @expose.expose(wtypes.text)
    def get(self):
        logger.info("Method Get is called ...")
        return "python-web-frame: pecan & wsme "

    # @expose.expose()
    # def _route(self, args):
    #     """Overrides the default routing behavior.

    #     It redirects the request to the default version of the magnum API
    #     if the version number is not specified in the url.
    #     """

    #     if args[0] and args[0] not in self._versions:
    #         args = [self._default_version] + args
    #     return super(RootController, self)._route(args)