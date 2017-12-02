# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Domain(models.Model):
    _name = 'assessment.domain'
    _rec_name = 'name'

    name = fields.Char()
    
class Lesson(models.Model):
    _name = 'assessment.lesson'
    name = fields.Char()

class Test(models.Model):
    _name = 'assessment.test'
    name = fields.Char()

class Domain(models.Model):
    _name = 'assessment.domain'
    name = fields.Char()