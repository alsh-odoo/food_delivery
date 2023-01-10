# -*- coding: utf-8 -*-

from odoo import models,fields

class foodDelivery(models.Model):
    _name="food.delivery"
    _description="This is a description of food delivery in our local area"

    name=fields.Char("Name",required=True)
    email=fields.Char(string="Email",required=True)
    mobile_number=fields.Char(string="Mobile Number")
    datetime = fields.Datetime.now('datetime')
    city=fields.Char("City")
    pincode=fields.Char("Pincode")
    state=fields.Char("State")
    food_type=fields.Selection(
        string="preffered food",
        selection=[('vegitarian','Pure Veg'),('non_vegitarian','Veg & Non veg')]
    )
    restaurant_name_id = fields.Many2one('restaurant.name',string="Restaurant Name")
    # delivery_type=fields.Selection(
    #     string="Delivery/Takeaway",
    #     selection=[('delivery','Delivery'),('take_away','Take Away')]
    # )
    
    # status = fields.Selection( 
    #     string='Status', 
    # selection = [('new', 'New'),('in_progress', 'In Progress'),('cancel', 'Cancelled'),('done', 'Done')])


