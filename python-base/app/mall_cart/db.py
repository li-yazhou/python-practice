# -*- coding: utf-8 -*-
from Product import Product

class DB(object):
	def __init__(self):
		self.productList = []

	#获取商品列表
	def getProductList(self):
		productList = self.productList
		for i in range(1,21):
			p = Product(i, "cloth"+ str(i), 100 + 10 * i)
			productList.append(p)
		