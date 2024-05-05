from odoo import fields, models, api
from odoo.exceptions import AccessError
import logging
import requests
_logger = logging.getLogger(__name__)



class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    # adds a new field to the existing table of the ticket. There will be stored the generated answers of the AI.
    ai_answer = fields.Text(string="AI Answer")
    ai_answer_ready = fields.Boolean(string="AI Answer is ready", default=False)

    #answer_regenerated = fields.Text(string="regenerated Answer!")

    # this method gets called when button is clicked

    def ai_answer_button(self):
        _logger.info("Test button clicked..")


        json_data = {
            "qId": self.id,
            "question": self.description,
        }

        self.ai_answer_ready=False

        headers = {'Content-Type': 'application/json'}
        url = 'http://app:5000/data'
        try:
            requests.post(url, json=json_data, headers=headers)
        except:
            _logger.info("LLM not available")
            raise AccessError("LLM not available")

    def show_ai_answer(self):
        _logger.info("showed answer...")
        return None







