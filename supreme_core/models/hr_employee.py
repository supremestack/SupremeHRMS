# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    
    # Identification
    employee_code = fields.Char(
        string='Employee ID',
        required=True,
        copy=False,
        index=True,
        readonly=True,
        default=lambda self: _('New'),
        help="Unique employee identification code"
    )
    
    # Personal Information
    blood_group = fields.Selection([
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ], string='Blood Group')
    
    # Emergency Contact
    emergency_contact_name = fields.Char('Emergency Contact Name')
    emergency_contact_phone = fields.Char('Emergency Phone')
    emergency_contact_relation = fields.Char('Relationship')
    
    # Banking Information
    bank_account_number = fields.Char('Bank Account Number')
    bank_name = fields.Char('Bank Name')
    bank_branch = fields.Char('Bank Branch')
    bank_ifsc = fields.Char('IFSC/SWIFT Code')
    
    # Work Location
    work_location_type = fields.Selection([
        ('office', 'Office'),
        ('home', 'Work from Home'),
        ('hybrid', 'Hybrid'),
        ('field', 'Field'),
    ], string='Work Location Type', default='office')
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('employee_code', _('New')) == _('New'):
                vals['employee_code'] = self.env['ir.sequence'].next_by_code(
                    'hr.employee.code') or _('New')
        return super().create(vals_list)
    
    _sql_constraints = [
        ('employee_code_unique', 'UNIQUE(employee_code)',
         'Employee ID must be unique!'),
    ]
