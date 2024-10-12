from email.policy import default

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'


    name = fields.Char(required=1, default='New')
    description = fields.Text()
    postcode = fields.Char(required=1)
    date_availability = fields.Date(default=fields.Date.today())
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer(required=1)
    living_areas = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
    ], default='north')

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0 :
                raise ValidationError('Please add a valid umberof bedrooms')



