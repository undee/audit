# -*- coding: utf-8 -*-
{
    'name': "inside audit",

    'summary': """
        CSA1141号   利用内部审计人员的工作
        """,

    'description': """
        
    """,

    'author': "Mfs Company",
    'website': "http://www.mfsystem.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'audit',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','native_china','audit'],

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