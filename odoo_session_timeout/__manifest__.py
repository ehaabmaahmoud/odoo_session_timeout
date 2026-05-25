{
    'name': 'Session Timeout Configuration',
    'version': '19.0.1.0.0',
    'author': 'Rawdix',
    'category': 'Technical',
    'summary': 'Configure session timeout duration from Settings',
    'description': """
        Allows system administrators to configure 
        the session timeout duration directly from 
        Odoo General Settings.
    """,
    'depends': ['base_setup'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'license': 'OPL-1',
    'price': 0.0,
    'currency': 'USD',
    'installable': True,
    'application': False,
}
