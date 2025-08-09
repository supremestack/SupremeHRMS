# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime, timedelta

class HrDashboard(models.Model):
    _name = 'hr.dashboard'
    _description = 'HR Dashboard'
    
    @api.model
    def get_dashboard_data(self):
        """Get dashboard metrics"""
        data = {}
        Employee = self.env['hr.employee']
        
        # Basic metrics
        data['total_employees'] = Employee.search_count([])
        data['active_employees'] = Employee.search_count([('active', '=', True)])
        
        # Attendance today
        today = fields.Date.today()
        Attendance = self.env['hr.attendance']
        data['present_today'] = Attendance.search_count([
            ('check_in', '>=', datetime.combine(today, datetime.min.time()))
        ])
        
        # On leave
        Leave = self.env['hr.leave']
        data['on_leave'] = Leave.search_count([
            ('state', '=', 'validate'),
            ('date_from', '<=', today),
            ('date_to', '>=', today)
        ])
        
        return data
