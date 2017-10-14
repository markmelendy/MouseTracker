from collections import deque
import pyautogui

reader = open("movements.txt",'r')
#mouse_points = deque([],100)

mon_size = pyautogui.size()
monitor1 = 0
monitor2 = 0

for line in reader:
	x,y = [int(x) for x in line.split()]
	if x > mon_size[0]:
		monitor1 += 1
	else:
		monitor2 += 1

print "Monitor 1 had: ", monitor1, "points"
print "Monitor 2 had: ", monitor2, "points"
