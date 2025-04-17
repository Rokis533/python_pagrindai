
# my_list = [1, 2, "shdjas", 3, 4, 5]

# lambda x: x * 2


# my_new_list = map(lambda x: x * 10 if isinstance(x,(int,float)) else None , my_list)



# my_new_list = map(lambda x: "Tai yra skaicius" if isinstance(x,(int,float)) else "Tai yra ne skaicius" , my_list)

# print(list(my_new_list))

# for i in my_new_list:
#     print(i)


# my_centimeter_list = [1, 2, 3, 4, 5]
# my_inch_list = map(lambda x: x / 2.54, my_centimeter_list)

# print(list(my_inch_list))

# my_file_paths = ["C:/Users/Rokas/Desktop/1.txt", "C:/Users/Rokas/Desktop/2.txt", "C:/Users/Rokas/Desktop/3.txt"]
# my_mac_os_file_paths = list(map(lambda x: x.replace("C:/", ""), my_file_paths))

# replace_char = '\\'
# # idomu kodel neveikia replace exacaped char
# my_linux_file_paths = list(map(lambda x: x.replace("/", "\\\\"), my_mac_os_file_paths))
# my_linux_file_paths = list(map(lambda x: x.replace("\\\\", "\\"), my_linux_file_paths))

# # my_mac_os_file_paths = ["Users/Rokas/Desktop/1.txt", "Users/Rokas/Desktop/2.txt", "Users/Rokas/Desktop/3.txt"]

# print(my_mac_os_file_paths)
# print(my_linux_file_paths)


# text = "C:/Users/Rokas/Desktop/1.txt"
# text = text.replace("/", "\\")

# print(text)

# Sample list of strings with double backslashes
# strings = ["path\\to\\file"]
 
# # Use map function to replace double backslashes with a single backslash
# result = list(map(lambda x: x.replace("\\\\", "\\"), strings))
# # print(result)
# # result = [x.replace("\\\\", "\\") for x in strings]
 
# # Print the result

# # print(result)

# for i in result:
#     print(f"String0: {i}, Repr: {repr(i)}")

# print(my_new_list)
# print(list(my_new_list))

# my_str_list = "labas, kaip sekasi".split(" ")

# print(my_str_list)

# my_new_str_list = map(lambda x: x.upper(), my_str_list)

# print(list(my_new_str_list))

# data = "2021-10-22"

# y, m, d = map(int, data.split("-"))
# print(y, m, d)
# print(type(y), type(m), type(d))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# my_list = [1, 2, 3, 4, 5]
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_new_list = filter(is_prime, my_list)

# print(list(my_new_list))

# my_list = [1,25,3,2,1,4,5,9,7,5,2,6,4,2,6]
# mean = sum(my_list) / len(my_list)
# print(mean)
# my_new_list = filter(lambda x: abs(mean - x) < 3 , my_list)
# print(list(my_new_list))


# from functools import reduce

# my_list = [1, 2, 3, 4]


# # y: x*(x + y)

# # x: 1*(1 + 2) = 3          [3, 3, 4]
# # x: 3*(3 + 3) = 18         [18, 4]
# # x: 18*(18 + 4) = 396      396
# my_sum = reduce(lambda x, y: x*(x + y) , my_list)

# print(my_sum)

# my_str_list = ["Rokas", "Slaboševičius"]
# my_str_sum = reduce(lambda x, y: x + " " + y[0] , my_str_list)
# print(my_str_sum)


class Irasas:
    def __init__(self, suma, kiekis):
        self.suma = suma
        self.kiekis = kiekis

    def __str__(self):
        return f"Str: {self.__class__.__name__}: {self.suma}, kiekis: {self.kiekis}"
    
    def __repr__(self):
        return f"Repr: {self.__class__.__name__}({self.suma}), {self.kiekis}"


class Pajamos(Irasas):
    pass

class Islaidos(Irasas):
    pass

# from operator import attrgetter

# list_of_records = [Pajamos(100, 5), Pajamos(200, 4), Islaidos(100, 6), Pajamos(300, 2), Islaidos(100, 4)]


# # sorted_list = sorted(list_of_records, key=lambda x: x.suma, reverse=True)
# sorted_list = sorted(list_of_records, key=attrgetter("suma", "kiekis"), reverse=True)
# # print(list_of_records) #using repr


# for record in sorted_list:
#     print(record) # using str


# pajamos_sum = reduce(lambda x, y: x + y.suma if isinstance(y, Pajamos) else x.suma, list_of_records)
# islaidos_sum = reduce(lambda x, y: x + y.suma if isinstance(y, Islaidos) else x.suma, list_of_records)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_new_list = [x*100 
#                for x in my_list 
#                     if x >= 5 and x <= 8]

# my_list_even = [x 
#                 for x in my_list 
#                     if x % 2 == 0]

# my_list_even_generator = (x 
#                             for x in my_list 
#                                 if x % 2 == 0)

# print(my_list_even)

# result = list(my_list_even_generator)
# for i in result:
#     print(i)

# print(list(my_list_even_generator))

# my_list = [5,9,7,5,3,1,4,5,2,9]

# # my_list.sort()
# # print(my_list)

# sordered_list = sorted(my_list, reverse=True)

# print(sordered_list)

my_list = [True, False, 1, 0]


new_list = filter(lambda x: x == False, my_list)
print(list(new_list))

new_list = filter(lambda x: x is False, my_list)
print(list(new_list))