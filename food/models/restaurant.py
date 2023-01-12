# -*- coding: utf-8 -*-

from odoo import models,fields

class restaurant(models.Model):
    _name="restaurant.name"
    _description="This module is about the names of restaurants"
    _order = "name"


    name=fields.Char(required=True)
    pincode=fields.Char()
    city=fields.Char()
    state=fields.Char()
    restaurant_type=fields.Selection(
        string="Restaurant Type",
        selection=[('pure_veg','Pure Veg'),('veg_non_veg','Veg&Nonveg')]
    )
    restaurant__menu_ids=fields.One2many('restaurant.menu.items','menu_item_id',string="Menu Items")
    restaurant_menu_id = fields.Many2one('food.delivery',string="Restaurant Menu")
    