import random

print("Welcome to Snake , Water , Gun  Game!")
print("Rules: Snake drinks Water, Water douses Gun, Gun kills Snake\n")

choices = ["snake", "water", "gun"]

while True:
    # Player's choice
    user_choice = input("Enter your choice (snake/water/gun or quit): ").lower()
    
    if user_choice == "quit":
        print("Thanks for playing! Goodbye ")
        break

    if user_choice not in choices:
        print("Invalid choice, try again!")
        continue

    # Computer's choice
    comp_choice = random.choice(choices)
    print(f"Computer chose: {comp_choice}")

    # Decide winner
    if user_choice == comp_choice:
        print("🤝 It's a tie!")
    elif (user_choice == "snake" and comp_choice == "water") or \
         (user_choice == "water" and comp_choice == "gun") or \
         (user_choice == "gun" and comp_choice == "snake"):
        print("You win!")
    else:
        print(" Computer wins!")

    print("-" * 30)
