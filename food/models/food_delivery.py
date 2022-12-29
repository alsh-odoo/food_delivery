# -*- coding: utf-8 -*-

from odoo import models,fields

class foodDelivery(models.Model):
    _name="food.delivery"
    _description="This is a description of food delivery in our local area"

    name=fields.Char("Name",required=True)
    date=fields.Date.to_date(self._context.get('date_from'))
    city=fields.Char("City")
    pincode=fields.Integer("Pincode")
    state=fields.Char("State")
    restaurant_name=fields.Char("Restaurant Name")
    food_type=fields.Selection(
        string="Veg/Non-Veg",selection=[('vegitarian','Vegitarian'),('non_vegitarian','Non Vegitarian')]
    )
    delivery_type=fields.Selection(
        string="Delivery/Takeaway",
        selection=[('delivery','Delivery'),('take_away','Take Away')]
    )


