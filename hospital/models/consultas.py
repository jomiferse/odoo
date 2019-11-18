# -*- coding: utf-8 -*-
from odoo import models, fields, api

class consultas(models.Model):
	_name = 'sis.consultas'
	nombre = fields.Char('Nombre', size=80, required=True, help='Aqui pones el nombre')
	partner_id = fields.Many2one('res.partner', 'Paciente', ondelete='restrict')
	especialidades = fields.Many2one('sis.especialidades', 'Especialidad', ondelete='restrict')

consultas();
