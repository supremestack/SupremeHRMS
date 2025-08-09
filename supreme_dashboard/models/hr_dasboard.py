# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime, timedelta

class HrDashboard(models.Model):
    _name = 'hr.dashboard'
    _description = 'HR Dashboard'
    _auto = False  # This is a virtual model for dashboard data
    
    @api.model
    def get_dashboard_data(self):
        """Get comprehensive dashboard metrics"""
        Employee = self.env['hr.employee']
        Attendance = self.env['hr.attendance']
        Leave = self.env['hr.leave']
        
        today = fields.Date.today()
        first_day_of_month = today.replace(day=1)
        
        # Basic metrics
        data = {
            'total_employees': Employee.search_count([('active', '=', True)]),
            'departments': [],
            'work_locations': [],
            'gender_distribution': [],
            'recent_joiners': [],
            'attendance_trend': [],
            'leave_trend': [],
        }
        
        # Present today
        data['present_today'] = Attendance.search_count([
            ('check_in', '>=', datetime.combine(today, datetime.min.time())),
            ('check_in', '<=', datetime.combine(today, datetime.max.time()))
        ])
        
        # On leave today
        data['on_leave'] = Leave.search_count([
            ('state', '=', 'validate'),
            ('date_from', '<=', today),
            ('date_to', '>=', today)
        ])
        
        # Pending leave requests
        data['pending_leaves'] = Leave.search_count([
            ('state', 'in', ['confirm', 'validate1'])
        ])
        
        # New joiners this month
        data['new_joiners'] = Employee.search_count([
            ('create_date', '>=', first_day_of_month),
            ('active', '=', True)
        ])
        
        # Department distribution
        dept_data = Employee.read_group(
            [('active', '=', True)],
            ['department_id'],
            ['department_id']
        )
        data['departments'] = [{
            'name': d['department_id'][1] if d['department_id'] else 'Unassigned',
            'count': d['department_id_count']
        } for d in dept_data]
        
        # Work location distribution
        if 'work_location_type' in Employee._fields:
            location_data = Employee.read_group(
                [('active', '=', True)],
                ['work_location_type'],
                ['work_location_type']
            )
            data['work_locations'] = [{
                'type': l['work_location_type'] or 'unspecified',
                'count': l['work_location_type_count'],
                'label': dict(Employee._fields['work_location_type'].selection).get(
                    l['work_location_type'], 'Unspecified'),
                'icon': self._get_location_icon(l['work_location_type']),
                'color': self._get_location_color(l['work_location_type'])
            } for l in location_data]
        
        # Gender distribution
        gender_data = Employee.read_group(
            [('active', '=', True)],
            ['gender'],
            ['gender']
        )
        data['gender_distribution'] = [{
            'gender': g['gender'] or 'other',
            'count': g['gender_count'],
            'label': dict(Employee._fields['gender'].selection).get(
                g['gender'], 'Not Specified') if g['gender'] else 'Not Specified'
        } for g in gender_data]
        
        # Recent joiners (last 5)
        recent_employees = Employee.search_read(
            [('active', '=', True)],
            ['name', 'job_id', 'department_id', 'work_email', 'create_date'],
            limit=5,
            order='create_date desc'
        )
        data['recent_joiners'] = [{
            'id': e['id'],
            'name': e['name'],
            'job_title': e['job_id'][1] if e['job_id'] else 'Not Assigned',
            'department': e['department_id'][1] if e['department_id'] else 'Not Assigned',
            'email': e['work_email'] or '',
            'join_date': e['create_date'].strftime('%Y-%m-%d') if e['create_date'] else ''
        } for e in recent_employees]
        
        # Attendance trend (last 30 days)
        data['attendance_trend'] = self.get_attendance_trend(30)
        
        # Leave trend (last 6 months)
        data['leave_trend'] = self.get_leave_trend(6)
        
        return data
    
    @api.model
    def get_attendance_trend(self, days=30):
        """Get attendance trend for last n days"""
        end_date = fields.Date.today()
        start_date = end_date - timedelta(days=days)
        
        # Use raw SQL for performance
        query = """
            SELECT 
                DATE(check_in) as date,
                COUNT(DISTINCT employee_id) as present_count
            FROM hr_attendance
            WHERE DATE(check_in) >= %s AND DATE(check_in) <= %s
            GROUP BY DATE(check_in)
            ORDER BY date
        """
        
        self.env.cr.execute(query, (start_date, end_date))
        results = self.env.cr.dictfetchall()
        
        # Fill in missing dates with zero
        date_range = [start_date + timedelta(days=x) for x in range(days + 1)]
        attendance_dict = {r['date']: r['present_count'] for r in results}
        
        return [{
            'date': d.strftime('%Y-%m-%d'),
            'present': attendance_dict.get(d, 0)
        } for d in date_range]
    
    @api.model
    def get_leave_trend(self, months=6):
        """Get leave trend for last n months"""
        end_date = fields.Date.today()
        start_date = end_date - timedelta(days=months * 30)
        
        query = """
            SELECT 
                TO_CHAR(date_from, 'YYYY-MM') as month,
                COUNT(*) as leave_count,
                SUM(number_of_days) as total_days
            FROM hr_leave
            WHERE state = 'validate'
                AND date_from >= %s 
                AND date_from <= %s
            GROUP BY TO_CHAR(date_from, 'YYYY-MM')
            ORDER BY month
        """
        
        self.env.cr.execute(query, (start_date, end_date))
        return self.env.cr.dictfetchall()
    
    @api.model
    def _get_location_icon(self, location_type):
        """Get icon for work location type"""
        icons = {
            'office': 'fa-building',
            'home': 'fa-home',
            'hybrid': 'fa-sync',
            'field': 'fa-map-marker',
        }
        return icons.get(location_type, 'fa-question-circle')
    
    @api.model
    def _get_location_color(self, location_type):
        """Get color class for work location type"""
        colors = {
            'office': 'text-info',
            'home': 'text-success',
            'hybrid': 'text-warning',
            'field': 'text-primary',
        }
        return colors.get(location_type, 'text-muted')
