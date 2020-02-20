# -*- coding: utf-8 -*-

from odoo import models, fields


class mod1a(models.Model):
    _name = 'mod1a.mod1a'
    _description = 'mod1a.mod1a'

    nombre = fields.Char()
    apellido = fields.Char()
    numero de id = fields.Integer()
    valor = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
