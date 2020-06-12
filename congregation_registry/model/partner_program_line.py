# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import Warning


class PartnerProgramLine(models.Model):
    _name = "partner.program.line"
    _description = "Partner Program Line"
    _rec_name = "name"
    _order = "sequence asc"

    partner_id = fields.Many2one('congregation.partner', required=True)
    session_id = fields.Many2one('school.program.line', required=True)

    sequence = fields.Integer(related='session_id.sequence', index=True, store=True)
    name = fields.Char(related='session_id.name')
    watched = fields.Boolean(string="Already Watched")

    @staticmethod
    def open_external_link(url):
        return {
                'type': 'ir.actions.act_url',
                'url': url,
                'target': 'new',
            }

    def open_video(self):
        if not self.session_id.video:
            raise Warning(_("No %s configured for session.") % _("Video"))
        return self.open_external_link(self.session_id.video)

    def open_notes(self):
        if not self.session_id.notes:
            raise Warning(_("No %s configured for session.") % _("Notes"))
        return self.open_external_link(self.session_id.notes)
    
    def change_watch_state(self):
        self.watched = not self.watched
