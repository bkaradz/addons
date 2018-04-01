from odoo import api, fields, models

class ProductPricelistItemModule(models.Model):
    _inherit = 'product.pricelist.item'

    # This will add emb_min_price field to the product.pricelist.item model
    emb_min_price = fields.Float(string="Min. Price", required=False, )

class ProductPricelistModule(models.Model):
    _inherit = 'product.pricelist'

