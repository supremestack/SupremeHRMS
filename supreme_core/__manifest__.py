{
    'name': 'Supreme HRMS Core',
    'version': '18.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Core HRMS extensions and configurations for Supreme Stack Systems',
    'description': """
Supreme HRMS Core Module
========================

This module provides core HR management extensions including:
* Enhanced employee records with additional fields
* Employee ID generation and management
* Emergency contact information
* Banking details management
* GPS-based attendance tracking support
* Multi-company configuration

Developed by Supreme Stack Systems Limited
Website: www.supremestack.net
    """,
    'author': 'Supreme Stack Systems Limited',
    'website': 'https://www.supremestack.net',
    'license': 'LGPL-3',
    'depends': [
        'hr',
        'hr_attendance',
        'hr_holidays',
        'hr_expense',
        'hr_recruitment',
        'hr_contract',
        'hr_skills',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'security/hr_security.xml',
        'security/ir.model.access.csv',
        'data/hr_sequence.xml',
        'views/hr_employee_views.xml',
        'views/res_config_settings_views.xml',
        'views/menu_items.xml',
    ],
    'demo': [
        'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
}
