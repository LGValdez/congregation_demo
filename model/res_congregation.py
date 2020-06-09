# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResCongregation(models.Model):
    _name = "res.congregation"
    _description = "Congregations"
    _rec_name = "name"

    name = fields.Char(string='Name', required=True)
    city = fields.Char(string='City')
    country = fields.Char(string='Country')
    congregation_id  = fields.Many2one('res.congregation', string='Is part of')
    congregation_lines = fields.One2many(string='Congregations', 
                                         comodel_name='res.congregation',
                                         inverse_name='congregation_id')
    partner_lines = fields.One2many(string='Partners', 
                                    comodel_name='congregation.partner',
                                    inverse_name='congregation_id')
    proyect_ids = fields.Many2many(string='Ministerial Project',
                                   comodel_name='ministerial.project',
                                   relation='rel_res_congregation_ministerial_project')
