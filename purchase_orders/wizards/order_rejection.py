
from odoo import fields, models, api


class RejectionOrder(models.TransientModel):
    _name = 'rejection.order'

    order_id = fields.Many2one('purchase.order.test', string="Order ID")
    reject_reason = fields.Text(string="Reject Reason", required=True)

    @api.multi
    def reject_order(self):
        for rec in self.env['purchase.order.test'].browse(self._context.get('active_ids', [])):
            print("record", rec)
            rec.reject_reason = self.reject_reason
            rec.state = 'reject'
            print("state", rec.state)
        print("Rejected")
