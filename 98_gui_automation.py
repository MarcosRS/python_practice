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

