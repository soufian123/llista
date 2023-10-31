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