# -*- coding: utf-8 -*-
{
    'name': "native china",

    'summary': """
        实际了中国人的习惯的一些定制
        """,

    'description': """
        实际了中国人的习惯的一些定制:
        --Power by
        --公司图标
    """,

    'author': "Mfs Company",
    'website': "http://www.mfsystem.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'audit',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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