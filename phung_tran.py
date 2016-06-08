# Phung Tran
# CWID: 893977769
# file: phung_tran.py
# Group 4 Project: Py Books - Inventory
# CPSC 223P
# November 21
# Sale class
# This module is created to help the user sell items that are purchased by customers

from brian_vuong import Customer		#use funtioncs in Customer class from brian_vuong module	
class Sale(object):				#Sale class
	articlesSold = []			#initialize a list of artciles sold
	customer = None				#initialize customer information
	invertory = None			#initialize inventory
	
	#constructor
	def __init__(self, articleLst, customer, inventory):
		self.articlesSold = articleLst
		self.customer = customer
		self.invertory = inventory
		
	#function that calculate and return the total price of artciles sold
	def getTotalSalePrice(self):
		return sum([article.getSalesPrice() for article in self.articlesSold])
		
	#function that return customer's full name
	def GetCustomerName(self):
                return self.customer.getFullName()
		
	#function that sell items by reduce article sold in inventory list	
	def MakeSale(self):
		for article in self.articlesSold:
			self.invertory.removeArticleByName(article.getName())
