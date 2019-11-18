# -*- coding: utf-8 -*-
{
    'name': 'Información hospitalaria',
    'version': '1.0',
    'category': 'Finanzas',
    'description': 'Modulo de gestión de hospital',
    'author': 'José Miguel Fernández Serrano',
    'website': 'http://www.iesayala.com',
    'depends': ['base'],
    'data': [
        'views/partner_view.xml',
        'views/hospital_view.xml',
        'views/especialidades_view.xml',
        'views/consultas_view.xml',
        'views/medicos_view.xml',
    ],
    'application': True,
    'installable': True,
}