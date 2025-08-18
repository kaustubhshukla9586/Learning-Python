import random
import time

while True:

    print("Welcome to Number Game. Here you have to guess the number between the chosen range.")
    time.sleep(1)
    game_range = int(input("Enter the range in which you want to play ( 10 - Easy ) , ( 100 - Medium ) , ( 1000 Hard ) , ( 10000 - Impossible ): "))
    time.sleep(1)

    valid = [10,100,1000,10000]

    while game_range not in valid:
        print("Can't Even Type a Number now? I'll ask again now.")
        game_range = int(input("Enter the range (10/100/1000/10000): "))

    if game_range == 10:
        print("Fairly easy one you choose, NGL")
    elif game_range == 100:
        print("Well this one is little hard but not that hard")
    elif game_range == 1000:
        print("HAHAHAH bro thinks he can do this lmaooo")
    elif game_range == 10000:
        print("you aint doing that bro because you're not him ")

    time.sleep(1)

    num = random.randint(1, game_range)
    attempts = 0

    while True:
        user_guess = input(f"Enter the guess between 1 and {game_range} ( q to quit) : ").strip().lower()
        attempts += 1
        if attempts == 10:
            print(f"Uh-oh! You used all your attempts but still couldn't guess it. The number was {num}.")
            break

        if user_guess == "q":
            print("Okay Pussy, Bye")
            break

        user_guess = int(user_guess)

        print(f"{10 - attempts} attempts left")
        if user_guess == num:
            print(f"Gawd damm! Well played — you got it in {attempts} tries 🎉")
            break
        elif attempts == '10':
            print(f"Uh-oh ! You used all your attempts but still couldn't guess it.")
            break
        elif abs(user_guess - num) <= max(2, game_range // 50):
            print("Very close! 🔥")
        elif user_guess > num:
            print("Too high! 📈 Try a smaller number.")
        else:
            print("Too low! 📉 Try a bigger number.")


    play_again = input("Would you like to play again? (y/n) : ").lower().strip()
    if play_again == "y":
        continue
    else:
        break




