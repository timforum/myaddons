# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = " Openacademy Courses"
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', ondelete="set null",
                                     string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session', "course_id", string="Sessions")


class session(models.Model):
    _name = "openacademy.session"
    _description = " OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digital=(6.2), help="duration in days")
    seats = fields.Integer(string="Nuamber of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor")

    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seats = fields.Float(string='Taken Seats', compute='_taken_seats')

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.take_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats


