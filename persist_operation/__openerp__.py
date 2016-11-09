# -*- coding: utf-8 -*-
{
    'name': "persist_operation",

    'summary': """
        CSA 第1324号  持续经营
        """,

    'description': """
目标
===========

    *  获取管理层编制财务报表时运用持续经营假设的适当性的证据
    *  确定是否存在导致对持续经营能力产生重大疑虑的事项或情况
    
    """,

    'author': "undee",
    'website': "http://www.mfsystem.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'audit',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['native_china','audit','bi'],

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