# -*- coding: utf-8 -*-
# from odoo import http


# class LabEquipos(http.Controller):
#     @http.route('/lab_equipos/lab_equipos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lab_equipos/lab_equipos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lab_equipos.listing', {
#             'root': '/lab_equipos/lab_equipos',
#             'objects': http.request.env['lab_equipos.lab_equipos'].search([]),
#         })

#     @http.route('/lab_equipos/lab_equipos/objects/<model("lab_equipos.lab_equipos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lab_equipos.object', {
#             'object': obj
#         })

