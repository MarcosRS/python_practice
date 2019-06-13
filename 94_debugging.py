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





#LOGGIN MODULE
# To add logging you need to enable it (for your script) first

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

# TO TURN OF ALL logging you can do: logging.disable(logging.CRITICAL).
# THE LOG levels are: debug(lowest), info, warning, error, critical(highest)
# CALLS: logging.debug(), logging.info(), logging.warning(), logging.error(), logging.critical()
# YOU can also write the logs to a file like  logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1 ,n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

factorial(5)
logging.debug('End of Program')

print(factorial(5))





# USING THE DEBUGGER  -  IDLE (pyhon IDE)
# check stack, locals, source, globals - in config
# The execution will pause on each lines
# looks at the debug control





















