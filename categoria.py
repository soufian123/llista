from article import Article

class Categoria:
    def __init__(self, nom):
        self.nom = nom
        self.articles = []

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_articles(self):
        return self.articles

    def add_article(self, article):
        if self.read_article(article.get_nom()) is None:
            self.articles.append(article)
        else:
            raise ValueError("Duplicate article name")

    def delete_article(self, nom_article):
        for article in self.articles:
            if article.get_nom() == nom_article:
                self.articles.remove(article)
                return
        raise ValueError("Article not found")

    def read_article(self, nom_article):
        for article in self.articles:
            if article.get_nom() == nom_article:
                return article
        return None

    def to_dict(self):
        return {
            "nom": self.get_nom(),
            "articles": [article.to_dict() for article in self.articles]
        }

    @classmethod
    def from_dict(cls, data):
        categoria = cls(data["nom"])
        categoria.articles = [Article.from_dict(article_data) for article_data in data["articles"]]
        return categoria