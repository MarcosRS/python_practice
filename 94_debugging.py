"""
***********
*         *
*         *
***********=
"""

#Exceptions
def boxPrint(symbol, width, height):
        if len(symbol) != 1:
            raise Exception("Symbol can only be 1 character")

        if (width <= 2)or (height <= 2):
            raise Exception("width and heigth must be greater that 2")
        
        print(symbol * width)
        for i in range(height - 2):
            print(symbol + (' ' * (width - 2)) + symbol)
        print (symbol * width)


boxPrint('*', 15, 5)
boxPrint('+', 1, 5)

#Exceptions as string 
import traceback
try:
    raise Exception("This is the error message")
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The tracebak info was written error_log.txt')


#Asssertion Error
assert False, 'This is an  Assetion error msg'
    #example
market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if  intersection[key] == 'green':
            intersection[key] == 'yellow'
        elif  intersection[key] == 'yellow':
            intersection[key] == 'red'
        elif  intersection[key] == 'red':
            intersection[key] == 'green'
    assert 'red' in intersection.values(), 'Neighter light is red!' + str(intersection)

switchLights(market_2nd)

#Note: Aserctions are for detecting programmer errors that are not meant to be recovered from.
#User errors should raise execeptions. 