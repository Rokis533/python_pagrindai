

# class User:
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password

#     def print_hello(self):
#         print(f"Hello {self.name}")


# class UserAdmin(User):
#     def __init__(self, name, password, admin_code):
#         super().__init__(name, password)
#         self.admin_code = admin_code

#     def my_admin_code(self):
#         print(f"Admin code is: {self.admin_code}")

# class Manager(User):
#     def __init__(self, name, password, manager_code):
#         super().__init__(name, password)
#         self.manager_code = manager_code

#     def my_manager_code(self):
#         print(f"Manager code is: {self.manager_code}")

# class Viewer(User):
#     def __init__(self, name, password, viewer_code):
#         super().__init__(name, password)
#         self.viewer_code = viewer_code

#     def my_viewer_code(self):
#         print(f"Viewer code is: {self.viewer_code}")






# class SuperAdmin(UserAdmin):
#     def __init__(self, name, password, admin_code, super_admin_code):
#         super().__init__(name, password, admin_code)
#         self.super_admin_code = super_admin_code

#     def my_super_admin_code(self):
#         print(f"Super admin code is: {self.super_admin_code}")


# """
# class UserAdmin(User):
#     def __init__(self, name, password, admin_code):
#         self.name = name
#         self.password = password
#         self.admin_code = admin_code
    
#     def print_hello(self):
#         print(f"Hello {self.name}")

# """

# user_admin = UserAdmin("Rokas", "1234", "admin")

# user_admin.print_hello()
# user_admin.my_admin_code()

# print("-"*50)

# user = User("Tomas", "1234")
# user.print_hello()
# user.my_admin_code()


# print(user_admin.name)


##################################################################


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_hello(self):
        print(f"Hello {self.name}")


class User(Person):
    def __init__(self, name, age, location=None):
        super().__init__(name, age)
        self.location = location
    
    def print_hello(self):
        # super().print_hello()
        print(f"Yoo Yo yo, my name is {self.name} my home is {self.location}")

    def print_location(self):
        print(f"My location is {self.location}")


class Student(Person):
    pass

class Teacher(Person):
    def print_hello(self):
        print(f"Good morning, students, my name is {self.name}")



user = User("Rokas", 30, "Vilnius")
student = Student("Tomas", 20)
teacher = Teacher("Antanas", 20)

list_of_users : list[Person] = [user, student, teacher]


for user in list_of_users:
    

    if isinstance(user, Person):
        print("This is a person")
        user.print_hello()

    if isinstance(user, User):
        user.print_location()

    print("-"*50)



class ElektrosPrietaisas:
    def __init__(self, pavadinimas, galia_vatais):
        self.pavadinimas = pavadinimas
        self.galia_vatais = galia_vatais
        self.ijungtas = False
    
    def ijungti(self):
        self.ijungtas = True
        return f"{self.pavadinimas} įjungtas."
    
    def isjungti(self):
        self.ijungtas = False
        return f"{self.pavadinimas} išjungtas."
    
    def energijos_sanaudos(self, valandos):
        if not self.ijungtas:
            return 0
        return self.galia_vatais * valandos / 1000  # kWh
    
    def __str__(self):
        busena = "įjungtas" if self.ijungtas else "išjungtas"
        return f"{self.pavadinimas} ({self.galia_vatais}W) - {busena}"


class Kompiuteris(ElektrosPrietaisas):
    def __init__(self, pavadinimas, galia_vatais, tipas):
        super().__init__(pavadinimas, galia_vatais)
        self.tipas = tipas


kompas = Kompiuteris("Asus", 500, "Nešiojamas")
kompas.ijungti()


# Užduotis: Sukurkite paveldėtas klases Kompiuteris ir Televizorius


# Užduotis: Sukurkite skirtingų prietaisų sąrašą ir apskaičiuokite energijos suvartojimą


# Papildoma užduotis: Sukurkite funkciją, kuri parodo, kuris prietaisas suvartoja daugiausiai energijos per nurodytą laiką
