{
    'name': 'Interlogistica Partner Requirements',
    'version': '18.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Hace obligatorios los campos de teléfono, dirección, nombre y apellido en contactos.',
    'description': """
        Este módulo asegura que al crear o editar un contacto (res.partner) que sea individuo,
        se completen obligatoriamente los campos:
        - Nombre y Apellido (usando partner_firstname)
        - Teléfono
        - Dirección (Calle)
    """,
    'author': 'DevOpsMBAConsultings',
    'depends': ['base', 'partner_firstname', 'sales_team'],
    'data': [
        'security/security_rules.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
