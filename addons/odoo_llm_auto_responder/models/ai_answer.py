from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)



class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    # Adds a new field to the existing table of the ticket. There will be stored the generated answers of the AI
    ai_answer = fields.Text()

    # This method gets called when button is clicked -> Insert the DB queries here
    def ai_answer_button(self):
        _logger.info("Test button clicked..")

