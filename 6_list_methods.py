spam = ['hello', 'hi', 'howdy', 'heyas'];
print(spam.index('howdy'));
spam.append('hellors');
spam.insert(1, 'what up');

print(spam)

## It will remove anywhere in the list 
spam.remove('heyas')
print(spam)


#Sorting - It uses ASCII-betical Order - A < a 
#For True Alphabetical you can pass (key = str.lower)
num = [2, 5, 3.1, -7, 3.14,]
num.sort()
print(num)
num.sort(reverse=True)
print(num)


