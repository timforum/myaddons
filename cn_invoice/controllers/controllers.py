# -*- coding: utf-8 -*-
# from odoo import http


# class CnInvoice(http.Controller):
#     @http.route('/cn_invoice/cn_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cn_invoice/cn_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cn_invoice.listing', {
#             'root': '/cn_invoice/cn_invoice',
#             'objects': http.request.env['cn_invoice.cn_invoice'].search([]),
#         })

#     @http.route('/cn_invoice/cn_invoice/objects/<model("cn_invoice.cn_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cn_invoice.object', {
#             'object': obj
#         })
