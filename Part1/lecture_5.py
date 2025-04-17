

# my_variable  = True
# my_variable = False

# print(my_variable)


# my_variable = 5 < 10 

# print(my_variable)

# should_continue = False


# if my_variable:
#     print("Yes")
#     should_continue = True
# else:
#     print("No")
#     should_continue = False


# print(should_continue)
# print("End of program")



####################################################################\

# my_int = 5
# my_float = 5.0
# my_string = "5"
# my_bool = True
# my_list = [1, 2, 3]
# my_tuple = (1, 2, 3)
# my_set = {1, 2, 3}
# my_dict = {'key': 'value'}

# print(type(my_int))
# print(type(my_float))
# print(type(my_string))
# print(type(my_bool))
# print(type(my_list))
# print(type(my_tuple))
# print(type(my_set))
# print(type(my_dict))

# new_list = [1, 5, "string", "10", True, 5.0, (1,2), {1,2}, {'key': 'value'}]


# # if type(my_int) == type(5):
# #     print("same type")

# my_sum = 0

# for item in new_list:
#     # print(item, type(item))
#     if type(item) == int or type(item) == float:
#         my_sum += item

#     if type(item) == str and item.isnumeric():
#         my_sum += int(item)

#     if type(item) == tuple:
#         # my_sum += sum(item)
#         for number in item:
#             if type(number) == int or type(number) == float:
#                 my_sum += number


# print(my_sum)
        

####################################################################\

import datetime


# print(datetime.datetime.now())
# print(datetime.date.today())
# print(datetime.datetime.today().time())

# x_date = datetime.date.today()

# my_date = datetime.date(2025, 1, 25)

# print(type(x_date))
# print(x_date)


# print(type(my_date))
# print(my_date)

# if x_date < my_date:
#     print("X mažiau")
# else:
#     print("daugiau")


# print()

# my_date = datetime.datetime.now()

# print(my_date)

# # my_date -= datetime.timedelta(days= 1)
# # my_date += datetime.timedelta(days= 1, hours=14)

# my_date_diference = my_date - datetime.datetime(2000, 1, 1 )

# print(my_date_diference)

# print( f"{my_date_diference.days // 7} weeks")




# print(my_date.strftime("%Y * %m * %d - %H : %M : %S : %f"))
# print(my_date.strftime("%Y * %B * %A * %d - %H : %M : %S : %f"))


# text = input("Iveskite data(YYYY-MM-DD H:M:S): ")

# print(text)
# print(type(text))

# my_date = datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S")

# print(my_date)
# print(type(my_date))

# my_date_diference = datetime.datetime.now() - my_date 

# print(f"Nuo datos praejo: {my_date_diference.days} dienos")



####################################################################\

# import traceback

# try:
#     number = int(input("Ivesk skaiciu su kuriuo dalinsim 5: "))
#     my_number = 5 / number
#     datetime.datetime.strptime(number, "%Y-%m-%d %H:%M:%S")
# except ZeroDivisionError:
#     print("Ups ivyko klaida dalybos iš nulio, dalyti iš nulio negalima, prašome įvesti skaičiu kuris nera 0")
# except ValueError:
#     print("jus įvedete ne skaičių, prašome įvesti skaičiu")
# except Exception as ex:
#     print(ex)

#     tb = traceback.extract_tb(ex.__traceback__)

#     for x in tb:
#         print(f"Eilutes nr {x.lineno}")

#     print("sorry, įvyko nenumatyta klaida, praneškite administratoriui")

number = None

while True:
    try:
        number = int(input("iveksite skaiciu: "))
        if number < 0:
            raise ValueError("Skaičius yra negatyvus")
        
        if number > 100:
            raise ValueError("Skaičius yra daugiau nei 100")
        
        break

    except Exception as ex:
        print("Klaida yra: ", ex)


print(number)



