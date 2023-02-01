# -*- coding: utf-8 -*-

from odoo import fields,models,api

class cusineStyle(models.Model):
    _name="cusine.style"
    _description="This model defines the style of the food like north Indian,South Indian and Chinese"
    _order="name"

    name=fields.Char('Name',required=True)
    color=fields.Integer()

    _sql_constraints=[('cusine_style_unique','unique(name)','Cusine style must be unique')]