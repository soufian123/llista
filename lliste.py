from categoria import Categoria
from article import Article
from registre import Registre
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
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")
