# -*- coding: utf-8 -*-

from odoo import models, fields, api

class invoicergister(models.Model):
    _name = 'cn.invoice'
    _description = 'Invoice registering'

    invoice_type = fields.Selection([('a','电子发票'), ('b','纸质普通发票'),('c','纸质专用发票'),('d','收据')], required=True )
    customer_net_id = fields.Char(string="Customer Net ID", required=True)
    order_no=fields.Char( string ='Order No', required=True)
    to_company = fields.Char(string="To Company", required=True)
    tax_id = fields.Char(string="Tax ID", required=True)
    note = fields.Text(string="Note")
    splited = fields.Boolean(string="Splited?", required=True)
    email = fields.Char(string="Email")

    state = fields.Selection( [('draft','Draft'),('done','Done')],default='draft')

    order_line= fields.One2many("cn.orderline","cn_invoice_id",string='sku')

    def action_draft(self):
        self.state = 'draft'

    def action_confirm(self):
        self.state = 'done'


    def action_reset(self):
       self.state = 'Reset to draft'






class cn_orderline(models.Model):
    _name = 'cn.orderline'
    _description = 'Order Line'
    sku = fields.Char(string="SKU")
    product_name = fields.Char(string="Product_Name",required=True)
    qty = fields.Float(string="Qty", required=True)
    unit_price = fields.Float(string="Unit_price",required=True)
    amount = fields.Float(string="Amount", compute="_amount")
    cn_invoice_id = fields.Many2one("cn.invoice")

    @api.depends('qty','unit_price')
    def _amount(self):
        for r in self:
            r.amount = r.unit_price * r.qty


class cn_content(models.Model):
    _name = 'invoice_content'
    _description = 'Invoice Content'
    product_name = fields.Char(string="Product_Name",required=True)
    qty = fields.Float(string="Qty", required=True)
    unit_price = fields.Float(string="Unit_price",required="True")
    # amount = fields.Float(string="Amount", compute="_amount_")
    # cn_invoice_id = fields.Many2one("cn.invoice",string="to_company" )

    #
    # @api.depends(qty,unit_price)
    # def _amount_(self):
    #     for r in self:
    #         r.amount = r.unit_price * r.qty


