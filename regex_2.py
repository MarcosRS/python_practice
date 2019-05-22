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

vowelsReg = re.compile(r'[aeiouAEIOU]')
vowelsRegDouble = re.compile(r'[aeiouAEIOU]{2}')
negVowelsReg = re.compile(r'[^aeiouAEIOU]')

lettersReg = re.compile(r'[a-zA-Z]')
print(vowelsReg.findall('Robocop eats baby food'))
print(vowelsRegDouble.findall('Robocop eats baby food'))


#^ caret symbol (negate)
print(negVowelsReg.findall('Robocop eats baby food'))
