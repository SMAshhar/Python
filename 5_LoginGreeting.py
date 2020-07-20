current_usernames = ["admin", "v2fftb", "Ali", "Rubab", "Nawal"]

# 5-8 greet every login. Some oneway, the others the otherway
for a in current_usernames:
    username = input("Enter username: ")
    if username == "admin":
        print("Hello admin, would you like a report?")
        break
    elif username in current_usernames:
        print(f"Welcome back {username}. How can I make your world easy for you today?")
        break
    else:
        print("This username is not registered")


#-5-9 send a message if there is nothing in  a list
# while current_usernames:
#     current_usernames.pop()
# if current_usernames == []:
#     print(current_usernames)
#     print("We need more users")

# 5-10 Checking usernames
new_users = ["Imad", "Danish", "Ali", "Nawal", "Umer"]
for a in new_users:
    if a in current_usernames:
        print(a, " is not available, please enter a different name")
    else: 
        print(a, " username is available")