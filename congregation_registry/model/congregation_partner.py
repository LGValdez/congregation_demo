# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CongregationPartner(models.Model):
    _name = "congregation.partner"
    _description = "Congregation Partner"
    _rec_name = "name"

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Mail')
    address = fields.Char(string='Address')
    city = fields.Char(string='City')
    country = fields.Char(string='Country')

    ministry_ids = fields.Many2many(string='Ministry',
                                    comodel_name='holy.ministry', 
                                    relation='rel_congregation_partner_holy_ministry')
    gift_ids = fields.Many2many(string='Gift',
                                comodel_name='holy.gift',
                                relation='rel_congregation_partner_holy_gift')

    congregation_id = fields.Many2one('res.congregation', string='Congregation')
    congregation_register_lines = fields.One2many(string='Congregations', 
                                                  comodel_name='participation.registry',
                                                  inverse_name='partner_id',
                                                  domain=[('congregation_id', '!=', False)])

    project_register_lines = fields.One2many(string='Projects', 
                                             comodel_name='participation.registry',
                                             inverse_name='partner_id',
                                             domain=[('project_id', '!=', False)])

    school_register_lines = fields.One2many(string='Schools', 
                                            comodel_name='participation.registry',
                                            inverse_name='partner_id',
                                            domain=[('school_id', '!=', False)])
