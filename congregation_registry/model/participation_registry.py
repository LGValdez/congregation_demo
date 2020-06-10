# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ParticipationRegistry(models.Model):
    _name = "participation.registry"
    _description = "Participation Registry"

    partner_id = fields.Many2one('congregation.partner', string='Partner')
    position = fields.Char(string='Position')
    date_start = fields.Date(string='Start Date')
    date_end = fields.Date(string='End Date')

    congregation_id = fields.Many2one('res.congregation', string='Congregation')

    project_id = fields.Many2one('ministerial.project', string='Project')

    school_id = fields.Many2one('school.program', string='School')
    school_date = fields.Boolean(string='Use School Dates')

    @api.onchange('school_date', 'school_id')
    def _onchange_school_date(self):
        for registry in self:
            registry.date_start = False
            registry.date_end = False
            if registry.school_date and registry.school_id:
                registry.date_start = registry.school_id.date_start
                registry.date_end = registry.school_id.date_end
                
