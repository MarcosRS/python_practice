import pprint  

mycat = {'size': 'fat', 'clor': 'grey'}
print(mycat['size'])

eggs = {'name': 'Zophie', 'species': 'cat'}
ham =  {'species': 'cat','name': 'Zophie'}

print(eggs==ham) #exact , no-order


#You can check  for a key
'name' in eggs  # should  return True

#Ditionary methods , the retrun list like data types, returns dict_keys([...]) , you need to past it to list to get and actual list
print(list(eggs.keys())) # eggf
print(list(eggs.values()))
print(list(eggs.items()))


# They can be used in loops:
for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for i in eggs.items(): # items has both items
    print(i)

# twople exmaple
for k, v  in eggs.items(): # items has both items
    print(k,v)

'Cat' in eggs.values() # should retune true

#for conditional you can use :
if 'color' in eggs:
    print(eggs['color'])

# Python give us shortcuts :
eggs.get('name', 0)
eggs.get('age', False)

# To set values you can use setdefault
eggs.setdefault('color', 'black') # only if the key does not exist

print(eggs)

#You can use setdefault to make sure a key exists so you dont get an errors
message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vestibulum ante in fringilla accumsan. Mauris non elit vel metus imperdiet tristique efficitur sed lacus. Cras id quam vel turpis porta egestas. Praesent dignissim turpis ut urna interdum, quis laoreet nulla interdum. Nullam in viverra nunc.'
count = {}

for character in message.upper():
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count) #organizes 
pprint.pformat(count)  # to save in a file


allCats = []
allCats.append({'name': 'Zophie', 'age': 7, 'color': 'black'})
allCats.append({'name': 'Pooka', 'age': 5, 'color': 'grey'})
allCats.append({'name': 'Fat-tail', 'age': 5, 'color': 'grey'})
allCats.append({'name': '???', 'age': 5, 'color': 'grey'})

# To store thing that represent real life objects you can use Data-Structures. Example: 
# Tic Tac Toe : 
# top-L | top-M | top-R
# mid-L | mid-M | mid-R
# low-L | low-M | low-R

theBoard = {'top-L': 'O', 'top-M': 'O' , 'top-R': 'O',
            'mid-L': 'X', 'mid-M':'X' , 'mid-R': 'X',
            'low-L': ' ', 'low-M': ' ' , 'low-R': 'X'}

def printTheBoard (theBoard):
    print(theBoard['top-L'] + '|' + theBoard['top-M'] + '|' + theBoard['top-R'])
    print('------')
    print(theBoard['mid-L'] + '|' + theBoard['mid-M'] + '|' + theBoard['mid-R'])
    print('------')
    print(theBoard['low-L'] + '|' + theBoard['low-M'] + '|' + theBoard['low-R'])

printTheBoard(theBoard)
# you can also use type() to to find out the type of data of something
print(type(theBoard))
