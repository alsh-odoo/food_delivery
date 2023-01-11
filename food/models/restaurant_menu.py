# -*- coding: utf-8 -*-

from oddo import models,fields,api,_

class restaurantMenu(models.Model):
    _name="restaurant.menu"
    _description="This model is used to define the menuitems of a restaurant"

    name=fields.Char()
