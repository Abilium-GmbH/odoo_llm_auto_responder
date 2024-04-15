from odoo import http

"""class AIAnswerController(http.Controller):
    @http.route("/ai_anwser/answer", type="json", auth="user")
    def receive_ai_answer(self, **kw):
       answer = http.request.env['helpdesk.ticket'].search([('id', '=', kw['id])])
       answer.write('ai_answer': kw['ai_answer'])
       return kw
        
   
    Meldung ausgeben, dass die Antwort für Ticketnummer angekommen ist
    und gespeichert wurde -> Popup"""





