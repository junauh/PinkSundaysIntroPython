import random

guess_count = 0
chances_left = 5

WordList = ["hello", "pink", "programming", "python"]
random.shuffle(WordList)

answer = list(WordList[0])

display = []
used = []

display.extend(answer)
used.extend(display)

for i in range(len(display)):
    display[i] = "-"

print(" ".join(display))
print()

while guess_count < len(answer) and chances_left > 0:
    guess = input("Please guess a letter: ")
    # convert the letter to a lower case
    guess = guess.lower()
    print(guess_count)

    for i in range(len(answer)):
        if answer[i] == guess and guess in used:
            display[i] = guess
            guess_count = guess_count + 1

            used.remove(guess)

    if guess not in display:
        chances_left = chances_left-1
        print("Sorry, Wrong guess")
    print("You have : ", guess_count, "correct letters")
    print("You have : ", chances_left, "chances left")

    print(' '.join(display))
    print()


if guess_count == len(answer):
    print("******************************")
    print("Congratulations, well done!")
    print("******************************")

else:
    print("------------------------------------")
    print("'Game Over :( No more chances left.")
    print("------------------------------------")