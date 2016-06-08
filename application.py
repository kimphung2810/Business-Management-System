from sanchez_torres import Inventory
from peter_vu import Purchase
from phung_tran import Sale
from patrick_ryan import Shipping
from brian_vuong import Return, Customer
from joshua_ungheanu import LogicControl
from viktor_tigerstrom import BudgetControl, Article, BowTie, Hoverboard, IPABeer, PapsBlueRibbon, RecordPlayer

def main():
	#use Customer class
    customer = Customer('Angelina Ung','Fullerton, 92834')#create an object of Customer with information
    Name = customer.getFullName()#get customer full name
    Address = customer.getFullAddress()#get customer adress

	#use Article class
    bowtie = BowTie()#Creates an object of BowTie that inherits from Article
    bowtieName = bowtie.getName()#get article name
    bowtieSalesPrice = bowtie.getSalesPrice()#get article sale price
    bowtiePurchasePrice = bowtie.getPurchasePrice()#get article price when it is purchased

    bowtie2 = bowtie.generateArticle()#another way to create an object of Hoverboard that inherits from Article

	#use Inventory class
    inventory = Inventory()#create an object of Inventory
    #use Purchase class
    articleLst = [bowtie, bowtie2, bowtie, bowtie]#generate a list of articles need to purchase
    purchase = Purchase(articleLst,inventory)#create an object of Purchase to buy articles in articleLst to add to inventory
    purchase.addToInventory()#Add all of the articles purchased to inventory
    totalPurchasePrice = purchase.getPurchaseTotalPrice()#calculate the total purchase price then return
    
    #use Inventory class
    inventory.addArticle(bowtie)#add bowtie to inventory
    inventory.addArticle(bowtie2)#add bowtie to inventory
    inventory.addArticle(bowtie2)#add bowtie to inventory
    inventory.addArticle(bowtie2)#add bowtie to inventory
    inventory.addArticle(bowtie2)#add bowtie to inventory

    inventory.removeArticle(bowtie)#remove article from inventory
    inventory.removeArticleByName(bowtieName)#another way to remove article from inventory, removed by its name
    
    articleDict = inventory.dictionaryOfArticleList(articleLst)#generate a dictonary from articleLst 
    inStock = inventory.itemsInStock(articleLst)#check if all of the articles are in stock

	#use Sale class
    sale = Sale(articleLst, customer, inventory)#create an object of Sale to sell items in the articleLst
    saleCustomer = sale.GetCustomerName()#get Customer's full name
    totalSalesPrice = sale.getTotalSalePrice()#calculate the total sale price then return
    sale.MakeSale()#sell items

	#user Shipping class
    shipping = Shipping(articleLst,customer)#create an object of Shipping to ship the customer articles in the articleLst
    shippingCost = shipping.getShippingCost()#get the total shipping cost for the items sold
    
    #use LogicControl class
    amount = 1000000
    logicControl = LogicControl(amount)#create an object of LogicControl with the amount
    logicControl.MakePurchase(articleLst)#to purchase items in the articleLst
    logicControl.MakeSale(articleLst, customer)#to sell items in the articleLst to the customer
    
    #use BudgetControl class
    budgetControl = BudgetControl(amount, inventory)#create an object of BudgetControl with the amount
    inBudget = budgetControl.expenseWithinBudget(purchase.getPurchaseTotalPrice())#check if the balance amount >= than the purchase price 
    budgetControl.addPurchase(purchase)#add purchase information
    budgetControl.addSaleWithShipping(sale, shipping)#add sale and shipping information
    budgetControl.recalculateBalance()#calculate balance 
    budgetControl.generateIncomeStatement()#output income
    
    print(logicControl.GetIncomeStatement())#to output incomE

	#use Return class
    returnItem = Return(articleLst,inventory)#create an object of Return to return articles in the articleLst			
    returnCost = returnItem.GetReturnCost()#gets the total of return cost for the items returned
    returnItem.makeReturn()#return items

    #use LogicControl class
    logicControl.MakeReturn(articleLst, customer)#to return items in the articleLst from the customer
    
    #use BudgetControl class
    budgetControl.addReturnWithShipping(returnItem, shipping)#add returnItem and shipping information
    budgetControl.recalculateBalance()#calculate balance 
    
    print(logicControl.GetIncomeStatement())#to output incomE

main()



