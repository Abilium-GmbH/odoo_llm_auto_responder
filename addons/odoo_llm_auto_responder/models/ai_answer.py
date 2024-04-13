from odoo import fields, models, api
import logging
import requests
import odoo.http as http


_logger = logging.getLogger(__name__)


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    # Adds a new field to the existing table of the ticket. There will be stored the generated answers of the AI
    ai_answer = fields.Text(string="AI Answer")

    # This method gets called when button is clicked -> Insert the DB queries here
    # @api.model
    def ai_answer_button(self):
        _logger.info("Button was clicked...")
        # New version
        self.write({'ai_answer': 'Das hier ist eine Testantwort!'})
        # ticket_id = self.id
        # description = self.env["helpdesk.ticket"].browse([ticket_id])
        # self.read([description])
        _logger.info(self.id)
        _logger.info(self.ai_answer)
        _logger.info(self.description)

    """ payload = {'id': self.id, 'description': self.description, 'ai_answer': none}
        r = requests.get('http://URL des Flaskservers', params=payload)"""

    """ 
    # Old version -> works
        self.env.cr.execute("update helpdesk_ticket set ai_answer = 'Das ist eine vorgefertigte Antwort!'")
        self.env.cr.commit()
        

        self.env.cr.execute("select number from helpdesk_ticket where id = %s", (self.id,))
        number = self.env.cr.fetchone()
        _logger.info(number)

        self.env.cr.execute("select ai_answer from helpdesk_ticket")
        ai_answer = self.env.cr.fetchone()
        _logger.info(ai_answer)

        self.env.cr.execute("select description from helpdesk_ticket")
        description = self.env.cr.fetchone()
        _logger.info(description)

    """
