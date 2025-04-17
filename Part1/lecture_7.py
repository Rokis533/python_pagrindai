
import os
import datetime 

file_info = os.stat("kortu_zaidimas.md")

print(datetime.datetime.fromtimestamp(file_info.st_mtime))

print(file_info.st_size / 1024, "kb")

# failo atidarymo tipai
# w - write to file
# a - append to file
# r - read file

# w+ - write and read to file
# a+ - append and read to file
# r+ - read and write file

# wb - write to binary file
# ab - append to binary file
# rb - read binary file

# with open("test.txt", "w") as failas:
#     failas.write("Labas\n")
#     failas.write("Sveiki\n")
#     failas.write("Ahoy\n")
    

# failas = open("test.txt", "w")

# failas.write("Labas\n")
# failas.write("Sveiki\n")
# failas.write("Ahoy\n")

# failas.close()


# with open("test.txt", "r+", encoding="UTF-8") as failas:
#     print(failas.read())
#     failas.seek(0)
#     failas.write("Cao\n")
#     failas.write("Salve\n")

# with open("test.txt", "a") as failas:
#     failas.write("Labas\n")
#     failas.write("Sveiki\n")
#     failas.write("Ahoy\n")

# with open("test.txt", "r", encoding="UTF-8") as failas:
#     text= failas.read()
#     for index, char in enumerate(text):
#         print(f"'{index}. {char}'")

# with open("test.txt", "r", encoding="UTF-8") as failas:
#     for line in failas:
#         if line.find("Labas") is -1:
#             print(line, end="")


# with open("test.txt", "r", encoding="UTF-8") as failas:
#     print(failas.read(10))
#     print(failas.read(10))
#     print(failas.read(10))
#     print(failas.read(10))
#     print(failas.read(10))

# with open("test.txt", "r", encoding="UTF-8") as failas:
#     with open("poetry_copy.txt", "w", encoding="UTF-8") as kopija:
#         for line in failas:
#             kopija.write(line)


# with open("download.png", "rb") as failas:
#     with open("codeacademy_logo.png", "wb") as kopija:
#         for line in failas:
#             kopija.write(line)


import pickle

def save_to_file(filename, variable):
    with open(filename, "wb") as failas:
        pickle.dump(variable, failas)

def load_from_file(filename):
    with open(filename, "rb") as failas:
        return pickle.load(failas)


# a = 99999999999

# with open("variable_a.pkl", "wb") as failas:
#     pickle.dump(a, failas)

# with open("variable_a.pkl", "rb") as failas:
#     result = pickle.load(failas)

# print(result)
# user = {'name': 'Rokas', 'age': 30, 'location': 'Kaunas'}

# save_to_file("variable_a.pkl", user)

# print(load_from_file("variable_a.pkl"))


# a = 1
# b = 2
# c = 5


# with open("variables_abc.pkl", "wb") as failas:
#     pickle.dump(a, failas)
#     pickle.dump(b, failas)
#     pickle.dump(c, failas)

# with open("variables_abc.pkl", "rb") as failas:
#     while True:
#         try:
#             x = pickle.load(failas)
#             print(x)
#         except EOFError:
#             break


# with open("test_title.txt", "w") as failas:
#     text = "Lord of the rings"
#     text = text.center(50, " ")
#     failas.write(text)


# with open("test.txt", "r", encoding="UTF-8") as failas:
#     with open("poetry_copy.txt", "w", encoding="UTF-8") as kopija:
#         for line in failas:

#             line = line.replace("\n", "")
#             line = line.center(50, " ")
#             line = line + "\n"
#             kopija.write(line)


with open("test.txt", "r", encoding="utf-8") as failas:
    text = failas.read()
    print(text)
    print("--------------------------------------------------")
    failas.seek(0)
    lines = failas.readlines()
    print(lines)
    print("--------------------------------------------------")

