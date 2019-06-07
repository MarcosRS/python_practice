#escaping characters \' , \" , \t, \n, \\
alison = 'That is Alison\'s cat'
print(alison)

#you can also use raw string and everythig will be interpreted as a string
rawStr = r'nice \' \n \" dfsfsf ' 
print(rawStr)

# multiline strings. this iincludes new lines as tab directly. Useful when you have a large string
mul = '''
Once Upon a time
    Little red hidding hood
was walking in the forrest.

And you know the rest :D 
'''

print(mul)

# You can use lists/array list in strings too:
print(alison[0])
print(alison[1:])
print(alison[-1])
print('al' in alison)
print('123' not in alison)


# String Methods
strText = 'once upon! SHREK! donkey'
print(strText.upper())
print(strText.lower())
print(strText.title())

print(strText.isupper()) #boolean
print(strText.islower()) # boolean

print(strText.upper().isupper())

# Other methods : isalpha, isalnum, isdecimal, 
# isspace, istitle, startswith, endswith, 
# ljust, rjust (second argument specifies the fill character)
# center (second argument specifies the fill character)
# strip, rstrip, lstrip (removes spaces)
# replace (same :D)

#join example:
print (','.join(['cat', 'rat', 'bat']))

#split example
print('bat,mat,fat'.split(',')) 


#Additional: pyperclip (needs to be installed)
#pyperclip is used to grab 
#pyperclip.copy() , copies to the clipboard
#pyperclip.paste() , brings back the text from the clipboard



# STING FORMATTING - Similar to templating
stingTest = 'nice' + 'coding'
name = 'Alice'
time = '10:00:'

print('%s You are invited to a party at %s' % (name, time))



