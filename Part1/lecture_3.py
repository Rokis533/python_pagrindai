


# list = [] # empty list
# list = [9, 2, "a", "b", [1, 2]] # list with diferent types of elements

#index= 0  1  2  3  4          5
# list = [9, 2, 4, 4, [3, 8, 9], 6] # list with 5 elements

#  0  1  2
# [3, 8, 9]

# list[4] = 7

# print(list[4][1])


# my_bank_transactions = [100, 600, -59, -28, -8, 1000]

# print(my_bank_transactions)

# new_transaction = int(input("Įveskite naują transakciją: "))

# my_bank_transactions.append(new_transaction)


# print(my_bank_transactions)


######################################################################################
#       0  1  2  3  4
# list = [1, 5, 9, 7, 6]

# print(list)

# droped_element = list.pop(2)

# print(list)
# print("Dropped value " + str(droped_element))


# print("List lenght: ", len(list))


# text = "Pirmadienis"

# text = text[::-1]
# print(text)

# text = text[0].replace("P", "p") + text[1:-1] 

# print(f"{text} yra {len(text)} simboliu")

# if text[0] == text[0].upper():
#     print("pirma dizioji raide didzioji")

######################################################################################


# list = [1, 5, 9, 7, 486]

# #         start, stop, step
# new_list = list[:2]
# new_list.extend(list[3:])

# print(list[:2] + list[3:])
# print(list[3:])

# list.extend([23,5,8])

# removed_element = list.pop(2)
# print(list)

# list.append(6)

# print(list)

######################################################################################

# text = "Rokas, Jonas, Tomas, Petras, Antanas"
# text = input("Įveskite vardus atskirtus kableliais: ")

# words = text.split(", ")

# # print(words[::-1])
# print(words)

# joined_text = " ".join(words)

# print(joined_text)


######################################################################################


# text = """
# Labas,
# Noriu pranesti, kad šiandien neateisiu į darbą, nes esu sergantis.
# Atsiprašau už nepatogumus.
# """

# print(text)

# new_text = text.splitlines()

# print(new_text)


######################################################################################

# Dictionaries
# key - value pairs
# key - unique
# value - can be anything

# roko_info = { 
#     'name': 'Rokas',
#     'age': 26,
#     'height': 1.85,
#     'weight': 80,
#     'is_student': False
# }

# antanas_info = { 
#     'name': 'Antanas',
#     'age': 31,
#     'height': 1.85,
#     'weight': 80,
#     'is_student': True
# }



# print(roko_info['name'])
# print(roko_info['is_student'])
# print()
# print(antanas_info['name'])
# print(antanas_info['is_student'])
# print()

# people = [roko_info, antanas_info]

# print(people[1]['name'])

# products = {
#     'apple': 1.5,
#     'banana': 2,
#     'orange': 3
# }

# products['apple'] = 0.99
# keys = products.keys()
# values = products.values()

# print(products)
# print(keys)
# print(values)

# grades = {
#     'rokas': [1,5,8,5,7],
#     'antanas': [5,8,6,],
#     'tomas': [5,6,4,6] 
# }

######################################################################################

# my_set = {1, 1, 3, 4, 5, 6, 7, 8, 9, 10}

# my_set.add(-1)

# print(my_set)

######################################################################################

# number = 5

# my_tuple = (2, 7,number)

# my_tuple = my_tuple + (3, 5)

# number = 6

# print(my_tuple)

######################################################################################

import time


my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
my_list = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)

start = time.perf_counter()

for i in range(100000):
    my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    pass

end = time.perf_counter()

print(f"Time it took to perform List: {(end - start)* 1000}ms")


start = time.perf_counter()

for i in range(100000):
    my_list = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
    pass

end = time.perf_counter()

print(f"Time it took to perform Tuple: {(end - start)* 1000}ms")







