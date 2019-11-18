# -*- coding: utf-8 -*-
from odoo import models, fields

class Medicos(models.Model):
    _name = "sis.medicos"
    nombre = fields.Char(string='Nombre', required=True)
    primer_apellido = fields.Char(string='Primer Apellido', required=True)
    segundo_apellido = fields.Char(string='Segundo Apellido', required=True)
    foto = fields.Binary(string='Foto')
    edad = fields.Integer(string='Edad')
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    genero = fields.Selection([('h', 'Hombre'), ('m', 'Mujer'), ('o', 'Otro')], string='Género')
    nacionalidad = fields.Many2one('res.country', string='Nacionalidad')
    especialidad = fields.Selection([('a','Angiología'),('d','Dermatología'),('g','Ginecología'),('of','Oftalmología'),('ot','Otorrinolaringología'),('u','Urología'),('t','Traumatología')], string='Especialidad')

Medicos()