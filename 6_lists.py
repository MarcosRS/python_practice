
# This is similar to an Array
spam = ['cat','bat', ['flat, mat']]
print(spam)
print(spam[2])

 # you can also get a sub list  'slice'
sub = spam[1:2]
print(sub)


# Can Also Assign 
ham = ['a', 'b', 'c', 'e']
ham[1] = 'd'




print(ham)

 #from fill from start: ham[:3] = ['x', 'y', 'z']
 #from fill from end: ham[3:] = ['x', 'y', 'z']

ham[1:3] = ['x', 'y', 'z']

print(ham)

#You can target the end of the List using a negative number:
ham[-1]

# To delete you can use 'del':
del ham[0]

#You can use len() to get the length of this List:
len([1,2,3])

# You can concatinate:
[1,2,3] + [4,5,6])

# You can multiply Lists withing them selfs
[1,2,3] * 3

# There is a a funtion that will take in values and convert them inta a list
list('hello') # = ['h','e','l','l','o']

# to check is an item is in a list you can use 'in' and 'not in'
'howdy' in ['hello', 'howdy']  # True



