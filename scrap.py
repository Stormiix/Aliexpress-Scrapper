# -*- coding: utf-8 -*-

# @Author: Stormix - Anas Mazouni
# @Website: https://stormix.co

class AliExpress_Product:
    '''
        AliExpress Class
    '''

    # AliExpress Product Class Attributes
    Name = None
    Price = None
    Stock = None
    Currency = None
    Shipping = None
    Condition = None
    Rating = None
    Orders = None
    Guarantee = None

    def __init__(self,url):
        self.productUrl = url

    def __str__(self):
        '''
		Object Representation
        '''
        return 'Product : {}'.format(self.productUrl)

    def productDetails(self):
        ## Add code here
