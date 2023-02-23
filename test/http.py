from odoo import http
import logging

_logger = logging.getLogger(__name__)

origin_dispatch_rpc = http.dispatch_rpc


def new_dispatch_rpc(service_name, method, params):
    _logger.info('........params.........')
    _logger.info(params)
    res = origin_dispatch_rpc(service_name, method, params)
    return res

http.dispatch_rpc = new_dispatch_rpc