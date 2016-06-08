class Customer:
	def __init__(self, fullName, address):
		self.fullName = fullName
		self.address = address
		
	def getFullName(self):
		return self.fullName.split( )[-1]
		
	def getFullAddress(self):
		return self.address

class Return(object):
    __articlesReturned = []
    __inventory = None
    
    def __init__(self, articles, inventory):
        self.__articlesReturned = articles
        self.__inventory = inventory
    
    def GetReturnCost(self):
        return sum([article.getSalesPrice() for article in self.__articlesReturned])
    
    def makeReturn(self):
        for article in self.__articlesReturned:
            self.__inventory.addArticle(article)
	
	
