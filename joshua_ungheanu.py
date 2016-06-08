from sanchez_torres import Inventory
from peter_vu import Purchase
from phung_tran import Sale
from patrick_ryan import Shipping
from brian_vuong import Return
from viktor_tigerstrom import BudgetControl

class LogicControl(object):
    __budgetControl = None
    __inventory = None
    
    def __init__(self, initialBalance):
        self.__inventory = Inventory()
        self.__budgetControl = BudgetControl(initialBalance, self.__inventory)

    def MakePurchase(self, lstArticles):
        purchase = Purchase(lstArticles, self.__inventory)
        if(not(self.__budgetControl.addPurchase(purchase))):
            return None
        purchase.addToInventory()
        return purchase
    
    def MakeSale(self, lstArticles, customer):
        if(not(self.__inventory.itemsInStock(lstArticles))):
            return None
        sale = Sale(lstArticles, customer, self.__inventory)
        if(not(self.__budgetControl.addSaleWithShipping(sale, Shipping(lstArticles, customer)))):
            return None
        sale.MakeSale()
        return sale
    
    def MakeReturn(self, lstArticles, customer):
        newReturn = Return(lstArticles, self.__inventory)
        if(not(self.__budgetControl.addReturnWithShipping(newReturn, Shipping(lstArticles, customer)))):
            return None
        newReturn.makeReturn()
        return newReturn
    
    def GetIncomeStatement(self):
        return self.__budgetControl.generateIncomeStatement()
