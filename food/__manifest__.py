# -*- coding: utf-8 -*-
{
    'name' : 'Food delivery',
    'description' : " Food delivery module",
    'version' :'',
    'author':'Althaf Shaik',
    'category':'Advertising',
    'depends':['mail',],
    'data':[
         'security/ir.model.access.csv',
         'views/food_delivery_menu.xml',
         'views/food_delivery_view.xml',
         'views/food_product_view.xml',
         'views/restaurant_name_view.xml',
        #  'views/user_details_view.xml',
    ],
    'demo':[
            'demo/demo_data.xml',
    ],
    'application' : True,
    
}