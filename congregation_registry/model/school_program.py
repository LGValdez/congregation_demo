# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import Warning


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
    meeting = fields.Char(string='Meeting')
    ongoing = fields.Boolean(string='Ongoing')

    school_lines = fields.One2many(string='Sessions', 
                                   comodel_name='school.program.line',
                                   inverse_name='school_id')

    @staticmethod
    def open_external_link(url):
        return {
                'type': 'ir.actions.act_url',
                'url': url,
                'target': 'new',
            }

    def open_webpage(self):
        if not self.webpage:
            raise Warning(_("No %s configured for school.") % _("Webpage"))
        return self.open_external_link(self.webpage)

    def open_meeting(self):
        if not self.meeting:
            raise Warning(_("No %s configured for school.") % _("Meeting"))
        return self.open_external_link(self.meeting)

    def open_all_sessions(self):
        cong_partner = self.env.context.get('congregation_partner')
        partner_program_obj = self.env['partner.program.line']
        for session in self.school_lines:
            program_line_exists = partner_program_obj.search([
                ('partner_id', '=', cong_partner),
                ('session_id', '=', session.id),
            ])
            if not program_line_exists:
                partner_program_obj.create({
                    'partner_id' : cong_partner,
                    'session_id' : session.id,
                    'watched': False
                })
        return {
            'name': self.name + " / " + _('Sessions'),
            'view_mode': 'tree',
            'res_model': 'partner.program.line',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain':[
                ('partner_id', '=', self.env.context.get('congregation_partner')),
                ('session_id', 'in', self.school_lines.ids),
            ],
        }
    
    def validate_latest_session(self, session_attr, message=None):
        message = message or session_attr
        if not self.school_lines:
            raise Warning(_("No %s configured for school.") % _("Sessions"))
        latest_session = min(self.school_lines, key=lambda r: r.sequence)
        if not getattr(latest_session, session_attr):
            raise Warning(_("No %s configured for latest session.") % _(message))
        return getattr(latest_session, session_attr)

    def open_latest_session_video(self):
        video_url = self.validate_latest_session("video")
        return self.open_external_link(video_url)

    def open_latest_session_notes(self):
        notes_url = self.validate_latest_session("notes")
        return self.open_external_link(notes_url)
