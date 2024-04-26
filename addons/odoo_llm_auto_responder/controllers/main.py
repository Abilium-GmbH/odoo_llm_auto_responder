from odoo import http
import logging
_logger = logging.getLogger(__name__)




class AIAnswerController(http.Controller):
    @http.route("/ai_answer/answer", type="json", auth="public")
    def receive_ai_answer(self, **kw):
        _logger.info("notification: received answer")
        answer = http.request.env['helpdesk.ticket'].sudo().search([('id', '=', kw['id'])])
        answer.write({'ai_answer': kw['ai_answer']})
        _logger.info("Description", answer.ai_answer)
        _logger.info("notification: saved answer")
        """self.answer_ready_notification()"""
        answer_status = http.request.env['helpdesk.ticket'].sudo().search([('id', '=', kw['id'])])
        answer_status.write({'ai_answer_ready': True})
        return 1

    """def answer_ready_notification(self):
        message = 'AI Answer is generated and saved'
        return {'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {'message': message,
                           'type': 'success',
                           'sticky': False,
                           }
                }"""