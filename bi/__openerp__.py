# -*- coding: utf-8 -*-
{
    'name': "bi",

    'summary': """
        project basic information
        """,

    'description': """
        例如财务报表编制基础
    """,

    'author': "undee",
    'website': "http://www.mfsystem.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'audit',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['audit','native_china'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}