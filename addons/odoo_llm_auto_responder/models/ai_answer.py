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

        record_dict = {
            'id': self.id,
            'description': self.description,
        }


        with open('record_dict.json', 'w') as json_file:
            json.dump(record_dict, json_file, indent=4)

        json_data = json.dumps(record_dict)
        headers = {'Content-Type': 'application/json'}
        url = 'http://localhost:5000/data'
        response = requests.post(url, data=json_data, headers=headers)
        response_data = response.json()  # response von KI
        _logger.info("response received %s", response_data)
        self.ai_answer = 'Ki responded with: ' + response_data['text']









