from odoo import api, fields, models

class ResPartnerInharited(models.Model):
    _inherit = 'res.partner'

    # This will add x_vat field to the res.partner model
    x_vat = fields.Char(string="VAT")


