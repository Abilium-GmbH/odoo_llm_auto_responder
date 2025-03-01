from odoo import fields, models, api
from odoo.exceptions import AccessError
import logging
import requests

_logger = logging.getLogger(__name__)


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"
    ai_answer = fields.Text(string="AI Answer")
    ai_answer_ready = fields.Boolean(string="AI Answer is ready", default=False)
    description = fields.Text(inverse='_set_description')

    def ai_answer_button(self):
        _logger.info("Test button clicked..")

        json_data = {
            "qId": self.id,
            "question": self.description,
        }

        self.ai_answer_ready = False

        headers = {'Content-Type': 'application/json'}
        url = 'http://app:5000/data'
        try:
            requests.post(url, json=json_data, headers=headers)
        except:
            _logger.info("LLM not available")
            raise AccessError("LLM not available")

        message = 'AI answer-generation is in progress, please click "AI Answered!"'
        return {'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {'message': message,
                           'type': 'success',
                           'sticky': False,
                           }
                }

    def show_ai_answer(self):
        _logger.info("showed answer...")
        return None

    # this inverse method triggers automatic LLM answering
    def _set_description(self):
        _logger.info("inverse description triggered")

        json_data = {
            "qId": self.id,
            "question": self.description,
        }

        headers = {'Content-Type': 'application/json'}
        url = 'http://app:5000/data'
        try:
            requests.post(url, json=json_data, headers=headers)
        except:
            _logger.info("LLM not available")
            raise AccessError("LLM not available")
        finally:
            return
