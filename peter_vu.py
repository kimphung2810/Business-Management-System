class Purchase(object):
    
    __listOfArticles = []
    __inventory = None
    
    def __init__(self, listOfArticles, inventory):
        self.__listOfArticles = listOfArticles
        self.__inventory = inventory

    def getPurchaseTotalPrice(self):
        return sum([article.getPurchasePrice() for article in self.__listOfArticles])

    def addToInventory(self):
        for article in self.__listOfArticles:
            self.__inventory.addArticle(article)