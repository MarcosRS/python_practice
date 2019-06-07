spam = 42 # global variable
ham = 10
def eggs():
    global ham # if you want to assign a value to a global variable you need to specifiy it as global
    spam = 42 # local variable
    ham = 6 

eggs()
print(spam)
print(ham)


