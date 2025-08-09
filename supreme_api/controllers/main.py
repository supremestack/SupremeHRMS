# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class SupremeAPI(http.Controller):
    
    @http.route('/api/v1/employee/profile', 
                type='json', auth='user', methods=['GET'])
    def get_employee_profile(self, **kwargs):
        """Get current employee profile"""
        employee = request.env.user.employee_id
        if not employee:
            return {'status': 'error', 'message': 'No employee linked'}
        
        return {
            'status': 'success',
            'data': {
                'id': employee.id,
                'name': employee.name,
                'employee_code': employee.employee_code,
                'department': employee.department_id.name,
                'job_title': employee.job_id.name,
            }
        }
    
    @http.route('/api/v1/attendance/checkin', 
                type='json', auth='user', methods=['POST'])
    def attendance_checkin(self, **kwargs):
        """Clock in"""
        employee = request.env.user.employee_id
        if not employee:
            return {'status': 'error', 'message': 'No employee linked'}
        
        attendance = request.env['hr.attendance'].create({
            'employee_id': employee.id,
        })
        
        return {
            'status': 'success',
            'attendance_id': attendance.id,
        }
