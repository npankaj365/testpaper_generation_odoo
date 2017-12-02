# -*- coding: utf-8 -*-
from odoo import http

# class Assessment(http.Controller):
#     @http.route('/assessment/assessment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/assessment/assessment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('assessment.listing', {
#             'root': '/assessment/assessment',
#             'objects': http.request.env['assessment.assessment'].search([]),
#         })

#     @http.route('/assessment/assessment/objects/<model("assessment.assessment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('assessment.object', {
#             'object': obj
#         })