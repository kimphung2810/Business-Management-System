from sanchez_torres import Inventory
from peter_vu import Purchase
from phung_tran import Sale
from patrick_ryan import Shipping
from brian_vuong import Return, Customer
from joshua_ungheanu import LogicControl
from viktor_tigerstrom import BudgetControl, Article, BowTie, Hoverboard, IPABeer, PapsBlueRibbon, RecordPlayer

def main():
    #Creates a Hoverboard object that inherits from the abstract class Article
    hoverboard1 = Hoverboard()
    #Gets the name of the article.
    hoverboardName = hoverboard1.getName()
    #Gets the purchase price of the article.
    hoverboardPurchasePrice = hoverboard1.getPurchasePrice()
    #Gets the sales price of the article.
    hoverboardSalesPrice = hoverboard1.getSalesPrice()
    #Creates a new Hoverboard object
    hoverboard2 = hoverboard1.generateArticle()
    #Creates an Inventory Object
    
    
    inventory = Inventory()
    #Adds the hoverboard1 object to the inventory
    inventory.addArticle(hoverboard1)
    #Removes the hoverboard1 object from the inventory
    inventory.removeArticle(hoverboard1)
    inventory.addArticle(hoverboard1)
    #Removes the first occurrence of a object in the inventory that has the same name as the hoverboard article
    inventory.removeArticleByName(hoverboardName)
    articleLst = [hoverboard1,hoverboard2]
    #Generates a dictionary from a list of articles with the name of the article as the key, 
    #and the number of objects in the list with the same article name as the value
    articleDict = inventory.dictionaryOfArticleList(articleLst) 
    #Checks if there are enough articles in the inventory to cover for the article list
    #which is important since you can't sell articles that are not in stock
    inStock = inventory.itemsInStock(articleLst)
    #Creates a customer object
    
    
    #Generates a customer object
    customer1 = Customer('Peter Smith','Student Housing II, Fullerton, CA 92831')
    #Gets the customer name
    customerName = customer1.getFullName()
    #Gets the customer adress 
    customerAdress = customer1.getFullAddress()
    
    
    #Creates a purchase object of two hoverboards
    purchase1 = Purchase(articleLst,inventory)
    #Gets the total purchase price for all articles included in the purchase
    totalPurchasePrice = purchase1.getPurchaseTotalPrice()
    #Executes the purchase which adds the articles to the inventory
    purchase1.addToInventory()
    
    
    #Generates a sale object for two hoverboards to the customer Peter Smith
    sale1 = Sale(articleLst, customer1, inventory)
    #Gets the name of the customer who the articles have been sold to
    saleCustomer = sale1.GetCustomerName()#not working
    #Gets the total sales price for the sale
    totalSalesPrice = sale1.getTotalSalePrice()
    #Executes the sale which will remove the articles from the inventory
    sale1.MakeSale()
    
    
    #Generates a shipping object for the sale of two hoverboards to the customer Peter Smith
    shipping1 = Shipping(articleLst,customer1)
    #Gets the total shipping cost for all shipped articles in the article list
    shippingCost = shipping1.getShippingCost()
    
    
    #Generates a return object for two hoverboards
    return1 = Return(articleLst,inventory)
    #Gets the total return cost
    returnCost = return1.GetReturnCost()
    #Executes the return which will refill the inventory with the articles in the return
    return1.makeReturn()
    
    
    #Generates a new budget control object with the initial balance of 50000
    budgetControl1 = BudgetControl(50000, inventory)
    #Checks whether there is enough balance for the expense, in this case a purchase
    inBudget = budgetControl1.expenseWithinBudget(purchase1.getPurchaseTotalPrice())
    #Adds the purchase to the budget control, effecting the balance and the expenses
    budgetControl1.addPurchase(purchase1)
    #Adds a sale with it's shipping cost to the budget control if the balance is enough to pay for the shipping
    budgetControl1.addSaleWithShipping(sale1, shipping1)
    #Adds a return with it's shipping cost to the budget control if the balance is enough
    budgetControl1.addReturnWithShipping(return1, shipping1)
    #Recalculates all expenses, incomes and the total balance
    budgetControl1.recalculateBalance()
    #Generates the budget control objects current income statement
    budgetControl1.generateIncomeStatement()
    
    
    #Generates a new logic control object with a new inventory and a new budget control with the initial balance of 50000
    logicControl1 = LogicControl(50000)
    #Executes the sale of two hoverboards if the purhcase is within budget
    logicControl1.MakePurchase(articleLst)
    #Executes a sale of two hoverboards to the customer Peter Smith if they are in stock 
    #and there is enough balance to pay for the shipping
    logicControl1.MakeSale(articleLst, customer1)
    #Executes a return of two hoverboards from the customer Peter Smith if it is within budget
    logicControl1.MakeReturn(articleLst, customer1) 
    #Returns the current income statement for the budget control object stored in the logic control object
    print(logicControl1.GetIncomeStatement())
    
    print("all good")

if __name__ == '__main__':
    main()




