# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class SupremeDashboardController(http.Controller):
    """Dashboard controller"""
    
    @http.route('/supreme/dashboard/data', type='json', auth='user')
    def get_dashboard_data(self, **kwargs):
        """Get dashboard metrics"""
        return request.env['hr.dashboard'].sudo().get_dashboard_data()
