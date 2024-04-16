from odoo import http
import logging
_logger = logging.getLogger(__name__)


class AIAnswerController(http.Controller):
    @http.route("/ai_answer/answer", type="json", auth="public")
    def receive_ai_answer(self, **kw):
        _logger.info("notification: received answer")
        answer = http.request.env['helpdesk.ticket'].search([('id', '=', kw['id'])])
        answer.write({'ai_answer': kw['ai_answer']})
        _logger.info("notification: saved answer")
        return 1

