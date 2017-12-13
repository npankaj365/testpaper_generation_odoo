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
        'views/domain_view.xml',
        'views/subdomain_view.xml',
        'views/lesson_views.xml',
        'views/objective_views.xml',
        'views/question_view.xml',
        'views/templates.xml',
        # 'views/rubric_view.xml',
        'reports/question_bank.xml',
        'reports/question_paper.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}