# class User:
#     #this is constructor, it is called when we create an object of this class
#     def __init__(self, name, age, address = "Unknown"):
#         self.name = name
#         self.age = age
#         self.location = address

#     # this is a method, it is a function that belongs to the class
#     def print_hello(self):
#         print("Hello,", self.name)

#     # this is a method, it is a function that belongs to the class
#     def __str__(self):
#         return f"-------\nUser: {self.name}, \nAge: {self.age}, \nLocation: {self.location}\n-----"



# list_of_users : list[User] = []

# while True:
#     name = input("Iveskite varda: ")
#     age = int(input("Iveskite amziu: "))
#     location = input("Iveskite miesta: ")
#     user = User(name, age, location)
    
#     list_of_users.append(user)
#     is_continue = input("Ar norite testi? (y/n): ")
#     if is_continue.lower() != "y":
#         break


# for user in list_of_users:
#     user.print_hello()
#     print(user)



# user = User("Rokas", 30)
# user2 = User("Tomas", 30, "Vilnius")


# print(user.name)
# print(user.age)
# print(user.location)

# user.print_hello()
# user2.print_hello()


# print()
# print(user2.name)
# print(user2.age)
# print(user2.location)

# print(user)
# print(user2)

# print(id(user))
# print(type(user))

# print("-"*50)
# text = "Labas, kaip sekasi?"

# text = text.upper()

# print(id(text))
# print(type(text))


#####################################################################

# class Sentence:
#     def __init__(self, text):
#         self.text : str = text

#     def print_text(self):
#         print(self.text)

#     def count_words(self):
#         return len(self.text.split())

#     def count_characters(self):
#         return len(self.text)
    
#     def count_digits(self):
#         return sum(c.isdigit() for c in self.text)
    
#     def count_letters(self):
#         return sum(c.isalpha() for c in self.text)
    

# sentence1 = Sentence("Labas, kaip sekasi?")
# sentence2 = Sentence("1234 5678 90")
# sentence3 = Sentence("Labas1234, kaip sekasi?")
# sentence4 = Sentence("Labas, kaip sekasi1234?")

# list_of_sentences = [sentence1, sentence2, sentence3, sentence4]


# for sentence in list_of_sentences:
#     sentence.print_text()
#     print("Žodžių skaičius:", sentence.count_words())
#     print("Simbolių skaičius:", sentence.count_characters())
#     print("Skaičių skaičius:", sentence.count_digits())
#     print("Raidžių skaičius:", sentence.count_letters())
#     print("-"*50)


#####################################################################

# class AccessExample:
#     def __init__(self):
#         self.public_variable = "Public"
#         self._protected_variable = "Protected"
#         self.__private_variable = "Private"
    
#     def public_method(self):
#         print("Public method")
    
#     def _protected_method(self):
#         print("Protected method")
    
#     def __private_method(self):
#         print("Private method")

#     def test(self):
#         print("Test")
#         self.public_method()
#         self._protected_method()
#         self.__private_method()
#         print(self.public_variable)
#         print(self._protected_variable)
#         print(self.__private_variable)



# access_example = AccessExample()
# print(access_example.public_variable)
# print(access_example._protected_variable) # neturetume kviesti už šios klasės ribų
# print(access_example._AccessExample__private_variable) # neturetume kviesti už šios klasės ribų

# print("*"*50)
# access_example.public_method()
# access_example._protected_method() # neturetume kviesti už šios klasės ribų
# access_example._AccessExample__private_method() # neturetume kviesti už šios klasės ribų\
# print("*"*50)
# access_example.test()

# import datetime


# class User:
#     def __init__(self, name, birth_date):
#         self.name = name
#         self.set_birth_date(birth_date)
        
#     def get_birth_date(self):
#         return self.__birth_date
    
#     def set_birth_date(self, new_birth_date):
#         try:
#             self.__birth_date = datetime.datetime.strptime(new_birth_date, "%Y-%m-%d").date()
#         except ValueError:
#             raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        






# user = User("Rokas", "1993-01-10")
# print(user.name)

# print(user.get_birth_date())


# user.set_birth_date("1994-02-20")

# print(user.get_birth_date())





# def test1():
#     test2()


# def test2():
#     print("test2")




# test1()

class Irasas:
    def __init__(self, tipas, suma):
        self.__tipas = tipas
        self.__suma = suma

    def pakeisti_tipa(self, tipas):
        if tipas not in ["Pajamos", "Islaidos"]:
            raise ValueError("Tipas gali buti tik 'Pajamos' arba 'Islaidos'")
        self.__tipas = tipas

    def pakeisti_suma(self, suma):
        if suma < 0:
            raise ValueError("Suma negali buti mazesne uz 0")
        self.__suma = suma

    def __str__(self):
        return f"{self.__tipas}: {self.__suma}"


class Biudzetas:
    def __init__(self):
        self.irasai : list[Irasas] = []

    def prideti_irasus(self, tipas, suma):
        irasas = Irasas(tipas, suma)
        self.irasai.append(irasas)

    def pakeisti_irasa(self, index, tipas, suma):
        self.irasai[index].pakeisti_suma(suma)
        self.irasai[index].pakeisti_tipa(tipas)


    def atvaizduoti(self):
        for irasas in self.irasai:
            print(irasas)



biudzetas = Biudzetas()




biudzetas.prideti_irasus("Pajamos", 1000)
biudzetas.prideti_irasus("Islaidos", 500)
biudzetas.prideti_irasus("Pajamos", 2000)

biudzetas.pakeisti_irasa(0, "Islaidos", 600)


biudzetas.atvaizduoti()

