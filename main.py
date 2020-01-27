import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False
range = 100

while not quit:
    random_number = random.randint(1,range)
    count = 1
    number = -1
    while (number) != random_number:
        number = input("Go on ahead- guess a number between 1 and {}: ".format(range))
        if not number.isdigit():
            print("What the... hey, uh... please type a number. Mkay?")
        else:
            number = int(number)
            count = count + 1
            print("... Oh dear. Um. That's not right.")
            if number > random_number:
                print("Nope, too high.")
            elif number < random_number:
                print("Eeehh... too low.")
    print("Awesome work!")
    print("You guessed the number in {} tries. Congratulations.".format(count))
    play_again = input("\nDo you wanna play again? If so, type yes or y. If not... well, go away.")
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y":
        quit = False
    else:
        quit = True

print("\n\nThanks for playing my first... uh... somewhat sucky game. Thing. Numbers guessing game! See you soon! ...or not. Hopefully I'll see you again!")