# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class MinisterialProject(models.Model):
    _name = "ministerial.project"
    _description = "Ministerial Project"
    _rec_name = "name"

    name = fields.Char(string='Name', required=True)
    origin_id = fields.Many2one('res.congregation', string='Original Congregation')
