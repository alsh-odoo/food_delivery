# -*- coding: utf-8 -*-

from odoo import models,fields

class foodDelivery(models.Model):
    _name="food.delivery"
    _description="This is a description of food delivery in our local area"
    _order = "name"


    name=fields.Char("Name",required=True)
    datetime = fields.Datetime.now('datetime')
    house_no = fields.Char("House-No/Street")
    city=fields.Char("City")
    pincode=fields.Char("Pincode")
    state=fields.Char("State")
    food_type=fields.Selection(
        string="Preffered Food",
        selection=[('vegitarian','Pure Veg'),('non_vegitarian','Veg & Non veg')]
    )
    # state=fields.Selection(
    #     string="State",
    #     selection=[('new','New','preparing_food','Preparing Food')]
    # )

    restaurant_name_id = fields.Many2one('restaurant.name',string="Restaurant Name")
    menu_item_ids = fields.One2many('restaurant.menu.items','food_delivery_id')

    user_details_ids=fields.One2many('user.details','customer_details_id')
    delivery_boy_id=fields.Many2one('res.users',string="Delivery Boy")
    # delivery_type=fields.Selection(
    #     string="Delivery/Takeaway",
    #     selection=[('delivery','Delivery'),('take_away','Take Away')]
    # )
    
    # status = fields.Selection( 
    #     string='Status', 
    # selection = [('new', 'New'),('in_progress', 'In Progress'),('cancel', 'Cancelled'),('done', 'Done')])


