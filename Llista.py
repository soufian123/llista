import json

class Llista:
    def __init__(self):
        self.registres = []
        self.categories = []

    def get_registres(self):
        return self.registres

    def create_registre(self, registre):
        if self.read_registre(registre.article.get_nom()) is None:
            self.registres.append(registre)
            return registre
        else:
            raise ValueError("Duplicate article name")

    def read_registre(self, nom_article):
        for registre in self.registres:
            if registre.article.get_nom() == nom_article:
                return registre
        return None

    def update_registre(self, registre):
        for i, r in enumerate(self.registres):
            if r.article.get_nom() == registre.article.get_nom():
                self.registres[i] = registre
                return registre
        return None

    def delete_registre(self, nom_article):
        for registre in self.registres:
            if registre.article.get_nom() == nom_article:
                self.registres.remove(registre)
                return
        raise ValueError("Article not found")

    def create_categoria(self, categoria):
        if self.read_categoria(categoria.get_nom()) is None:
            self.categories.append(categoria)
            return categoria
        else:
            raise ValueError("Duplicate category name")

    def read_categoria(self, nom_categoria):
        for categoria in self.categories:
            if categoria.get_nom() == nom_categoria:
                return categoria
        return None

    def update_categoria(self, categoria):
        for i, c in enumerate(self.categories):
            if c.get_nom() == categoria.get_nom():
                self.categories[i] = categoria
                return categoria
        return None

    def delete_categoria(self, nom_categoria):
        for categoria in self.categories:
            if categoria.get_nom() == nom_categoria:
                self.categories.remove(categoria)
                return
        raise ValueError("Category not found")

    def desa_a_disc(self, nom_fitxer):
        data = {
            "registres": [registre.to_dict() for registre in self.registres],
            "categories": [categoria.to_dict() for categoria in self.categories]
        }
        with open(nom_fitxer, 'w') as file:
            json.dump(data, file, indent=4, default=self.custom_json_encoder)

    def llegeix_de_disc(self, nom_fitxer):
        try:
            with open(nom_fitxer, 'r') as file:
                data = json.load(file)
                self.registres = [Registre.from_dict(r) for r in data["registres"]]
                self.categories = [Categoria.from_dict(c) for c in data["categories"]]
        except FileNotFoundError:
            # Si no se encuentra el archivo, se crea una lista vacía.
            self.registres = []
            self.categories = []

    @staticmethod
    def custom_json_encoder(obj):
        if isinstance(obj, Article):
            return {"nom": obj.get_nom()}
        # Aquí puedes agregar otras comprobaciones para otros tipos de clases si es necesario.
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

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

class Article:
    def __init__(self, nom):
        self.nom = nom

    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def to_dict(self):
        return {
            "nom": self.get_nom()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["nom"])

# Ejemplo de uso
if __name__ == '__main__':
    # Crea una llista de compra
    llista = Llista()

    # Crea categorías y artículos
    categoria_frescos = Categoria("Frescos")
    categoria_frescos.add_article(Article("Llet"))
    categoria_frescos.add_article(Article("Ous"))

    categoria_begudes = Categoria("Begudes")
    categoria_begudes.add_article(Article("Aigua"))
    categoria_begudes.add_article(Article("Suc"))

    # Añade las categorías a la lista
    llista.create_categoria(categoria_frescos)
    llista.create_categoria(categoria_begudes)

    # Añade un registro
    registre1 = Registre(categoria_frescos.read_article("Llet"), 2)
    llista.create_registre(registre1)

    # Guarda la lista en disco
    llista.desa_a_disc("llista_compra.json")

    # Lee la lista de disco
    llista.llegeix_de_disc("llista_compra.json")
