# -*- coding: utf-8 -*-
from odoo import models,fields,api

class foodProduct(models.Model):
    _name="food.product"
    _description="This model is used to create and describe the food product"
    _order="name"

    name=fields.Char(string="Item Name",required=True)
    price=fields.Float(string="Price")
    description=fields.Text("Product Description")
    restaurant_id=fields.Many2one("restaurant.name",string="Restaurant Name")
    product_categroy_id=fields.Many2one("food.product.category",string="Food Categroy")