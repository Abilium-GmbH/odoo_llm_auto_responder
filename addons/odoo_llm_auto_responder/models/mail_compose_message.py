from odoo import fields, models, api
import logging
import requests
_logger = logging.getLogger(__name__)


class MailComposer(models.TransientModel):
    _inherit = "mail.compose.message"
    
    
    def action_send_mail(self):
        message = self.body

        json_data = {
            "context": message
        }

        headers = {'Content-Type': 'application/json'}
        url = 'http://app:5000/store'
        requests.post(url, json=json_data, headers=headers)

        _logger.info("Nachricht", message)
        return super().action_send_mail()


