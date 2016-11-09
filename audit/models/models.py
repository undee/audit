# -*- coding: utf-8 -*-

from openerp import models, fields, api

class audit(models.Model):
    _name = 'audit.audit'
    _inherit = 'mail.thread'  

    name = fields.Char()
    report_data=fields.Date()
