def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.') 

print(div42by(0))
print(div42by(2))

print('How many dog you have?')
numDogs = input()

try:
    if int(numDogs) >= 4:
        print('That a lot of dogs')
    elif numDogs < 0:
        print('Please enter a more realistic number')
    else:
        print('That is not that many dogs.')
except ValueError:
    print('You did not nter a number')