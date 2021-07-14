# -*- coding: utf-8 -*-
from odoo import http

# class PurchaseOrders(http.Controller):
#     @http.route('/purchase_orders/purchase_orders/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_orders/purchase_orders/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_orders.listing', {
#             'root': '/purchase_orders/purchase_orders',
#             'objects': http.request.env['purchase_orders.purchase_orders'].search([]),
#         })

#     @http.route('/purchase_orders/purchase_orders/objects/<model("purchase_orders.purchase_orders"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_orders.object', {
#             'object': obj
#         })