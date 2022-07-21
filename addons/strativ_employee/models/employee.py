from odoo import fields, models

class Employee(models.Model):
    _name = "strativ.employee"
    _description = "Strativ Employee Information"

    name = fields.Char('Name')
    stack = fields.Selection([
        ('python', 'Python'),
        ('react', 'React'),
    ], string='Tech Stack')
    salary = fields.Float('salary')

    team_id = fields.Many2one('strativ.team', string='team')


class Team(models.Model):
    _name = "strativ.team"
    _description = "Strativ Team"

    name = fields.Char('name')
    employee_ids = fields.One2many('strativ.employee', 'team_id', string='employee')
