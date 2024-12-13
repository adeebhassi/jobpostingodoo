from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    job_posting_widget = fields.Boolean(string='Job post settings')
