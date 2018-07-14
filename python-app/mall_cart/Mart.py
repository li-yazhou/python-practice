# -*- coding: utf-8 -*-
from db import DB


class Mart(object):
	def __init__(self,db,cart=None):
		self.db = db
		self.cart = cart

	def run(self):
		self.mainview()

	def mainview(self):
		content = """
			******************************************
			   	welcome you, please choose:
			   	------------------------
			  	 1.show product list
			  	 2.buy product
			   	 3.show cart
			   	 4.pay
			******************************************
			"""
		print content
		self.chooseService()

	def chooseService(self):
		choices = ['1','2','3','4']
		while True:
			no = raw_input('please input number [1-4]:')
			if no in choices:
				no = int(no)
				break	
		if no == 1:
			self.showProductList()
		elif no == 2:
			self.buyProduct()
		elif no == 3:
			self.showCart()
		else:
			self.pay()
		



	def showProductList(self):
		db = self.db
		for p in db.productList:
			print p
		self.mainview()

	def buyProduct(self):
		Nos = []
		for i in range(1,21):
			Nos.append(str(i))

		while True:
			no = raw_input('请输入购买商品的编号：')
			if no in Nos:
				break

		no = int(no)
		# 初始化选购商品
		product = self.db.productList[no-1]
		print product
		while True:
			num = raw_input('please input product number [1-5]')
			if num in Nos and 0 <= Nos.index(num) <= 4:
				break

		num = int(num)
		print product, ',\t product number:', num, ',\t小计:', product.price * num
		self.cart.addProduct(product,num)
		self.mainview()


	def showCart(self):
		cart_content = self.cart.cart
		# print cart_content is None
		# print cart_content == None
		# print cart_content == []
		if cart_content != []:
			print '购物车信息如下：'
			self.print_list()
		else:
			print '您的购物车还空空如也，欢迎选购商品！'
		self.mainview()

	def pay(self):
		cart = self.cart  # 购物车本身，包含总金额属性和清空商品方法等
		cart_content = cart.cart  #购物车里面的商品
		total = cart.total()
		change = 0
		if cart_content != []:
			while True:
				s = '商品总金额是：' + str(total)  + '，所付金额不能少于：' + str(total)
				money = raw_input(s)
				if money.isdigit() and int(money) >= total:
					change = int(money) - total
					print '商品总金额是：', total
					print '您付金额是：',money
					break

		if cart_content != []:
			print '找零：',change
			print '购物清单是：'
			self.print_list()
			cart.clear() #清空购物车
		else:
			print '您的购物车还空空如也，欢迎选购商品！'
		self.mainview()


	# 购物车中商品列表
	def print_list(self):
		cart = self.cart
		cart_content = self.cart.cart
		# print cart_content is None
		# print cart_content == None
		# print cart_content == []
		for productItem in cart_content:
			print productItem
		print 'Total is ',cart.total()


