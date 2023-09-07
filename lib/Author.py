class Author :
    def __init__(self, id, name) :
        self.id = id
        self._name = name
        self._articles = []

    def add_article(self, article):
        self._articles.append(article)

    def name(self):
        return self._name
    
    def articles(self):
        return self._articles
    
    def topic_areas(self):
        unique_categories = set()
        for article in self._articles:
            unique_categories.add(article.magazine().category())
        return list(unique_categories)
    
    def magazines(self):
        unique_magazines = set()
        for article in self._articles:
            unique_magazines.add(article.magazine())
        return list(unique_magazines)


author1 = Author(1, "Delamoar Vikta")
author2 = Author(2, "Benjamin Djibah")

print("Author's name:", author1.name())
print("Author's name:", author2.name())