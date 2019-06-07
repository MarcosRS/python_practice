# files paths , file names, file extensions
# os module contains file path fuction (compatible for windows, mac, linux)
import os

#generates path for current os
print(os.path.join('folder1', 'folder2', 'folder3'))

os.sep #\\

print(os.getcwd()) # get current working directory

#to change directory
os.chdir('/')

# . root folder
#.. parent folder

#return absolute file path
os.path.abspath('spam.png')

#check if its absolute
s.path.isabs('spam.png') #False

#check if its absolute
s.path.isabs('spam.png') #False

#gives you the relative path between two paths
os.path.relpath('c:\\folder1\\folder2\\spam.png','c:\\folder1')
#output folder2\\spam.png

#get path 
os.path.dirname('c:\\folder1\\folder2\\spam.png')
#output c:\\folder1\\folder2

os.path.basename('c:\\folder1\\folder2\\spam.png')
#output spam.png  it can get the foldername too

#to check if the file exist
os.path.exists('c:\\folder1\\folder2\\spam.png') #False

#to check if the intput is a file
os.path.isfile('c:\\folder1\\folder2\\spam.png') #True

#to check if the intput is a directory
os.path.isdir('c:\\folder1\\folder2\\spam.png') #False

#to get size of a file , returns in bytes
os.getsize('c:\\folder1\\folder2\\spam.png') 

#list all the files in a folder
os.listdir('c:\\folder1)


#example that returns the total sizes of all files in directory
totalsize = 0 
for filename in os.listdir('c:\\folder1\\folder2'):
    if not os.path.isfile(os.path.join('c:\\folder1\\folder2',filename))
        continue
    totalsize = totalsize + os.getsize(os.path.join('c:\\folder1\\folder2',filename)') 


#os make directories
os.makedirs('c:\\folder1\\folder2\\waffles')





#reading and wirting plaintext files (a binary file is everything else thats not plaint text)

helloFile = open('\home')
content = helloFile.read()
helloFile.close()

contentlines = helloFile.readlines()
#contentlines will give you a list of stings for evryline respectively.

#THIS WAS NOT TESTED
# write mode overwrites what you have the content
helloFile = open('\home\text.txt', 'w')
helloFile.write('Hello!')

helloFile.close()
# write mode overwrites what you have the content
helloFile = open('\home\text.txt', 'a')

print(os.getcwd())

#To handle complex data structures you can use the shelve module.
import shelve
shelveFile = shelve.open('mydata')
shelveFile['cats'] =  ['zophie', 'pooka', 'simon']
shelveFile.close()


shelveFile = shelve.open('mydata')
shelveFile['cats'] # should have ['zophie', 'pooka', 'simon']



