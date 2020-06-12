# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SchoolProgramLine(models.Model):
    _name = "school.program.line"
    _description = "School Program Session"
    _rec_name = "name"

    school_id = fields.Many2one('school.program', string= 'School', required=True)

    name = fields.Char(string='Name', required=True)
    video = fields.Char(string='Video')
    notes = fields.Char(string='Notes')
    sequence = fields.Integer(index=True, default=1)
