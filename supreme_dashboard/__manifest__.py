{
    'name': 'Supreme HRMS Dashboard',
    'version': '18.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'HR Analytics Dashboard',
    'author': 'Supreme Stack Systems Limited',
    'website': 'https://www.supremestack.net',
    'license': 'LGPL-3',
    'depends': [
        'supreme_core',
        'hr',
        'hr_attendance',
        'hr_holidays',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/dashboard_views.xml',
    ],
    'installable': True,
    'application': False,
}
