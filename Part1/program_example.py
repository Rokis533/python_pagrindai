
class Book:
    def __init__(self, pavadinimas, autorius):
        self.pavadinimas = pavadinimas
        self.autorius = autorius


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, pavadinimas, autorius):
        book = Book(pavadinimas, autorius)
        self.books.append(book)


def knygos_sukurimas(library: Library):
    while True:
        try:
            pavadinimas = input("Iveskite knygos pavadimą: ")
            autorius = input("Iveskite knygos autoriu: ")
            library.add_book(pavadinimas, autorius)
            break

        except Exception:
            print("Problem")


def run():

    library = Library()
    while True:
        print("Pasirinkite veiksma:")
        print("1. knygos suskurimas")
        # print("2. pajamos")
        # print("3. išrašas")
        user_choise = input("Iveskites (1 arba 2)")
        
        match user_choise:
            case "1":
                knygos_sukurimas(library)
            case "2":
                pass
                # pajamos()


run()