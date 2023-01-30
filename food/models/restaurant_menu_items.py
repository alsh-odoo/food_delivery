# -*- coding: utf-8 -*-
from odoo import models,fields,api,_

class menuItems(models.Model):
    _name="restaurant.menu.items"
    _description="This model is used to connect with restaurant model to describe the menu items of that specific restaurant"

    item_name=fields.Char(string="Food Item Name",required=True)
    price=fields.Float(string="Price",required=True)
    menu_item_id=fields.Many2one('restaurant.name')
