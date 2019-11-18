# -*- coding: utf-8 -*-
from odoo import models, fields, api

class hospital(models.Model):
	_name = 'sis.hospital'
	nombre = fields.Char('Nombre', size=80, required=True, help='Aqui pones el nombre')
	country_id = fields.Many2one('res.country', 'Country', ondelete='restrict')

hospital();
