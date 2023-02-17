from random import randint

username=input("what is your name:")

print("hello there"+" "+username)
random_number=randint(10,50)

counter=0
while counter <5:
    user_number=eval(input("enter a random number between 10 and 50 :"))
    counter += 1

    if user_number<random_number:
        print("your guess is too low")
    elif user_number>random_number:
        print("yor guess is too high")
    elif user_number==random_number:
       
        break


if user_number ==random_number:

  print("you win! ")
else:
    print("Game over! The corect number was:" ,random_number)
    

