# -*- coding: utf-8 -*-
{
    'name': "manajemen_aset",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'auth_signup'
    ],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/auth_signup_inherit.xml',
        'views/templates.xml',
        'report/laporan_aset.xml',
        'report/laporan_member.xml',
        'report/laporan_pengadaan.xml',
        'report/laporan_peminjaman.xml',
        'report/laporan_inventaris.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}