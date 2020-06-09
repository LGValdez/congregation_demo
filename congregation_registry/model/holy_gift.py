# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class HolyGift(models.Model):
    _name = "holy.gift"
    _description = "Holy Gift Ministry"
    _rec_name = "name"

    name = fields.Char(string='Name', required=True)
