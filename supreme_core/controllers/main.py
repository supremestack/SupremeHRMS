# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class SupremeHRMSController(http.Controller):
    """Main controller for Supreme HRMS Core"""
    
    @http.route('/supreme/info', type='json', auth='user')
    def get_info(self, **kwargs):
        """Get Supreme HRMS information"""
        return {
            'version': '18.0.1.0.0',
            'modules': ['supreme_core', 'supreme_dashboard', 'supreme_api'],
            'muk_compatible': True,
        }
