from odoo import fields, models, api
from odoo.exceptions import AccessError
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
        """except:
            _logger.info("LLM not available")
            raise AccessError("LLM not available")"""

        _logger.info("Nachricht", message)
        return super().action_send_mail()


