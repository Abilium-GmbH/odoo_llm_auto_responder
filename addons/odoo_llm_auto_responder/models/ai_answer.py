from odoo import fields, models
import psycopg2
import logging
_logger = logging.getLogger(__name__)

# Connect to an existing database
""" conn = psycopg2.connect(
    database='postgres',
    user='odoo',
    password='odoo',
    host='0.0.0.0',
    port='5432') """




class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    # Adds a new field to the existing table of the ticket. There will be stored the generated answers of the AI
    ai_answer = fields.Text(string="AI Answer")


    # This method gets called when button is clicked -> Insert the DB queries here
    def ai_answer_button(self):
        _logger.info("Button was clicked...")

    """# Version 1
        self.env.cr.execute("update helpdesk_ticket set ai_answer 'Das ist eine vorgefertigte Antwort!'")
        self.env.cr.commit()

        res = self.env.cr.fetchall("select description from helpdesk_ticket")
        _logger.info(res)"""

    """"# Version 2
         # Open cursor to perform database operations
        cur = conn.cursor()
    # Insert data
        cur.execute("INSERT INTO helpdesk.ticket (ai_answer) VALUES ('Das ist eine vorgefertigte Antwort!')")
    # Query the database
        cur.execute("SELECT description FROM helpdesk.ticket")
        descriptions = cur.fetchall() 
        logger.info(descriptions)

    # Close communication with database
    # cur.close()"""

