from categoria import Categoria
from article import Article
from registre import Registre
from lliste import Llista

def main():
    # Crear una instancia de la lista de compra
    llista = Llista()

    # Crear categorías y artículos
    categoria_frescos = Categoria("Frescos")
    categoria_frescos.add_article(Article("Llet"))
    categoria_frescos.add_article(Article("Ous"))

    categoria_begudes = Categoria("Begudes")
    categoria_begudes.add_article(Article("Aigua"))
    categoria_begudes.add_article(Article("Suc"))

    # Agregar categorías a la lista
    llista.create_categoria(categoria_frescos)
    llista.create_categoria(categoria_begudes)

    # Agregar registros
    registre1 = Registre(categoria_frescos.read_article("Llet"), 2)
    registre2 = Registre(categoria_begudes.read_article("Aigua"), 3)

    llista.create_registre(registre1)
    llista.create_registre(registre2)

    # Guardar la lista en un archivo JSON
    llista.desa_a_disc("llista_compra.json")

if __name__ == "__main__":
    main()