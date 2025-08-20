import random
attempts=0
while True:
    number=int(input("Enter the guess number between (50-80). "))
    attempts+=1
    if number <50 and number >80:
        print(f"The number is not in range of (50-80).Try number between given range.")
    elif number > random.randint(50,80):
        print("Your number is greater than actual number.Try Smaller number!")
    elif number < random.randint(50,80):
        print("Your number is smaller than actual number.Try greater number!")
    else:
        print(f"Congratulations! You guessed the right number in {attempts} attempts.")  
        break  