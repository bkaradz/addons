from odoo import api, fields, models

class ChangeToMinPrice(models.Model):
    _inherit = ['sale.order.line', 'product.pricelist', 'product.pricelist.item']

    # This method will be called when the field Stitches changes on the product form.
    @api.onchange('price_unit', 'product_uom_qty', )
    def change_unit_price(self):
        if self.price_unit < self.emb_min_price:
            self.price_unit = self.emb_min_price
