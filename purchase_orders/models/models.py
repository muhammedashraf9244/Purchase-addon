# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrderTest(models.Model):
    _name = 'purchase.order.test'
    _rec_name = 'order_name'

    def state_to_be_approved(self):
        for rec in self:
            rec.state = 'to be approved'

    def state_approved(self):
        for rec in self:
            rec.state = 'approve'

    def state_to_be_canceled(self):
        for rec in self:
            rec.state = 'cancel'

    def state_to_be_draft(self):
        for rec in self:
            rec.state = 'draft'

    def calculate_sub_total(self):
        for rec in self:
            for line in rec.order_lines:
                rec.sub_total += line.total

    # def send_email(self):
    #     template_id = self.env.ref('purchase_orders.order_mail_template').id
    #     print("template_id", template_id)
    #     template = self.env['mail.template'].browse(template_id)
    #     print("template", template)
    #     template.send_mail(self.id, force_send=True)
    #     print("self.id", self.id)
    #
    # def get_email_to(self):
    #     users = self.env['res.users'].search([])
    #     print("users", users)
    #     email_list = ""
    #     for user in users:
    #         if user.has_group('purchase_orders.purchase_manager_groups') and user.email:
    #             email_list += user.email + " "
    #     print(email_list)
    #     return email_list

    def send_email(self):
        # template_id = self.env.ref('purchase_orders.order_mail_template').id
        # print("template_id", template_id)
        # template = self.env['mail.template'].browse(template_id)
        # print("template", template)
        # template.send_mail(self.id, force_send=True)
        # print("self.id", self.id)

        users = self.env['res.users'].search([])
        print("users", users)
        for u in users:
            if u.has_group('purchase_orders.purchase_manager_groups') and u.email:
                print("user", u)
                template_email_to = self.env.ref('purchase_orders.order_mail_template')
                template_email_to.write({'email_to': u.email})
                template_id = self.env.ref('purchase_orders.order_mail_template').id
                print("template_id", template_id)
                template = self.env['mail.template'].browse(template_id)
                print("template", template)
                template.send_mail(self.id, force_send=True)
    #
        self.state = 'approve'
        print("workkk")

    def check_group(self):
        users = self.env['res.users'].search([])
        print("users", users)
        for user in users:
            if user.has_group('purchase_orders.purchase_manager_groups'):
                print("user", user)

    order_name = fields.Char(string="Order Name", required= True)
    requested_by = fields.Many2one('res.users', string="Requested by", required=True, default=lambda self: self.env.user)
    start_date = fields.Date(string="Start Date", default=fields.Date.today())
    end_date = fields.Date(string="End Date")
    order_lines = fields.One2many('purchase.order.test.line', 'order_id', string="Orders")
    sub_total = fields.Float(string="subtotal", compute=calculate_sub_total)
    reject_reason = fields.Text(string="Reject Reason")
    state = fields.Selection(
        {
            ('draft', 'Draft'),
            ('to be approved', 'To Be Approved'),
            ('approve', 'Approve'),
            ('reject', 'Reject'),
            ('cancel', 'Cancel'),
        }, string="States", default="draft"
    )
    email_id = fields.Char(string="Email")


class PurchaseOrderTestLine(models.Model):
    _name = 'purchase.order.test.line'

    @api.onchange('cost_price', 'quantity')
    def calculate_total(self):
        for rec in self:
            rec.total = rec.cost_price * rec.quantity

    @api.onchange('product_id')
    def get_description(self):
        for rec in self:
            rec.description = rec.product_id.name

    @api.onchange('product_id')
    def get_unit_price(self):
        for rec in self:
            rec.cost_price = rec.product_id.list_price

    product_id = fields.Many2one('product.product', string="Product", required=True)
    description = fields.Char("Description", readonly=True, compute=get_description)
    quantity = fields.Integer(string="Quantity", default=1)
    cost_price = fields.Float(string="Cost Price", readonly=True, compute=get_unit_price)
    total = fields.Float(string="Total", readonly=True, compute=calculate_total)
    order_id = fields.Many2one('purchase.order.test', string="Order ID")