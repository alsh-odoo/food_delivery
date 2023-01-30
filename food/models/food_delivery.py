# -*- coding: utf-8 -*-

from odoo import models,fields

class foodDelivery(models.Model):
    _name="food.delivery"
    _description="This model is used to create a food order in our local city"
    _inherit= ['mail.thread','mail.activity.mixin']
    _order = "name"


    name=fields.Char(" food product",related="menu_item_ids.name",required=True)
    date = fields.Date('order_date',default=fields.Date.context_today)
    house_no = fields.Char("House-No/Street")
    city=fields.Char("City")
    pincode=fields.Char("Pincode")
    food_type=fields.Selection(
        string="Preffered Food",
        selection=[('vegitarian','Pure Veg'),('non_vegitarian','Veg & Non veg')]
    )
    state=fields.Selection(
        string="Statusbar",
        selection=[('new','New'),('preparing_food','Preparing Food'),('dispatched','Dispatched'),('cancel','Cancelled')],default="new",tracking=True)
    restaurant_name_id = fields.Many2one('restaurant.name',string="Restaurant Name")
    menu_item_ids = fields.Many2many('food.product', string="Food Menu")
    cusine_style_ids=fields.Many2one('cusine.style',string="Cusine Style")
    # user_details_ids=fields.One2many('user.details','customer_details_id')
    delivery_boy_id=fields.Many2one('res.users',string="Delivery Boy",default=lambda self:self.env.user)

    # #constraints
    # _sql_constraints=[('check_')]



