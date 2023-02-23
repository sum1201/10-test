from odoo import models, tools
import logging

_logger = logging.getLogger(__name__)


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def message_process(self, model, message, custom_values=None,
                        save_original=False, strip_attachments=False,
                        thread_id=None):
        _logger.info('*************')
        _logger.info(self.env.user.id)
        _logger.info('********')
        return super(MailThread, self).message_process(model, message, custom_values,
                                                       save_original, strip_attachments, thread_id)