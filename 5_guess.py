import random

print('Hello. What is you name?')
name = input()
secretNumber = random.randint(1, 20)
print('Well' + name + ', I\'m thinking of a number between 1 - 20. Can you guess it ?')

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break 

if guess == secretNumber:
    print('Good job '+name+'! Ypu guessed the number')
else:
    print('Nope. the number I was thinking of is: ' + str(secretNumber))
