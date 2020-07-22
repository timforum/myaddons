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
    store_name = fields.Selection(
        [('tmsmzyd', '天猫数码专营店'), ('tmzmd', '天猫makeblock专卖店'), ('jdsmzyd', '京东数码专营店'), ('tbkakamaker', '咖咖>创客官方店'),
         ('1688', '咖咖创客1688'), ('others', '其它')], required=True)

    copy_paste_tax = fields.Text(string='copy & paste tax information')
    copy_paste_order = fields.Text(String = 'copy & paste order information')

    #specified invoice needed informaiton
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

    @api.constrains('tax_id')
    def _verify_tax_id(self):
        for r in self:
            s = r.tax_id
            x=s.split(",")
            print (1)




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
            if self.state =='done' or self.state == 'apply_invoice':
                raise exceptions.UserError('You cannot Delete this record, unless you reset it to draft')
        return super().unlink()

    def button_demo(self):
        self.copy_paste_tax =""
        # self.invoice_type="aaa"
        self.to_company="bbb"
        self.tax_id = "cccc"







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
