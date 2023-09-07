from Magazine import magazine1, magazine2
from Author import author1, author2 

class Article :
    _articles = []

    def __init__(self, author, id, magazine, title) :
        self.id = id
        self._title = title
        self._author = author
        self._magazine = magazine
        Article._articles.append(self)
    
    def title(self):
        return self._title
    
    def author(self):
        return self._author
    
    def magazine(self):
        return self._magazine
    
    @classmethod
    def all(cls):
        return cls._articles
    

article1 = Article(author1, 1, magazine1, "American tour")
article2 = Article(author2, 2, magazine2, "Transfomers")

print("Article 1's title:", article1.title())
print("Article 2's title:", article2.title())

print("Article 1's author:", article1.author().name())
print("Article 2's author:", article2.author().name())


all_articles = Article.all()
for article in all_articles:
    print("Article:", article.title(), "-Author:", article.author().name(), "-Magazine:", article.magazine().name())
