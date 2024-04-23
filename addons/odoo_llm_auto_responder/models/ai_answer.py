from odoo import fields, models, api
import os
import json
import logging
import requests
_logger = logging.getLogger(__name__)



class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    # adds a new field to the existing table of the ticket. There will be stored the generated answers of the AI.
    ai_answer = fields.Text(string="AI Answer")

    # this method gets called when button is clicked
    def ai_answer_button(self):
        _logger.info("Test button clicked..")

        self.ai_answer = 'KI responded with: ' + self.description

        json_data = {
            "qId": self.id,
            "question": self.description,
        }



        headers = {'Content-Type': 'application/json'}
        url = 'http://localhost:5001/data'
        requests.post(url, data=json_data, headers=headers)









