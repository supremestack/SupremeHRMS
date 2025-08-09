# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ApiLog(models.Model):
    _name = 'api.log'
    _description = 'API Request Log'
    _order = 'create_date desc'
    _rec_name = 'endpoint'
    
    endpoint = fields.Char('API Endpoint', required=True)
    method = fields.Selection([
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
        ('PATCH', 'PATCH'),
    ], string='HTTP Method', required=True)
    
    user_id = fields.Many2one('res.users', 'User', required=True)
    employee_id = fields.Many2one('hr.employee', 'Employee')
    
    request_data = fields.Text('Request Data')
    response_data = fields.Text('Response Data')
    
    status_code = fields.Integer('Status Code')
    success = fields.Boolean('Success')
    error_message = fields.Text('Error Message')
    
    execution_time = fields.Float('Execution Time (ms)')
    ip_address = fields.Char('IP Address')
    user_agent = fields.Text('User Agent')
    
    @api.model
    def log_request(self, endpoint, method, request_data=None, response_data=None, 
                    status_code=200, success=True, error_message=None, 
                    execution_time=0, ip_address=None, user_agent=None):
        """Create API log entry"""
        return self.create({
            'endpoint': endpoint,
            'method': method,
            'user_id': self.env.user.id,
            'employee_id': self.env.user.employee_id.id if self.env.user.employee_id else False,
            'request_data': str(request_data) if request_data else False,
            'response_data': str(response_data) if response_data else False,
            'status_code': status_code,
            'success': success,
            'error_message': error_message,
            'execution_time': execution_time,
            'ip_address': ip_address,
            'user_agent': user_agent,
        })
    
    @api.model
    def clean_old_logs(self, days=30):
        """Clean logs older than specified days"""
        from datetime import datetime, timedelta
        cutoff_date = datetime.now() - timedelta(days=days)
        old_logs = self.search([('create_date', '<', cutoff_date)])
        old_logs.unlink()
        return len(old_logs)
