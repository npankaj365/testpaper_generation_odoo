# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random
import logging

_logger = logging.getLogger(__name__)

class Topic(models.AbstractModel):
    '''Abstract Class for Different Topics to be kept in the Question Bank'''
    _name = 'assessment.topic'
    _rec_name = 'name'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    enabled = fields.Boolean(string="Enabled")

class Domain(models.Model):
    '''Class for the Domains to be kept in the Question Bank'''
    _name = 'assessment.domain'
    _inherit = 'assessment.topic'

    subdomain = fields.One2many('assessment.subdomain', 'domain')

class Subdomain(models.Model):
    '''Class for the SubDomains to be kept in the Question Bank'''
    _name = 'assessment.subdomain'
    _inherit = 'assessment.topic'

    domain = fields.Many2one('assessment.domain', 'domain')
    lesson = fields.One2many('assessment.lesson', 'subdomain')

class Lesson(models.Model):
    '''Class for the Lessons to be kept in the Question Bank'''
    _name = 'assessment.lesson'
    _inherit = 'assessment.topic'
    
    domain = fields.Many2one('assessment.domain', 'domain')
    subdomain = fields.Many2one('assessment.subdomain', 'subdomain', domain="[('domain','=',domain)]")
    objective = fields.One2many('assessment.objective', 'lesson')
    rubric = fields.One2many('assessment.rubric', 'lesson')

class Objective(models.Model):
    '''Class for the Learning Objectives to be kept in the Question Bank'''
    _name = 'assessment.objective'
    _inherit = 'assessment.topic'
    
    domain = fields.Many2one('assessment.domain', 'domain')
    subdomain = fields.Many2one('assessment.subdomain', 'subdomain', domain="[('domain','=',domain)]")
    lesson = fields.Many2one('assessment.lesson', 'Lesson', domain="[('subdomain','=',subdomain)]", required=True)
    question = fields.One2many('assessment.question', 'objective')
    rubric = fields.Many2one('assessment.rubric', 'rubric')

class Question(models.Model):
    '''Class for the Questions to be kept in the Question Bank'''
    _name = 'assessment.question'
    _rec_name = 'statement'

    statement = fields.Text()
    
    question_type = fields.Selection(
        [
            ('mcsa','Multiple Choice Single Answer'), 
            ('mcma','Multiple Choice Multiple Answer'), 
            ('num','Numerical Value'), 
            ('fa','Free Answer')
        ], required=True, default='mcsa'
    )
    
    answer_choice_a = fields.Char()
    answer_choice_b = fields.Char()
    answer_choice_c = fields.Char()
    answer_choice_d = fields.Char()

    time_required = fields.Integer()
    enabled = fields.Boolean()
    correct_choices = fields.Char(help='If multiple answers, separate each by comma')
    domain = fields.Many2one('assessment.domain', 'domain')
    subdomain = fields.Many2one('assessment.subdomain', 'subdomain', domain="[('domain','=',domain)]")
    lesson = fields.Many2one('assessment.lesson', 'lesson', domain="[('subdomain','=',subdomain)]", required=True)
    objective = fields.Many2one('assessment.objective', 'objective', domain="[('lesson','=',lesson)]")


class Rubric(models.Model):
    '''Class for the Rubrics to be kept in the Question Bank'''
    _name = 'assessment.rubric'
    # _rec_name = 'title'

    # title = fields.Char()
    lesson = fields.Many2one('assessment.lesson', 'Lesson')
    objective = fields.Many2one('assessment.objective', 'Objective', required=True)
    grade_a = fields.Char()
    grade_b = fields.Char()
    grade_c = fields.Char()
    grade_d = fields.Char()
    grade_e = fields.Char()
    
class TestSection(models.Model):
    _name = 'assessment.testsection'
    _rec_name = 'title'
    title = fields.Char()
    lesson = fields.Many2many('assessment.lesson', 'lesson', required=True)
    question_type = fields.Selection(
        [
            ('mcsa','Multiple Choice Single Answer'), 
            ('mcma','Multiple Choice Multiple Answer'), 
            ('num','Numerical Value'), 
            ('fa','Free Answer')
        ], required=True, default='mcsa'
    )
    test = fields.Many2one('assessment.test', 'test')
    duration = fields.Integer(string="Test Section Duration")
    no_of_question = fields.Integer(string="No. of Questions")
    gen_question_list = {}

class Test(models.Model):
    _name = 'assessment.test'
    _rec_name = 'title'
    title = fields.Char(string="Section")
    subtext = fields.Html(string="Header Content")
    test_section = fields.One2many('assessment.testsection', 'test')

    @api.multi
    def generate(self):
        for section in self.test_section:
            time_left = section.duration
            for lesson in section.lesson:
                for objective in lesson.objective:
                    for question in objective.question:
                        if (question.question_type == section.question_type and time_left > question.time_required):
                            section.gen_question_list[question] = section.title
                            time_left -= question.time_required
            keys = list(section.gen_question_list.keys())
            random.shuffle(keys)
            section.gen_question_list = [(key, section.gen_question_list[key]) for key in keys]

    def clear(self):
        for section in self.test_section:
            section.gen_question_list.clear()
