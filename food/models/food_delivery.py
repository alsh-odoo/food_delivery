# -*- coding: utf-8 -*-

from odoo import models,fields

class foodDelivery(models.Model):
    _name="food.delivery"
    _description="This is a description of food delivery in our local area"
    _inherit= ['mail.thread','mail.activity.mixin']
    _order = "name"


    name=fields.Char("Name",required=True)
    datetime = fields.Datetime.now('datetime')
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
    menu_item_ids = fields.One2many('restaurant.menu.items','food_delivery_id')
    cusine_style_ids=fields.Many2many('cusine.style',string="Cusine Style")
    user_details_ids=fields.One2many('user.details','customer_details_id')
    delivery_boy_id=fields.Many2one('res.users',string="Delivery Boy")

    # #constraints
    # _sql_constraints=[('check_')]


    # _sql_constraints = [('check_expected_price','CHECK(expected_price>=0)','Expected Price must be positive.'),
    # ('check_selling_price','CHECK(selling_price>=0)','Selling Price must be positive.'),
    # ('check_living_area','CHECK(living_area>=0)','Living Area must be positive.')]


