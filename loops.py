import random

#exercise 1
for i in range(1, 11):
    print(i)

#exercise 2
password=""
while password != "python123":
    password=input("write the right password ")
    if password !="python123":
        print("wrong password")
print("access granted")

#exercise 3
computer=random.randint(1, 10)
guess =0

while guess !=computer:
    guess=int(input("chosse between 1 and 10"))
    if guess>computer :
        print("too high")
    elif guess <computer:
        print("too  low")
    else :
        print(" you guess it")

#exercise 4
for i in range(2, 21, 2):
    print(i)

#exercise 5
password_user=""
while password_user != "hello world":
    password_user=input("type the correct password ").lower()
    if password_user != "hello world":
        print("try again")
print("access granted")

#exercise 6
print("PLAY THE GAME: GUESS THE NUMBER")
computer=random.randint(1, 5)
guess =0

while guess !=computer :
    guess=int(input("choose the right number "))
    if guess !=computer:
        print("try again")
print("CORRECT!")
