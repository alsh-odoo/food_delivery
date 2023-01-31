# -*- coding: utf-8 -*-
from odoo import models,fields,api

class foodProductCategory(models.Model):
    _name="food.product.category"
    _description="this model is to categorize the food product"
    _order="name"

    name=fields.Char(string="Food Category",required=True)

