class Shipping(object):

	__customer = None
	__shipping_cost_per_item = 2.5 
	__articleLst = []
	
	def __init__(self, articleLst, customer):
		self.__customer = customer
		self.__articleLst = articleLst
		
	def getShippingCost(self):
		return len(self.__articleLst) * self.__shipping_cost_per_item