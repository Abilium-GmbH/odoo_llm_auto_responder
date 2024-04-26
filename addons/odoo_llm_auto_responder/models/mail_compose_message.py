from odoo import fields, models, api
import logging
import requests
_logger = logging.getLogger(__name__)


class MailComposer(models.TransientModel):
    _inherit = "mail.compose.message"
    
    
    def action_send_mail(self):
        message = self.body
        _logger.info("Nachricht", message)
        return super().action_send_mail()


