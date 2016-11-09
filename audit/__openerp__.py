# -*- coding: utf-8 -*-
{
    'name': "audit",

    'summary': """
        审计系统的基础模块,其他模块均依赖于它
        """,
    'description': """
        审计系统的基础模块,其他模块均依赖于它
    """,

    'author': "undee",
    'website': "http://www.mfsystem.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'audit',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

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