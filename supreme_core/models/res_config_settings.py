# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    # Supreme HRMS Settings
    use_employee_code = fields.Boolean(
        string='Auto-generate Employee IDs',
        config_parameter='supreme_hrms.use_employee_code',
        default=True
    )
    
    employee_code_prefix = fields.Char(
        string='Employee ID Prefix',
        config_parameter='supreme_hrms.employee_code_prefix',
        default='EMP'
    )
    
    employee_code_padding = fields.Integer(
        string='Employee ID Padding',
        config_parameter='supreme_hrms.employee_code_padding',
        default=5
    )
    
    track_work_location = fields.Boolean(
        string='Track Work Locations',
        config_parameter='supreme_hrms.track_work_location',
        default=True
    )
    
    enable_emergency_contacts = fields.Boolean(
        string='Emergency Contacts',
        config_parameter='supreme_hrms.enable_emergency_contacts',
        default=True
    )
    
    enable_gps_attendance = fields.Boolean(
        string='GPS Attendance Tracking',
        config_parameter='supreme_hrms.enable_gps_attendance',
        default=False
    )
    
    # MuK Theme Integration
    muk_theme_installed = fields.Boolean(
        string='MuK Theme Installed',
        compute='_compute_muk_theme_installed'
    )
    
    supreme_theme_colors = fields.Boolean(
        string='Use Supreme Colors',
        config_parameter='supreme_hrms.use_supreme_colors',
        default=False
    )
    
    @api.depends('company_id')
    def _compute_muk_theme_installed(self):
        """Check if MuK theme modules are installed"""
        for record in self:
            IrModule = self.env['ir.module.module']
            muk_modules = IrModule.search([
                ('name', 'in', ['muk_web_theme', 'muk_web_appsbar', 'muk_web_chatter']),
                ('state', '=', 'installed')
            ])
            record.muk_theme_installed = bool(muk_modules)
    
    @api.model
    def get_values(self):
        res = super().get_values()
        
        # Check MuK theme compatibility
        if self.muk_theme_installed:
            # Apply MuK-specific settings
            res.update({
                'muk_compatible_mode': True,
            })
        
        return res
    
    def set_values(self):
        super().set_values()
        
        # Apply Supreme colors to MuK theme if enabled
        if self.supreme_theme_colors and self.muk_theme_installed:
            self._apply_supreme_colors_to_muk()
    
    def _apply_supreme_colors_to_muk(self):
        """Apply Supreme HRMS colors to MuK theme"""
        # Supreme Stack brand colors
        supreme_colors = {
            'color_brand_light': '#2C3E50',  # Dark blue-gray
            'color_primary_light': '#3498DB',  # Bright blue
            'color_success_light': '#27AE60',  # Green
            'color_info_light': '#2980B9',  # Blue
            'color_warning_light': '#F39C12',  # Orange
            'color_danger_light': '#E74C3C',  # Red
        }
        
        # Check if MuK color settings exist
        if hasattr(self, 'color_brand_light'):
            for field, color in supreme_colors.items():
                if hasattr(self, field):
                    setattr(self, field, color)
