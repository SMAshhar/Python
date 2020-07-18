Alien_Colour = ["green", "yellow", "blue", "red", "death"]
import random


b = random.randint(0, 2 )
a = Alien_Colour[b]
c = True
y = 0
score = [40, 30, 20]
while c == True:
    
    x = input("Try your hitting an alien")
    if x.lower() != "q":
        b = random.randint(0, 4)
        a = Alien_Colour[b]
        
        if a == "yellow":
            print("Nice... you got a yellow one, 5 points")
            y += 5
        elif a == "green":
            print("Awesome... there goes the green one, 10 points")
            y += 10
        elif a == "blue":
            print("WoW... another blue bites the dust, 15 points")
            y += 15
        elif a == "red":
            print("An Epic kill.... a red down, 20 points")
            y += 20
        elif a == "death":
            print("The aliens finally caught you despite your great heroism and courage.")
            print("gameover")
            print("Your total score is ", y)
            break
    else:
        print("Your total score is ", y)
        break
if score[0] < y:
    score.insert(0, y)
print(f"""
    Top high scores are :
    {score[0]}
    {score[1]}
    {score[3]}
    """)