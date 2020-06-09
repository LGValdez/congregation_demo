# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SchoolProgram(models.Model):
    _name = "school.program"
    _description = "School Program"
    _rec_name = "name"

    name = fields.Char(string='Name', required=True)
    date_start = fields.Date(string='Start Date')
    date_end = fields.Date(string='End Date')
    city = fields.Char(string='City')
    country = fields.Char(string='Country')
    summary = fields.Text(string='Summary')
    webpage = fields.Char(string='Webpage')
    ongoing = fields.Boolean(string='Ongoing')
