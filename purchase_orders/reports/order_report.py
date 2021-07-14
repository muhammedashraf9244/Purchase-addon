
from odoo import models, api


class OrderReport(models.AbstractModel):
    _name = 'report.purchase_orders.report_order_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['purchase.order.test'].browse(docids[0])
        orders = self.env['purchase.order.test.line'].search([('order_id', '=', docids[0])])
        orders_list = []
        for order in orders:
            vals= {
                'product_id': order.product_id.id,
                'quantity': order.quantity,
                'cost_price': order.cost_price,
                'total': order.total,
            }
            orders_list.append(vals)
        return{
            'doc_model': 'purchase.order.test',
            'docs': docs,
            'data': data,
            'orders_list': orders_list
        }