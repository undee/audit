# -*- coding: utf-8 -*-
from openerp import http

# class Expertise(http.Controller):
#     @http.route('/expertise/expertise/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/expertise/expertise/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('expertise.listing', {
#             'root': '/expertise/expertise',
#             'objects': http.request.env['expertise.expertise'].search([]),
#         })

#     @http.route('/expertise/expertise/objects/<model("expertise.expertise"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('expertise.object', {
#             'object': obj
#         })