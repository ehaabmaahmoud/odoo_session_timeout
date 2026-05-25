from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    session_timeout = fields.Integer(
        string='Session Timeout (minutes)',
        default=60,
        config_parameter='web.session.timeout',
    )
