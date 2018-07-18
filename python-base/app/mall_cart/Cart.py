# -*- coding: utf-8 -*-
from Product import Product
from ProductItem import ProductItem

class Cart(object):
	"""用户购买商品业务逻辑"""
	def __init__(self):
		self.cart = []

	#添加商品
	def addProduct(self,product,num=1):
		cart = self.cart

		# 先把这种商品封装成购物项
		pi = ProductItem(product,num)
		if pi in cart:
			# 取出该商品
			pi = cart[cart.index(pi)]
			# 修改商品数量
			# pi.addNum(num)
			pi.count = pi.count + num
		else:
			cart.append(pi)
		
	#删除商品
	def deleteProductItem(self,pi):
		self.cart.remove(pi)

	# # 清空购物车
	def clear(self):
		self.cart = []


	# 计算商品总金额
	def total(self):
		total = 0
		if self.cart != []:
			for productItem in self.cart:
				total += productItem.amount()
		return total


		## 用in关键即可
		# 将该商品封装成一种购物项
		# temp = productItem(product)
		# if cart.contains(temp):
		# 	#假如购物车里面包含这种商品则取出该购物项
		# 	productItem = cart[cart.index(temp)]
		# 	productItem.addNum(num)
		# else:

		
	# #查看购物车是否包含该商品	
	# def contains(self,productItem):
	# 	retval = false
	# 	if cart.index(productItem) != -1:
	# 		retval = True
	# 	return retval

