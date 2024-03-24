from odoo import fields, models


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    # Adds a new field to the existing table of the ticket. There will be stored the generated answers of the AI
    ki_answer = fields.Text()

    # This method gets called when button is clicked -> Insert the DB queries here
    def ki_answer_button(self):
        print("Test button clicked..")

