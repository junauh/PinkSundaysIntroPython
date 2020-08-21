# module : a collection of different classes, methods, and variables (single python file of methods)
# e.g. random() returns a random float r between 0, 1
# e.g. shuffle()
# -----------code : module import, variable assignment ----------------
import random

guess_count = 0
chances_left = 5
# -----------code----------------

# -----------hint : list, print, random.shuffle, list, length and extend method ----------------
# list : most basic data structure in python; sequence with index/position; can modify list
# list creation : list_L = []
# list index (starts from 0)
list_L = []
list_L = ['aAa', 'bBb', 'cCc', 'dDd', 'eEe']
print(list_L)
print(list_L[0])
print(list(list_L[0]))
print(list_L[4])

random.shuffle(list_L)
print(list_L)
print(list_L[0])
print(list(list_L[0]))
print(list_L[4])
print(len(list_L))

# append method will append the word/object 'PINK'
# extend method will append the 'contents' of sequence 'PINK' :'P','I','N','K'
# list_a = list_L
list_e = list_L
# list_a.append('PINK')
list_e.extend('PINK')
# print(list_a)
print(list_e)
# -----------hint----------------

# -----------code----------------

WordList = ['hello', 'pink', 'programming', 'python']
random.shuffle(WordList)

answer = list(WordList[0])

display = []
# print(display)
used =[]

display.extend(answer)
# print(display)

used.extend(display)
# -----------code----------------

# -----------hint : for loop , range and join method----------------
for i in range(5):
    print(i)

print(len('pink'))

pink = ['p', 'i', 'n', 'k']
hello = ['h', 'e', 'l', 'l', 'o']

print(pink)
print(hello)
for i in range(len(pink)):
    pink[i] = '-'

for i in range(len(hello)):
    hello[i] = '-'

print(pink)
print(hello)

print(' '.join(pink))
print(' '.join(hello))
# -----------hint----------------

# -----------code----------------

for i in range(len(display)):
    display[i] = '-'

print(' '.join(display))

count = 0
incorrect = 5
# -----------code----------------

# --------hint: while loop, input function, and if/elif/else statements -------
j = 0
while j < 5:
    # j = j + 1
    j =+ 1
    print(j)

Variable_a = input("Please guess a number between 0 to 10 : ")

if Variable_a == 1:
    print('Guessed right : 1!')
elif Variable_a == 10:
    print('Guessed right : 10!')
else:
    print('...Expected 10 or 1')

List_a = [1, 2, 3, 4]
if 1 in List_a:
    print('Yes 1 is in the list')
else:
    print('1 is not in the list')

List_a.remove(1)
print(List_a)
# -----------hint----------------

# -----------hint----------------
while guess_count < len(answer) and chances_left > 0:
    guess = input('Please guess a letter : ')
    # convert the letter to a lower case
    # print guess_count

    for i in range(len(answer)):
        # if guess is in the answer and guess is in used:
            # update the display with the guess
            # increase the guess_count by 1

            # remove the guess from used

    if guess not in display:
        # reduce chances_left by 1
        # print 'Sorry, wrong guess'

    # print how many correct guess have been made
    # print how many chances are left
    # print the display variably by joining each list element with a space

# if a user succeed in guessing the word, print out a congrats message
# if a user fails in guessing the word, print out a failure message

# -----------code----------------
while guess_count < len(answer) and chances_left > 0:
    guess = input('Please guess a letter : ')
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
        print('Sorry, wrong guess')
    print('You have : ', guess_count, 'correct letters')
    print('You have : ', chances_left, 'chances left')

    print(' '.join(display))
    print()


if guess_count == len(answer):
    print('******************************')
    print('Congratulations, well done!')
    print('******************************')

else:
    print('------------------------------------')
    print('Game Over :( No more chances left.')
    print('------------------------------------')