#Its worth learning regular expression
import re
phoneNumRex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # we need to use raw string due to the amount of back-slashes

message = 'Call me at 415-555-1011 tommorow, or at 646-833-5804'
mo = phoneNumRex.search(message) # match object
moa = phoneNumRex.findall(message)
print(mo.group())
print(moa)

#Groups ()
#to target one group within the result you can use parentesis
phoneNumRex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phoneNumRex2.search(message) # match objectt 
print(mo2.group(1))   # will return  415

#if you need a literal parentesis in the text you need to excape it
message2= 'Call me at (415)-(555-1011) tommorow, or at (646)-(833-5804)'
phoneNumRex3 = re.compile(r'\(\d\d\d\)-\(\d\d\d-\d\d\d\d\)')
mo3 = phoneNumRex3.search(message2) # match objectt 
print(mo3.group())   # will return  415

# PIPE |
message3 = 'batman batmobile batcopter '
phoneNumRex4 = re.compile(r'bat(man|mobile|copter)')
mo4 = phoneNumRex4.findall(message3) 
print(mo4)   # will return  batman

# OPTIONAL 
batRegex = re.compile(r'Bat(wo)?man') #wo? can be 0 to 1 times
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowoman')
print(mo==None)

nums = '646-555-5555 555-5555'
optionalArea = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d')
acceptedNums = optionalArea.search(nums)
print(acceptedNums.group()) 

batRegex = re.compile(r'Bat(wo)*man') #wo* can be 0 to MORE times
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())

#MUST
batRegex = re.compile(r'Bat(wo)+man') #wo+ can be 1 to MORE times
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batman')
print(mo==None) # True
#remember if you need literal chars you can escape them: \? \* \+

#EXACT NUM
haRegex = re.compile(r'(ha){3}')
ha = haRegex.search('hahaha lorem')
print(ha.group())

#RANGE
haRegex = re.compile(r'(ha){1,3}') # {1,} one or more
ha = haRegex.search('haha lorem')
print(ha.group())
#regular expressions will match the longest possible string (greedy match)
digitRegex = re.compile(r'(\d){3,5}')
num = digitRegex.search('1234567890')
print(num.group())
# to not get the greedy match use the {#,#}?
digitRegex = re.compile(r'(\d){3,5}?')
num = digitRegex.search('1234567890')
print(num.group())

