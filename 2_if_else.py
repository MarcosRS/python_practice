user = 'marcos'
password = 'swordfish'

if password == 'swordfish' and  user == 'marcos':
    print('Access Granted')
else :
    print('Access Denied')

age = 26

if age == 25:
    print('Shit is just starting Bro')
elif age < 25:
    print('you some young mofo')
else :
    print('you some old mofo')


name = raw_input() 
#it has the falsey condition
if name:
    print('Hello '+ name + ', you cray mofo')
else :
    print('Hello no name mofo')

#you can use the bool() function to get the truthy or falsey values