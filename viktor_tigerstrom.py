from abc import ABCMeta, abstractproperty, abstractclassmethod

class BudgetControl(object):

	__initialBalance = 0
	__incomes = 0
	__expenses = 0
	__balance = 0
	__inventory = None
	__purchaseLst = []
	__shippingLst = []
	__salesLst = []
	__returnsLst = []
	
	def __init__(self, initialBalance, inventory):
		self.__inventory = inventory
		self.__initialBalance = initialBalance
		self.__balance = initialBalance
		
	def recalculateBalance(self):
		self.__expenses = sum([purchase.getPurchaseTotalPrice() for purchase in self.__purchaseLst])
		self.__expenses += sum([shipping.getShippingCost() for shipping in self.__shippingLst])
		self.__expenses += sum([_return.GetReturnCost() for _return in self.__returnsLst])
		self.__incomes = sum([sale.getTotalSalePrice() for sale in self.__salesLst])
		self.__balance = (self.__initialBalance + self.__incomes) - self.__expenses
		
	def expenseWithinBudget(self, expense):
		return self.__balance - expense >= 0
	
	def addSaleWithShipping(self, sale, shipping):
		if(not(self.expenseWithinBudget(shipping.getShippingCost()))):
			return False
		self.__salesLst.append(sale)
		self.__shippingLst.append(shipping)
		self.recalculateBalance()
		return True
	
	def addPurchase(self, purchase):
		if(not(self.expenseWithinBudget(purchase.getPurchaseTotalPrice()))):
			return False
		self.__purchaseLst.append(purchase)
		self.recalculateBalance()
		return True
	
	def addReturnWithShipping(self, newReturn, shipping):
		if(not(self.expenseWithinBudget(shipping.getShippingCost() + newReturn.GetReturnCost()))):
			return False
		self.__returnsLst.append(newReturn)
		self.__shippingLst.append(shipping)
		self.recalculateBalance()
		return True
		
	def generateIncomeStatement(self):
		self.recalculateBalance()
		incomeStateMentString = 'Most Recent Income Statement'
		inventoryStock = self.__inventory.dictionaryOfStock()
		incomeStateMentString += '\n\n----------------------------\n'
		incomeStateMentString += '\nThe items in stock are: '
		for key in inventoryStock.keys():
			incomeStateMentString += '\n' + key + ': ' + str(inventoryStock[key])
		incomeStateMentString += '\n\n----------------------------\n'
		incomeStateMentString += '\nThe total amount of sales is ' + str(len(self.__salesLst)) 
		incomeStateMentString += ' generating an income of ' + str(sum([sale.getTotalSalePrice() for sale in self.__salesLst]))
		incomeStateMentString += '\nThe total amount of purchases is ' + str(len(self.__purchaseLst)) 
		incomeStateMentString += ' generating an expense of ' + str(sum([purchase.getPurchaseTotalPrice() for purchase in self.__purchaseLst]))
		incomeStateMentString += '\nThe total amount of returns is ' + str(len(self.__returnsLst)) 
		incomeStateMentString += ' generating an expense of ' + str(sum([_return.GetReturnCost() for _return in self.__returnsLst]))
		incomeStateMentString += '\nThe total amount of shipments is ' + str(len(self.__shippingLst)) 
		incomeStateMentString += ' generating an expense of ' + str(sum([shipping.getShippingCost() for shipping in self.__shippingLst]))
		incomeStateMentString += '\n\n----------------------------\n'
		incomeStateMentString += '\nInitial balance  ' + str(self.__initialBalance)
		incomeStateMentString += '\nRevenues         ' + str(self.__incomes)
		incomeStateMentString += '\nExpenses         ' + str(self.__expenses)
		incomeStateMentString += '\n\n----------------------------\n'
		incomeStateMentString += '\nBalance          ' + str(self.__balance)
		return incomeStateMentString

class Article(object):
    __metaclass__ = ABCMeta
    @abstractproperty
    def name(self):
        pass
    @abstractproperty
    def purchasePrice(self):
        pass
    @abstractproperty
    def salesPrice(self):
        pass
    
    def getName(self):
        return self.name
    def getPurchasePrice(self):
        return self.purchasePrice
    def getSalesPrice(self):
        return self.salesPrice
    
    @abstractclassmethod
    def generateArticle(self):
        pass

    
class Hoverboard(Article):
    name = "Hoverboard"
    purchasePrice = 100.00
    salesPrice = 250.00
    
    @abstractclassmethod
    def generateArticle(self):
        return Hoverboard()

class RecordPlayer(Article):
    name = "RecordPlayer"
    purchasePrice = 25.00
    salesPrice = 80.00
    
    @abstractclassmethod
    def generateArticle(self):
        return RecordPlayer()
    
class BowTie(Article):
    name = "BowTie"
    purchasePrice = 25.00
    salesPrice = 50.00
    
    @abstractclassmethod
    def generateArticle(self):
        return BowTie()
    
class PapsBlueRibbon(Article):
    name = "PapsBlueRibbon"
    purchasePrice = 1.00
    salesPrice = 2.00
    
    @abstractclassmethod
    def generateArticle(self):
        return PapsBlueRibbon()

class IPABeer(Article):
    name = "IPABeer"
    purchasePrice = 3.00
    salesPrice = 6.00
    
    @abstractclassmethod
    def generateArticle(self):
        return IPABeer()

