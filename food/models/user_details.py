# -*- coding: utf-8 -*-

from odoo import fields,models,api,_

class userDetails(models.Model):
    _name = "user.details"
    _description = "This model is linked with food.delivery model to describe user details"

    customer_details_id=fields.Many2one('food.delivery',required=True)
    email=fields.Char(string="Email",required=True)
    mobile_number=fields.Char(string="Mobile Number")