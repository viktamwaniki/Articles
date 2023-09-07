class Magazine:
    _magazines = []
    def __init__(self, id, name, category):
       self.id = id
       self._name = name
       self._category = category
       self._articles = []
       self._contributors = []
       Magazine._magazines.append(self)
 
    
    def name(self):
        return self._name
    
    def category(self):
        return self._category
    
    def add_contributor(self, author):
        self._contributors.append(author)

    def add_article(self, article):
        self._articles.append(article)

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._magazines:
            if magazine._name == name:
               return magazine
        return None
    
    @classmethod
    def article_titles(cls, name):
        magazine = cls.find_by_name(name)
        if magazine:
            return [article.title() for article in magazine._articles]
        return []
    
    def contributors(self):
        return self._contributors
    
    def all():
        return Magazine._magazines

magazine1 = Magazine(1, "Travel Blog", "Travelling")
magazine2 = Magazine(2, "Electricity World", "Electricity")

print("Magazine 1's name:", magazine1.name())
print("Magazine 1's category:", magazine1.category())

print("Magazine 2's name:", magazine2.name())
print("Magazine 2's category:", magazine2.category())

all_magazines = Magazine.all()
for magazine in all_magazines:
    print("Magazine:", magazine.name(), "-Category:", magazine.category())

print("Contributors for Magazine 1: ")
for contributor in magazine1.contributors():
    print("-", contributor.name())

print("Contributors for Magazine 2: ")
for contributor in magazine2.contributors():
    print("-", contributor.name())