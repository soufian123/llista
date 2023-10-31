from article import Article

class Registre:
    def __init__(self, article, quantitat):
        self.article = article
        self.quantitat = quantitat

    def get_quantitat(self):
        return self.quantitat

    def set_quantitat(self, quantitat):
        self.quantitat = quantitat

    def to_dict(self):
        return {
            "article": self.article.to_dict(),
            "quantitat": self.get_quantitat()
        }

    @classmethod
    def from_dict(cls, data):
        article = Article.from_dict(data["article"])
        return cls(article, data["quantitat"])