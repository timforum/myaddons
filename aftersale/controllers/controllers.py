# -*- coding: utf-8 -*-
# from odoo import http


# class Aftersale(http.Controller):
#     @http.route('/aftersale/aftersale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aftersale/aftersale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aftersale.listing', {
#             'root': '/aftersale/aftersale',
#             'objects': http.request.env['aftersale.aftersale'].search([]),
#         })

#     @http.route('/aftersale/aftersale/objects/<model("aftersale.aftersale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aftersale.object', {
#             'object': obj
#         })
