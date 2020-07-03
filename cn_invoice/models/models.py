# -*- coding: utf-8 -*-

from odoo import models, fields, api,exceptions


class invoicergister(models.Model):
    _name = 'cn.invoice'
    _description = 'Invoice registering'

    invoice_type = fields.Selection([('a','电子发票'), ('b','纸质普通发票'),('c','纸质专用发票'),('d','收据')], required=True )
    customer_net_id = fields.Char(string="Customer Net ID", required=True)
    order_no=fields.Char( string ='Order No')
    to_company = fields.Char(string="To Company", required=True)
    tax_id = fields.Char(string="Tax ID", required=True)

    # specified invoice needed informaiton
    bank_id = fields.Char(string="Bank Account ID")
    bank_name = fields.Char(string="Bank Name")
    address = fields.Char(string="Address")
    telephone = fields.Char(string="Telephone")

    note = fields.Text(string="Note")
    splited = fields.Boolean(string="Splited?", required=True)
    email = fields.Char(string="Email")

    state = fields.Selection( [('draft','Draft'),('apply_invoice', 'apply_invoice'),('done','Done')],default='draft')

    order_line= fields.One2many("cn.orderline","cn_invoice_id",string='sku')
    content_line =fields.One2many("cn.content","cn_invoice_id",string='sku')

    def action_submit(self):
        self.state = 'apply_invoice'


    def action_apply(self):
        self.state = 'done'

    # def action_confirm(self):
    #     self.state = 'done'

    def action_reset(self):
       self.state = 'draft'

    # disable delete record on state done
    def unlink(self):
        for order in self:
            if self.state =='done':
                raise exceptions.UserError('You cannot Delete this record')
        return super().unlink()


class cn_orderline(models.Model):
    _name = 'cn.orderline'
    _description = 'Order Line'
    name=fields.Char(string="Order Line")
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


class cn_Content(models.Model):
    _name = 'cn.content'
    _description = 'Invoice Content'
    name =fields.Char(string="Invoice Content")
    sku = fields.Char(string="SKU")
    product_name = fields.Char(string="Product_Name", required=True)
    qty = fields.Float(string="Qty", required=True)
    unit_price = fields.Float(string="Unit_price", required=True)
    amount = fields.Float(string="Amount", compute="_amount")
    cn_invoice_id = fields.Many2one("cn.invoice")

    @api.depends('qty', 'unit_price')
    def _amount(self):
        for r in self:
            r.amount = r.unit_price * r.qty
