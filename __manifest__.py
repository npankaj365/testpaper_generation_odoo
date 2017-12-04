# -*- coding: utf-8 -*-
{
    'name': "Assessment",

    'summary': """
        Rubric based Assessment Module""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Pankaj Niroula",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'survey'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assessment_views.xml',
        'views/test_creation_views.xml',
        'views/lesson_views.xml',
        'views/question_form.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}