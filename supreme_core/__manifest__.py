{
    'name': 'Supreme HRMS Core',
    'version': '18.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Core HRMS with MuK Theme Integration',
    'description': """
Supreme HRMS Core Module
========================

Fully compatible with MuK Backend Theme modules.

Features:
* Enhanced employee records
* MuK theme responsive design
* Sidebar navigation support
* Chatter position compatibility
* Color theme integration
    """,
    'author': 'Supreme Stack Systems Limited',
    'website': 'https://www.supremestack.net',
    'license': 'LGPL-3',
    'depends': [
        # Core Odoo modules
        'hr',
        'hr_attendance', 
        'hr_holidays',
        'hr_expense',
        'hr_recruitment',
        'hr_contract',
        'hr_skills',
        
        # MuK Theme modules (optional but recommended)
        'muk_web_theme',  # Main theme - mark as optional
    ],
    'data': [
        'security/hr_security.xml',
        'security/ir.model.access.csv',
        'data/hr_sequence.xml',
        'views/hr_employee_views.xml',
        'views/hr_dashboard_views.xml',
        'views/res_config_settings_views.xml',
        'views/menu_items.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'supreme_core/static/src/scss/supreme_theme.scss',
            'supreme_core/static/src/js/supreme_core.js',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    # MuK Theme Compatibility
    'muk_theme_compatible': True,
    'external_dependencies': {
        'python': [],
    },
}
