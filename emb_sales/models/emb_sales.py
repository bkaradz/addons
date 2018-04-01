from odoo import api, fields, models

class SaleOrderLineModel(models.Model):
    _inherit = 'sale.order.line'

    # This will add all the x_stitches to the sales order line model
    x_stitches = fields.Integer(related='product_id.product_tmpl_id.x_stitches', string='Stitches', store=True, readonly=False)
