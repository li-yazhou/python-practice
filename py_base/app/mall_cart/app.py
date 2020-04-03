# -*- coding: utf-8 -*-
from db import DB
from Cart import Cart
from Mart import Mart

if __name__ == '__main__':
	db = DB()
	db.getProductList()
	mart = Mart(db,Cart())
	mart.run()