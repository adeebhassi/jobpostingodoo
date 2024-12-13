from odoo import models , api ,fields , _

class RefuseresonWizard(models.TransientModel):
    _name = 'refuse.reason.wizard'
    _description = 'Class Refusereason Wizard'

    refuse_reason = fields.Char(string="Refuse Reason")
    