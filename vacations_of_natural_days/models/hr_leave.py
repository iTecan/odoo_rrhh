from datetime import datetime, time
from math import ceil
from odoo import models
from odoo.addons.resource.models.resource import float_to_time, HOURS_PER_DAY


class HolidaysRequest(models.Model):
    _inherit = 'hr.leave'

    def _compute_works_days_from_calendar(self, date_from, date_to, employee):
        """
        Get works_days with a calendar. It used if company have leaves with natural days
        :return: days ceil()
        """
        if self.env.user.company_id.vacations_calendar_days:
            return ceil(employee.get_work_days_data(date_from, date_to, calendar=self.env.user.company_id.resource_calendar_id)['days'])

    def _get_number_of_days(self, date_from, date_to, employee_id):
        """ Returns a float equals to the timedelta between two dates given as string."""
        if employee_id:
            employee = self.env['hr.employee'].browse(employee_id)
            """ It used if company have leaves with natural days """
            if self.env.user.company_id.vacations_calendar_days:
                return self._compute_works_days_from_calendar(date_from, date_to, employee)
            # ---------------
            return employee.get_work_days_data(date_from, date_to)['days']

        today_hours = self.env.user.company_id.resource_calendar_id.get_work_hours_count(
            datetime.combine(date_from.date(), time.min),
            datetime.combine(date_from.date(), time.max),
            False)

        return self.env.user.company_id.resource_calendar_id.get_work_hours_count(date_from, date_to) / (today_hours or HOURS_PER_DAY)
