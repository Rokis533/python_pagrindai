class Irasas:
    def __init__(self, suma, kiekis):
        self.suma = suma
        self.kiekis = kiekis

    def __str__(self):
        return f"Str: {self.__class__.__name__}: {self.suma}, kiekis: {self.kiekis}"
    
    def __repr__(self):
        return f"Repr: {self.__class__.__name__}({self.suma}), {self.kiekis}"
    