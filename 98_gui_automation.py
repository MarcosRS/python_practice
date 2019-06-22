# pip install pyautogui
# https://pyautogui.readthedocs.org

# the screen is like cartesian coordinates
# coordinates start at 0 top left

import pyautogui
pyautogui.size() #screen resolution
width, height = pyautogui.size() # multiple assignment 

pyautogui.position() # gives you the mouse position

#moveTo
pyautogui.moveTo(10, 10) # moves mouse to a certain postion

pyautogui.moveTo(10, 10, duration=1.5 ) # moves to certain postion in a time-frame


#moveRel 
pyautogui.moveRel(200, 0 ) # moves mouse to a position relative to where you currently are
pyautogui.moveRel(200, 0,  duration=2 ) # || with time-frame in seconds
pyautogui.moveRel(0, -100,  duration=1 ) #|| down

#click
pyautogui.click() # left click at current position
pyautogui.click(100,250) # || with coordinates
pyautogui.doubleClick(100,250) # double click with coordinates
pyautogui.middleClick(100,250) # middle click with coordinates
pyautogui.rightClick(100,250) # right click with coordinates

pyautogui.dragRel(200, 250, duration=2) # right click pressed with duration 





#Keyboard
import pyautogui

#first focus where you want to write
pyautogui.click(100, 100)
pyautogui.typewrite('Hello World')
#for multiple commands use `;`
pyautogui.click(100, 100);
pyautogui.typewrite('Hello World')

#for pauses between characters you can use interval
pyautogui.typewrite('Hello World',interval=0.2)

#to send specific keys like 'left' arrow use
pyautogui.typewrite(['a','b','left','left','X','Y']) #XYab

#For keyboarkeys list 
pyautogui.KEYBOARD_KEYS # prints the list

#to press you one key
pyautogui.press('f1')

#to press a combination of keys like `ctrl-c` & `ctrl-v`
pyautogui.hotkey('ctrl', 'o')






#Sceen shots and image recognition
#to use the screenshot pyautogui feature and NOT 'windows or OS 10' you need to install  `sudo apt-get install scrot`
import pyautogui
pyautogui.screenshot() # this creates something called a pillow object

#saves screenshot in a file
pyautogui.screenshot('./screenshot_example.png')

# you can just screenshot a certain section of the screen.
# and pass it to locateOnScreen or locateCenterOnScreen 
# coputing expensive and screenshots have to be pixel perfect. Not suited for realtime. Read the docs for partial matches
pyautogui.locateOnScreen('./screenshot_of_a_num7_in_calc') #this will return (x,y,width, hegiht) 
pyautogui.locateCenterOnScreen('./screenshot_of_a_num7_in_calc') #this will return (x,y,width, hegiht). x and y will be the center 

pyautogui.moveTo((300, 300), duration=1)
pyautogui.click((300, 300)) #it can be passed in ()
