{
    'name': 'it_hr_appraisal_CE',
    'description': 'iTecan - Evaluación de empleados',
    'version': '12.0.1.0.1',
    'summary': 'hr',
    'author': 'Infraestructuras Tecnológicas de Cantabria, S.L.',
    'website': 'https://www.itecan.es',
    'depends': ['calendar', 'hr', 'survey'],
    'application': True,
    'data': [
        'security/hr_appraisal_security.xml',
        'security/ir.model.access.csv',

        'views/calendar_event_views.xml',
        'views/hr_appraisal_views.xml',
        'views/hr_appraisal_survey_form.xml',
        'views/menus.xml',

        'data/hr_appraisal_stages.xml'
    ],
    'demo': [
        'data/hr_appraisal_demo.xml'
    ]
}
