# -*- coding: utf-8 -*-
from openerp import http

# class PersistOperation(http.Controller):
#     @http.route('/persist_operation/persist_operation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/persist_operation/persist_operation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('persist_operation.listing', {
#             'root': '/persist_operation/persist_operation',
#             'objects': http.request.env['persist_operation.persist_operation'].search([]),
#         })

#     @http.route('/persist_operation/persist_operation/objects/<model("persist_operation.persist_operation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('persist_operation.object', {
#             'object': obj
#         })