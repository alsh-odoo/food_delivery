# -*- coding: utf-8 -*-

from odoo import models,fields

class restaurant(models.Model):
    _name="restaurant.name"
    _description="This module is about the names of restaurants avilable in our nearest cities"
    _order = "name"

    partner_id=fields.Many2one('res.partner',string="Restaurant",required=True)
    name=fields.Char(string="Name",related="partner_id.name",readonly=False)
    pincode=fields.Char(string="Pincode",related="partner_id.zip",readonly=False)
    city=fields.Char(related="partner_id.city",readonly=False)
    state_id=fields.Many2one("res.country.state",related="partner_id.state_id",readonly=False)
    country_id=fields.Many2one("res.country",related="partner_id.country_id",readonly=False)
    restaurant_type=fields.Selection(
        string="Restaurant Type",
        selection=[('pure_veg','Pure Veg'),('veg_non_veg','Veg&Nonveg')]
    )
    cusine_type_ids=fields.Many2many('cusine.style',string="Cusine Type")
    # restaurant_menu_ids=fields.One2many('food.product','restaurant_id',string="Menu Items")
    