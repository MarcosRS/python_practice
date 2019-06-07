for i in range(4): #this actually creates a list [0,1,2,3]
    print(i)


range(0,4) # will print range(0,4)
list(range(0,4)) #will print the actual list [0,1,2,3]


#for huge number with (lest say an increment of 2) you can do:
list(range(1,100,2))
# [0, 2 ,4, 6......]

#You ou can also use the len technique with the for approach
supplies = ['pens','staplers','flame-throwers','binders']
for i in range(len(supplies)): 
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#Multiple Assignment 
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
# size : fat , color: orange , disposition: loud

#Multiple Assignment #2
size, color, disposition = 'skinny', 'black', 'quiet'

#Swapping 
a = 'AAA'
b = 'BBB' 

a, b = b, a
# a : 'BBB' & b: 'AAA'


#Augmented assignment
spam = 44
spam += 1

print(spam)



