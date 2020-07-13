from odoo import fields, models, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    vacations_calendar_days = fields.Boolean("Vacations as Calendar Days")
