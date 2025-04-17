
# funkcijos aprašymas
# def greeting(name):
#     print("hello!")
#     print(f"     {name},")



# funkcijos iškvietimas
# vardas = input("Įveskite savo varda: ")
# greeting(vardas)

###############################################################

# def pakelk_kvadratu(number):
#     kvadratas = number * number
#     print(f"Kvadratas skaičiaus {number} yra {kvadratas}")



# def daugyba(x, y):
#     result = x * y
#     return result



# a = 5
# b = 3

# daugyba_result = daugyba(a, b)

# print(daugyba_result)

# while True:
#     number = int(input("Iveskite skaiciu: "))

#     pakelk_kvadratu(number)


###############################################################


# def skaiciuokle(x, y, z, j = 0):
#     result = x * y
#     result = result + z + j

#     return result


# skaiciuokle_result = skaiciuokle( 5, 9, 7)

# print(skaiciuokle_result)


###############################################################

# def teksto_manipuliacija(text:str, to_upper:bool = False, to_lower:bool = False) -> str:
#     """ 
#     Šita funkcija keičia teksta ir gražinajį pakeistą.
#     Args:
#         text: Tai yra teksto kintamasis kuris bus manipuliuojamas
#         to_upper: Jei True tai pavers text į didžiasias
#         to_lower: Jei True tai pavers text į mažasias
    
#     Returns:
#         Ši funkcija gražina pakeistą textą
#     """
#     if to_upper:
#         text = text.upper()
#     if to_lower:
#         text = text.lower()
#     return text


# def text_input():
#     while True:
#         text = input("Iveskite teksta: ")
#         if text.count() > 5:
#             return text
    


# def run():
#     text = text_input()

#     naujas_textas = teksto_manipuliacija(text, to_upper=True)

#     print(naujas_textas)

    



# run()

# text= "Labas"

# naujas_textas = teksto_manipuliacija("sadas")

# naujas_textas

# print(naujas_textas)


###############################################################\

# def spausdinimas(name, *args):
#     for number in args:
#         print(name , number)

# def spausdinimas(start, end, **kwargs):
#     for key, value in kwargs.items():
#         print(start, key, " ", value)


# # my_list = [5,9,8]

# spausdinimas("Rokas",5,6,7,2,8,7,2)

# spausdinimas(1, 9, Rokas = 5, Tomas = 9, Antanas = 6)


###############################################################\


# def get_initial_coordinates():
#     x = 0
#     y = 0
#     z = 0
#     return x, y, z


# x, y, z = get_initial_coordinates()


# print("x: ", x)
# print("y: ", y)
# print("z: ", z)


# globalus = 10

# def skaiciavimas():
#     global globalus 

#     localus = 20
#     globalus = 9999
#     return localus + globalus


# print(globalus)
# print(skaiciavimas())
# print(globalus)




def run_task_1_1():
    x = 0
    print("hello")

def run_task_1_2():
    x = 0
    print("hello")

def dalyba_is_2_example(x):
    return x / 2

def run_lambda_example():
    

    # dalyba_is_2 = lambda x: x / 2

    # result = dalyba_is_2(5)

    # print(result)

    # my_list = [1,5,6]

    # my_list_new_example = []
    # for i in my_list:
    #     x = dalyba_is_2_example(i)
    #     my_list_new_example.append(x)
    
    # print("*"*50)
    # for i in my_list_new_example:
    #     print(i)

    # my_list_new = map(lambda x: x % 2, my_list)
    # print("*"*50)
    # for i in my_list_new:
    #     print(i)

    my_list = ["Rokas", "Mantas", "Antanas", "Samsung", "445", "rokas"]

    # my_list_new = list(map(lambda x: len(x) <= 5, my_list))
    # my_list_new = list(filter(lambda x: len(x) <= 5, my_list))
    my_list_new = list(filter(lambda x: not x.isdigit(), my_list))
    # my_list_new = my_list
    # my_list_new = sorted(my_list, key=lambda x: len(x))
    # my_list_new.sort( key=lambda x: "~" if x.isdigit() else x)
    # my_list_new.sort()
    print("*"*50)
    for i in my_list_new:
        print(i)


    pass

# my_list = []
# for i in range(1,5):
#     my_list.append(i)

def run_inline_loop():

    # my_list = [i / 2  for i in range(1,5)]
    # my_list_lambda = [lambda x = i: x / 2  for i in range(1,5)]

    # for i in my_list:
    #     print(i)
    
    # print("*"*50)
    # for i in my_list_lambda:
    #     print(i())
    # my_list = []
    # for i in range(1,10):
    #     if i % 2 == 0:
    #         my_list.append(i / 2)

    # #         | 3     |        1           |     2       |
    # my_list = [i / 2  for i in range(1,10) if i % 2 == 0]
    # my_list_lambda = [lambda x = i: x / 2  for i in range(1,10) if i % 2 == 0]

    # for i in my_list:
    #     print(i)
    
    # print("*"*50)
    # for i in my_list_lambda:
    #     print(i())

    pass


# def skaiciavimas(x):
#     return x * 2

# run_task_1_1()
# run_task_1_2()
run_lambda_example()
# run_inline_loop()





