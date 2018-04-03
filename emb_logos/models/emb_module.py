from odoo import api, fields, models

class ProducTemplateModule(models.Model):
    _inherit = 'product.template'

    # This will add all the field bellow to the product.template model
    x_stitches = fields.Integer(string="Stitches", required=False, )
    x_length = fields.Integer(string="Length", required=False, )
    x_width = fields.Integer(string="Width", required=False, )
    x_colours = fields.Integer(string="Colours", required=False, )
    x_colours_changes = fields.Integer(string="Colour Changes", required=False, )

class ProductsPricelistModule(models.Model):
    _inherit = 'product.pricelist'

    # This method will be called when the field Stitches changes on the product form.
    # It will calculate the unit price and update it, based on the Stitches
    @api.onchange('x_stitches', 'emb_price_max_unit')
    def change_price(self):
        import pdb
        total_amount = (self.x_stitches/ float(1000)) * 0.24
        if total_amount >= 0.75:
            self.list_price = total_amount
        else:
            self.list_price = 0.75