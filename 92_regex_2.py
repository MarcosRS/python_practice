import re
#NRMAL
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
text = ''' 123-456-78941 345-654-3445 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc pulvinar neque in imperdiet ultrices. Maecenas suscipit, enim at aliquam imperdiet, lorem est feugiat eros, id pulvinar purus nisi sed velit. Nunc vitae mattis est. Donec rhoncus orci nunc, quis ultricies purus efficitur in. In urna mauris, egestas vitae mi et, iaculis laoreet neque. Sed ultrices ac nisl nec eleifend. Donec placerat convallis efficitur. Pellentesque efficitur elit at tempus ultricies. Quisque luctus faucibus efficitur. Vestibulum sodales mattis auctor. Aenean vehicula augue nec libero malesuada molestie a vitae mauris. Praesent lobortis tempor magna, ac accumsan orci viverra sit amet. Nunc placerat mauris a nulla accumsan, vel auctor lorem dapibus. Vivamus in lectus non elit interdum ultricies in eu ante. Suspendisse quis felis posuere, consectetur nisi id, maximus augue.  '''
print(phoneRegex.findall(text)) # ['123-456-7894', '345-654-3445']

#Twoples and ()
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(phoneRegex.findall(text)) #[('123', '456-7894'), ('345', '654-3445')]

#Keep result in one twople
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex.findall(text)) #[('123-456-7894', '123', '456-7894'), ('345-654-3445', '345', '654-3445')]



#Character Classes //https://www.dataquest.io/blog/regex-cheatsheet/#characterclassesakaspecialsequences
digitRegex = re.compile(r'\d')
print(digitRegex.findall('12334'))

lyrics = ''' On the first day of Christmas
my true love sent to me:
A Partridge in a Pear Tree

On the second day of Christmas
my true love sent to me:
2 Turtle Doves
and a Partridge in a Pear Tree

On the third day of Christmas
my true love sent to me:
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the fourth day of Christmas
my true love sent to me:
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the fifth day of Christmas
my true love sent to me:
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree

On the sixth day of Christmas
my true love sent to me:
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and a Partridge in a Pear Tree...'''

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))


#Making your own character classes

vowelsReg = re.compile(r'[aeiouAEIOU]') #PYTHON SPECIFIC you can pass 're.IGNORECASE' to cover new-line too like  re.compile(r'[aeiou]', re.IGNORECASE)
vowelsRegDouble = re.compile(r'[aeiouAEIOU]{2}')
negVowelsReg = re.compile(r'[^aeiouAEIOU]')

lettersReg = re.compile(r'[a-zA-Z]')
print(vowelsReg.findall('Robocop eats baby food'))
print(vowelsRegDouble.findall('Robocop eats baby food'))


#^ caret symbol (negate) inside if the []
print(negVowelsReg.findall('Robocop eats baby food'))

# ^ caret symbol (begining) '^Hello'
# $ dollar symbol (end) 'wolrd$'
# you can use them to sya it covers 'the entire text' '^Hell wolrd$''

beginsWithHello = re.compile(r'^Hello')
beginsWithHelloOut =  beginsWithHello.search('Hello there!')
beginsWithHelloOut2 = beginsWithHello.search('Hi there Hello')

endsWithWorld = re.compile(r'World$')
endsWithWorldOut = endsWithWorld.search('clean World')
print(endsWithWorldOut)

# wild-Card . (dot) stand for any character execpt for new-line
#PYTHON SPECIFIC you can pass 're.DOTALL' to cover new-line too like  re.compile(r'.*', re.DOTALL)
atRex = re.compile(r'.{1,2}at')
print(atRex.findall('The Cat in the hat sat on the flat mat'))


#.*   dot(any character) * (0 or more) - greedy mode.
#.*?  dot(any character) * (0 or more) - none greedy mode - take as less character as posible.
nameRex = re.compile(r'First Name: (.*) Last Name: (.*)') # twoples
print(nameRex.findall('First Name: Ian Last Name: Reynoso'))

serve = '<To serve humans> for dinner> '
nongreedy = re.compile(r'<(.*?)>') 
greedy = re.compile(r'<(.*)>') 
print(nongreedy.findall(serve))
print(greedy.findall(serve))

#Find Features  - upto-now search and findall
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret document to Agent Bob'))

#Sub - Subtitute
print(namesRegex.sub('REDACTED','Agent Alice gave the secret document to Agent Bob'))

#Grabbing character from result - Using groups
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.sub(r'Agent \1****','Agent Alice gave the secret document to Agent Bob')) #\1 \2 .. match the the specified groups

# Verbose - Format, in verbose mode new-lines won't affect the regex. You can also put comments in verbose mode
verboseEx = re.compile(r,'''
            \d\d\d      #area code
            -\d\d\d     #first 3 digits
            -\d\d\d\d   #last four digits''', re.VERBOSE)
