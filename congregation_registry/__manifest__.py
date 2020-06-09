# -*- coding: utf-8 -*-
{
    'name' : 'Congregation Registry',
    'version' : '1.0.0',
    'summary' : 'Congregation Registry',
    'description' : """
Congregation Registry
====================
    """,
    'category' : 'Congregation Organization',
    'depends'  : [],
    'data' : [
        'security/congregation_registry_security.xml',
        'security/ir.model.access.csv',
        'view/holy_gift.xml',
        'view/holy_ministry.xml',
        'view/holy_gift.xml',
        'view/ministerial_project.xml',
        'view/res_congregation.xml',
        'view/school_program.xml',
        'view/congregation_partner.xml',
        'view/congregation_registry_menus.xml',
    ],
    'installable'  : True,
    'application'  : True,
    'auto_install' : False,
}
