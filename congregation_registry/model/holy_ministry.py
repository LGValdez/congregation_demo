# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class HolyMinistry(models.Model):
    _name = "holy.ministry"
    _description = "Holy Spirit Ministry"
    _rec_name = "name"

    name = fields.Char(string='Name', required=True, translate=True)
