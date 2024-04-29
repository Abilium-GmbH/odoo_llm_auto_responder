# -*- coding: utf-8 -*-
{
    'name': "Odoo LLM Auto Responder",

    'summary': """
		
		""",

    'description': """
	    
	""",

    'author': "Abilium GmbH",
    'website': "https://www.abilium.io",

    'category': '',
    'version': '0.0.1',
    'application': True,
    'sequence': 1,

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'web',
        'helpdesk_mgmt'
    ],
    # always loaded
    'data': [
        'data/llm_auto_responder_data.xml',
        'views/ai_button_view.xml',
        'views/ai_kanban_view.xml'
    ],
    'demo': [

    ],

    'assets': {

    }
}
