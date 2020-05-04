import random

true_number = random.randint(1, 100)
print (true_number)
guessNumber = int(input("please enter a number between 1 to 100: "))
count = 0
state = True
while state:
    if true_number > guessNumber:
        guessNumber = int(input("your guess is lower than the number \n try again:"))
        count += 1
    elif true_number < guessNumber:
        guessNumber = int(input("your guess is higher than the number \n try again:"))
        count += 1
    else:
        print(" you guessed the number correctly! congratulations! it take you ", count, "attempts \n")
        continue_play = input("want to continue play ? (y/n)")

        if continue_play == 'n':
            state = False
        else:
            true_number = random.randint(1, 100)
            print(true_number)
            count = 0
            guessNumber = int(input("please enter a number between 1 to 100: "))



