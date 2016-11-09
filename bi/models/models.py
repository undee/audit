# -*- coding: utf-8 -*-

from openerp import models, fields, api

class fffr(models.Model):
    _name = 'fffr.fffr'

    name = fields.Char()
    persist_operation = fields.Boolean(help=u'编制基础是否明确要求管理层对持续经营能力进行评估')
    description = fields.Html(string='',help=u'描述编制基础对管理层进行持续经营能力进行评估的明确要求')