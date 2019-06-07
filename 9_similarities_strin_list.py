import copy
#You can use the copy module to do a deep copy not just a reference

# List are mutable
# Strings are inmutable
# list only keep references

#The same applies to refeneces and assignment


name ='Marcos'
#You cannot do name[2] = 'o'
#But you can slices

pet = 'Ian\'s new cat'
newPet = pet[0:5] + 'will have a dog';

spam = ['A','B','C', 'D']
cheese = copy.deepcopy(spam)
spam.append('E')
print(spam)
print(cheese)

# Python lets you give a new line  on list with out affecting the 
# Tab indentation

#You can also use line continuation with '\'
print('Four score and seven' + \
    ' years ago')

