# -*- coding: utf-8 -*-
{
    'name': "expertise",

    'summary': """
        利用专家的工作来获取必要的审计证据
        """,

    'description': """
利用专家的工作来获取必要的审计证据
==============================

主要程序
-------------
        
    * 当利用专家的工作来获取必要的审计证据是必要时,由项目组成员提出        
    * 项目负责人考虑是否利用专家的工作        
    * 当决定利用专家的工作时需要与专家签订书面协议    
    * 对专家的工作成果进行评估        
    * 注意对利用专家的工作的事项在审计报告中表述        
    * 利用专家工作是否实现目的的结论
    
如何使用
-----------

    * Tools/Expertise/Expertise
    """,

    'author': "Mfs Company",
    'website': "http://www.mfsystem.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'audit',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','native_china','audit'],

    # always loaded
    'data': [
        'security/security.xml',             
        'security/ir.model.access.csv',
        'security/data.xml',
        'views/views.xml',
#         'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}