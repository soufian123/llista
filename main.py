from categoria import Categoria
from article import Article
from registre import Registre
from lliste import Llista

def main():
    # Crear una instancia de la lista de compra
    llista = Llista()

    # Intenta crear la categoría "Frescos"
    try:
        categoria_frescos = Categoria("Frescos")
        llista.create_categoria(categoria_frescos)
    except ValueError:  # Si la categoría ya existe, utiliza la categoría existente
        categoria_frescos = llista.read_categoria("Frescos")

    # Crea una nueva categoría "Parafarmacia" y agrégala a la lista
    categoria_parafarmacia = Categoria("Parafarmacia")
    llista.create_categoria(categoria_parafarmacia)

    # Agrega artículos a la categoría "Frescos"
    categoria_frescos.add_article(Article("Llet"))
    categoria_frescos.add_article(Article("Ous"))

    # Agrega artículos a la nueva categoría "Parafarmacia"
    categoria_parafarmacia.add_article(Article("Vitamines"))
    categoria_parafarmacia.add_article(Article("Medicaments"))

    # Agregar registros
    registre1 = Registre(categoria_frescos.read_article("Llet"), 2)
    registre2 = Registre(categoria_parafarmacia.read_article("Vitamines"), 3)

    llista.create_registre(registre1)
    llista.create_registre(registre2)

    # Guardar la lista en un archivo JSON
    llista.desa_a_disc("llista_compra.json")

if __name__ == "__main__":
    main()