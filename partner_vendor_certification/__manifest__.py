# Copyright 2019 Eficent <patrickraymondwilson@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Certification',
    'summary': "Adds a certification status to a supplier.",
    'author': "Eficent, Odoo Community Association (OCA)",
    'website': "https://github.com/OCA/partner-contact",
    'category': 'Customer Relationship Management',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'contacts',
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/partner_certification_status.xml',
        'views/res_partner.xml'

    ],
    'development_status': 'Beta',
    'maintainers': ['NuriaMartinXifre'],
}
