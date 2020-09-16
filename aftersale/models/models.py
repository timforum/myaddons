# -*- coding: utf-8 -*-

from odoo import models, fields, api


class aftersale(models.Model):
    _name = 'aftersale.aftersale'
    _description = 'aftersale.aftersale'

    name = fields.Char()
    serial_no = fields.Char()
    order_no = fields.Char()
    purchase_date = fields.Date()
    using_dates = fields.Float()
    request_date = fields.Date()
    weixin_no = fields.Char()
    priorit = fields.Selection([('a', 'urgent--important'), ('b', 'urgent--important'), ('c', 'non-urgent--important'),
                                ('d', 'non-urgnet--unimportant')], required=True)
    stage = fields.Selection([('a', 'Reuest'), ('b', 'Handeling'), ('c', 'Replace parts'), ('c', 'Done')])
    problem = fields.Char()
    note = fields.Text()
    products_line= fields.Many2one('aftersale.products',string="name")


class products(models.Model):
    _name = 'aftersale.products'
    _description = 'aftersale.products'
    name = fields.Char()
    sku = fields.Char()
