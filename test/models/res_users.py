from odoo import models, tools
import logging

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = 'res.users'

    @classmethod
    @tools.ormcache('uid', 'passwd')
    def check(cls, db, uid, passwd):
        _logger.info('..........................')
        _logger.info(uid)
        _logger.info(passwd)
        return super(ResUsers, cls).check(db, uid, passwd)