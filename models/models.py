# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

# MODELO AULA

class Aula(models.Model):

    _name = 'lab_equipos.aula' 
    _description = 'Aula del laboratorio de informática'
    _rec_name = 'nombreAula'

    # Atributos
    nombreAula = fields.Char(string='Nombre del aula', required=True)
    capacidadAula = fields.Integer(string='Capacidad máxima (puestos)', required=True)

    equipo_ids = fields.One2many('lab_equipos.equipo', 'aula_id', string='Equipos en el aula')

    @api.constrains('equipo_ids', 'capacidadAula')
    def _check_capacidad_aula(self):
        for aula in self:
            if len(aula.equipo_ids) > aula.capacidadAula:
                raise ValidationError(
                    f"El aula no puede albergar más equipos."
                )


# MODELO SOFTWARE

class Software(models.Model):

    _name = 'lab_equipos.software' 
    _description = 'Software instalado en el equipo'
    _rec_name = 'nombreSoftware'

    # Atributos
    nombreSoftware = fields.Char(string='Nombre del software', required=True)
    versionSoftware = fields.Char(string='Versión del software')
    
    equipo_ids = fields.Many2many('lab_equipos.equipo', string='Equipos con este software')


# MODELO EQUIPO

class Equipo(models.Model):

    _name = 'lab_equipos.equipo' 
    _description = 'Equipo informático del laboratorio'
    _rec_name = 'nombreEquipo'

    # Atributos
    nombreEquipo = fields.Char(string='Nombre del equipo', required=True)
    tipoEquipo = fields.Selection([('Ordenador de escritorio', 'Ordenador de escritorio'), ('Portátil', 'Portátil'), ('Proyector', 'Proyector')], string='Tipo de Equipo', required=True)
    
    # Relaciones entre tablas
    
    aula_id = fields.Many2one('lab_equipos.aula', string='Aula') 
    software_ids = fields.Many2many('lab_equipos.software', string='Software instalado')


# class lab_equipos(models.Model):
#     _name = 'lab_equipos.lab_equipos'
#     _description = 'lab_equipos.lab_equipos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

