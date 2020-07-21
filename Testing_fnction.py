
# def x():
#     if a == b and c == d:
#         print("Great; you won the first prize")
#     else:
#         print("better luck next time")

# print("\t\t==============================================\t\t")
# a = input(print("\t\t Try your luck, Enter YOUR first number"))
# b = input(print("\t\t Try your luck, Enter YOUR second number"))
# c = input(print("\t\t Try your luck, Enter YOUR third number"))
# d = input(print("\t\t Try your luck, Enter YOUR forth number"))
# print("\t\t==============================================\t\t")

# x()

# def x(a, b):
#     print(a + b)
# x(2, 3)

# def qrd(a, b):

#     x = (a + b) * (a - b)

#     print(x)

# d = float(input(print("Enter your first number: ")))
# c = float(input(print("Enter your second number: ")))

# qrd(b = 3, a = 9)


# def fullName(first, last, middle = " "):
#     print(first, middle, last)

# fullName(last = "Syed", middle="Muhammad", first = "Ashhar")
# # x = str(input(print("Enter your First Name")))
# # y = str(input(print("Enter your Middle Name; (press Enter if your don't have one)")))
# # z = str(input(print("Enter your Last Name")))

# x, y, z = str(input(print("Enter your Full name"))).split()
# fullName(first = x, middle = y, last = z)


# RETURNING A FUNCTION

# def pizzaOrder(size, flavour, *toppings):
#     print(f"Your order of {size} inch pizza of {flavour} flavour and {toppings} as toppings is confirmed")
#     return size, flavour, toppings

# size, flavour, *toppings = str(input(print("Enter your size, flavour and toppings"))).split()
# print(pizzaOrder(size, flavour, *toppings))

# def table():
#     p = int(input(print("Number to be factorised")))
#     y = int(input(print("Table for?")))
#     print(f"\t\t Searching for factors of {y}")
#     for x in range(1500):
#         z = y * x
#         # print(f"\t\t {y} x {x} = ", z)
#         if z == p:
#             return x

# y = table()
# print("\t\t",y)

# name = "Ashhar"
# fname = "Shakeel"
# age = 23
# gender= "M"
# print(f"\nName : {name} \nFather Name : {fname} \nAge : {age} , Gender : {gender}")


# l1 = [1 +2 ,3 + 5]
# print(l1)

# name = "aisr"
# name.upper()
# print(name.upper())

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l1[0, 2, 3, 1, 5])



#LEARNING ** AND * PARAMETERS IN FUNCTINOS

# def game_status(winner, looser, score, **other_info):
#     print("The winnder was "+ winner)
#     print("The looser was " + looser)
#     print("The score was " + score)
#     for key, value in other_info.items():
#         print(key, " : ", value)


# game_status("Real Mandred", "Barcelona", "1-0", Overthrows = "None", Injuries = "None", Fouls = 15)


# def exam_result(English, Math, Science, Urdu, **others):
#     print(f"The score in English is {English}, math is {Math}, Science is {Science}, Urdu is {Urdu}.")
#     print("The scores for other subjects are :")
#     for key, value in others.items():
#         print(key, ":", value)

# exam_result(57, 99, 74, 20, Social_Studies = 57, Sindhi = 60, Computer_Science = 100)

# def calling_cards(first, second, third, *rest):
#     print(first, second, third, *rest)

# calling_cards(12, 45, 895, 20, 456, 2113)

# def noise(**type):
#     for key, value in type.items():
#         print(key, value)
#     print(type)
    

# noise(asdf = "Hellow", afg= "there", wetwer="confusing", afgtrj= "code")

# defining_dictionary = {
#     0 : {
#         1 : "Jons",
#         2 : "Millers",
#     },
# }

# print(defining_dictionary)

# def sing():
#     y = "2"
#     print(y)
# y = "1"
# sing()
# print(y)


#FUNCTION WITH WHILE LOOP

# entry = {}


# def register():
#     flag = True
#     x = 1
#     while flag:
#         fname = input("Please enter your first name :")
#         lname = input("Please enter your last name : ")
#         father_name = input("Please enter your father's name : ")

        
        
#         roll_number = f"PIAIC{x}"
#         x += 1      

#         print(f"""
#         Name = {fname} {lname}
#         Father's Name = {father_name}
#         Roll Number = {roll_number}
#         """)
#         entry[roll_number] = [fname, lname, father_name]
        
      

#         print(entry[roll_number])

#         y = input("Do you want to register another? Press N to terminate")

#         if y == "N" or y == "n":
#             flag = False
#         else:
#             flag = True

# register()

# print(entry)

#SAMPLE DICTIONARY

Student_information = {
    "AI" : {
        "PIAIC1" : {"Name" : "Syed Muhammad Ashhar",
        "Father's Name" : "Syed Muhammad Shakeel",
        "Roll Number" : "PIAIC1",
        },
        "PIAIC2" : {"Name" : "Syed Muhammad Nawal",
        "Father's Name" : "Syed Muhammad Shakeel",
        "Roll Number" : "PIAIC2",}
        },
    "CNC" : {
        "PIAIC3" : {"Name" : "Syeda Mirha Ashhar",},
        "PIAIC4" : {"Name" : "Syeda Eshe Ashhar",},
        },
    "IOT" : {
        "PIAIC5" : {"Name" : "Rubab Adil"},
        },
}

# x = Student_information["AI"]["PIAIC2"]["Name"]

# # print(f"{x}")

# print(Student_information)

for s in Student_information.keys():
    print(Student_information[s])





