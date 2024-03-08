# -*- coding: utf-8 -*-
{
    'name': "Hello World",

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
        'web'
    ],
    # always loaded
    'data': [
        'views/menu.xml',
        'views/hello_world.xml'
    ],
    'demo': [

    ],

    'assets': {

    }
}