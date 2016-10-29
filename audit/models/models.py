# -*- coding: utf-8 -*-

from openerp import models, fields, api

class audit(models.Model):
    _name = 'audit.audit'

    name = fields.Char()
