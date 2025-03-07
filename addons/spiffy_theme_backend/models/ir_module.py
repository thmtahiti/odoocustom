# -*- coding: utf-8 -*-
# Developed by Bizople Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details

from odoo import models, fields, api
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)


class Module(models.Model):
    _inherit = "ir.module.module"

    def next(self):
        """
        Return the action linked to an ir.actions.todo is there exists one that
        should be executed. Otherwise, redirect to /web
        """
        Todos = self.env['ir.actions.todo']
        active_todo = Todos.search([('state', '=', 'open')], limit=1)
        if active_todo:
            return active_todo.action_launch()
        if request.env.user.table_color:
            return {
                'type': 'ir.actions.act_url',
                'target': 'self',
                'url': '/web?bg_color=True&tool_color_id=1',
            }
        else:
            return {
                'type': 'ir.actions.act_url',
                'target': 'self',
                'url': '/web',
            }