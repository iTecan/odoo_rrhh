from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    related_partner_id = fields.Many2one('res.partner', compute='_compute_related_partner')

    @api.one
    def _compute_related_partner(self):
        self.related_partner_id = self.user_id.partner_id
