from odoo import api, models


class Meeting(models.Model):
    """ Check from appraisal and update meeting_id"""
    _inherit = 'calendar.event'

    @api.model
    def create(self, values):
        """ Add meeting_id in appraisal """
        appraisal = False
        if self.env.context.get('active_model', False) == 'hr.appraisal':
            appraisal = self.env['hr.appraisal'].browse(self.env.context.get('active_id'))
        meeting = super(Meeting, self).create(values)
        if appraisal:
            # add employee of the appraisal
            if appraisal.emp_id.user_id:
                meeting['partner_ids'] = [(4, appraisal.emp_id.user_id[0].partner_id.id)]

            appraisal.write(
                {'meeting_id': meeting.id,
                 'date_next_meeting': meeting.start}
            )
        return meeting

    @api.multi
    def write(self, values):
        """ Modify start meeting in appraisals """
        start = values.get('start', False)
        if start:
            appraisals = self.env['hr.appraisal'].search([('meeting_id', 'in', self.ids)])
            if appraisals:
                appraisals.write({
                    'date_next_meeting': start
                })
        return super(Meeting, self).write(values)

    @api.multi
    def unlink(self):
        """ clean meeting_id appraisal """
        appraisals = self.env['hr.appraisal'].search([('meeting_id', 'in', self.ids)])
        out = super(Meeting, self).unlink()
        if appraisals:
            # if not error, clean appraisals
            appraisals.write({
                'meeting_id': False,
                'date_next_meeting': False
            })
        return out
