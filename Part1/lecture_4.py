# my_list = [1, 2, 3, 4, 5]


# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])

# suma = 0
# for item in my_list:
#     suma += item

# print(suma)


# for item in my_list:
#     print(item)


# print("Done!")



# print(list(range(10))) 


# for i in range(100):
#     print(f"dabar eina {i} ciklo iteracija")
#     print("Hello!")


############################################################

# my_dict = {
#     "apple": 9,
#     "banana": 2,
#     "cherry": 4,
#     "date": 4,
#     "elderberry": 5
# }

# for item in my_dict:
#     print(item)

# print("-------------------")

# for item in my_dict.values():
#     print(item)

# print("-------------------")


# total_price = 0
# print("-"*40)
# for key, value in my_dict.items():
#     total_price += value
#     print(f"{key:<15} {value} Eur")
#     print("-"*40)


# print(f"Total price:   {total_price} Eur")
# print("-"*40)

############################################################

# for i in range(1000, 1100, 10):
#     print(f"dabar eina {i} ciklo iteracija")


############################################################

# my_list = [5, 2, 9, 4, 3]

# print(my_list[0])
# print(my_list[2])

# lenght = len(my_list)


# for index in range(lenght):
#     item = my_list[index]
#     print(f"Index: {index}, Value: {item}")

# for item in my_list:
#     print(f"Value: {item}")

############################################################


# names = ["rokas", "antanas", "tomas", "lukas", "marius", "kazys"]

# i = 0

# surasta = False

# while not surasta :
#     if names[i] == "lukas":
#         print(f"{i} Radau Luką!")
#         surasta = True
#         # break
#     else:
#         print(f"bandom {i} kartą")

#     i += 1

# for name in names:
#     if name == "lukas":
#         print(f"Radau Luką!")
#         break
#     else:
#         print(f"bandom toliau")

names = ["rokas", "antanas", "tomas", "mukas", "marius", "kazys"]


# for name in names:
#     if len(name) != 6:
#         continue

#     print(f"Vardas: {name}")


    
for name in names:
    if name == "lukas":
        print(f"Radau Luką!")
        break
    else:
        print(f"bandom toliau")
else:
    print("Neradau Luko")


print("Done!")
