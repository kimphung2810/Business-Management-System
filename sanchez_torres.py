class Inventory(object):
    __stock = []
    
    def addArticle(self, article):
        self.__stock.append(article)
        
    def removeArticle(self, article):
        try:
            self.__stock.remove(article)
            return True
        except ValueError:
            return False
        
    def removeArticleByName(self, articleName):
        try:
            article = self.findArticle(articleName)
            self.__stock.remove(article)
            return True
        except ValueError:
            return False
        
    def findArticle(self,articleName):
        for article in self.__stock:
            if article.getName() == articleName:
                return article
        return None
    
    def itemsInStock(self, itemsToCheckLst):
        stockDict = self.dictionaryOfArticleList(self.__stock)
        itemsDict = self.dictionaryOfArticleList(itemsToCheckLst)
        for articleName in itemsDict.keys():
            if(not(stockDict.get(articleName)) or itemsDict[articleName] > stockDict[articleName]):
                return False
        return True
        
    def dictionaryOfArticleList(self, artLst):
        artDict = {}
        for article in artLst:
            if artDict.get(article.getName()):
                artDict[article.getName()] = artDict[article.getName()] + 1
            else:
                artDict[article.getName()] = 1
        return artDict

    def dictionaryOfStock(self):
        return self.dictionaryOfArticleList(self.__stock)