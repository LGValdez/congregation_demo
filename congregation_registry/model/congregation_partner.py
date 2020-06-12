# -*- coding: utf-8 -*-

from base64 import b64encode

from odoo import api, fields, models, _
from odoo.modules.module import get_module_resource


class CongregationPartner(models.Model):
    _name = "congregation.partner"
    _description = "Congregation Partner"
    _rec_name = "name"

    @api.model
    def _default_image(self):
        image_path = get_module_resource('congregation_registry', 
                                         'static/src/img', 
                                         'default_avatar.png')
        return b64encode(open(image_path, 'rb').read())

    name = fields.Char(string='Name', required=True)
    avatar = fields.Image(default=_default_image, max_width=128, max_height=128, store=True)
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

    @api.onchange('congregation_register_lines')
    def _get_most_recent_congregation(self):
        for partner in self:
            congregation_registers = sorted(partner.congregation_register_lines, 
                                            key=lambda r: r.date_start)
            if congregation_registers:
                partner.congregation_id = congregation_registers[-1].congregation_id.id
            else:
                partner.congregation_id = False

    def button_ongoing_schools(self):
        return {
            'name': _('Ongoing Schools'),
            'view_mode': 'kanban',
            'res_model': 'school.program',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', [r.school_id.id for r in self.school_register_lines if r.school_id.ongoing])],
            'context': {
                'delete': False, 
                'create': False, 
                'edit': False, 
                'import': False, 
                'congregation_partner': self.id},
        }
