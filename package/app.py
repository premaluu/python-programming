'''
    name : app.py
    Created by : Premal Upadhyay
    Date : 31-01-2022
'''

#Importing entire module
import ecommerce.shipping

#Import one function from that module
from ecommerce.shipping import calc_shipping

ecommerce.shipping.calc_shipping()
calc_shipping()