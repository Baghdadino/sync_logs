from odoo import models, fields, api, exceptions


class SyncLogs(models.Model):
    _inherit = 'audit.log'

    action = fields.Char('Action', readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('method') == 'create':
            vals.update({'action': 'NEW'})
        else:
            vals.update({'action': 'REFORM'})
        return super(SyncLogs, self).create(vals)
