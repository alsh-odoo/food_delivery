# -*- coding: utf-8 -*-

from odoo import models,fields

class restaurant(models.Model):
    _name="restaurant.name"
    _description="This module is about the names of restaurants avilable in our nearest cities"
    _order = "name"


    name=fields.Char(string="name",required=True)
    pincode=fields.Char(string="Pincode")
    city=fields.Char(string="City")
    state_id=fields.Char(string="State")
    restaurant_type=fields.Selection(
        string="Restaurant Type",
        selection=[('pure_veg','Pure Veg'),('veg_non_veg','Veg&Nonveg')]
    )
    cusine_type_ids=fields.Many2many('cusine.style',string="Cusine")
    restaurant_menu_ids=fields.One2many('food.product','restaurant_id',string="Menu Items")
    