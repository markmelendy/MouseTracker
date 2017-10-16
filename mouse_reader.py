from collections import deque
import pyautogui, sys

if len(sys.argv) != 3:
	mon_x_div = 1
	mon_y_div = 1
	print "2 inputs not detected, making 1 monitor area"
else:
	try: 
		mon_x_div = int(sys.argv[1])
		mon_y_div = int(sys.argv[2])
	except ValueError:
		mon_x_div = 1
		mon_y_div = 1
		print "non int detected, making 1 monitor area"

monitor_split = [[0 for i in range(mon_x_div)] for j in range(mon_y_div)]

reader = open("movements.txt",'r')

mon_size = pyautogui.size()
monitor1 = 0
monitor2 = 0

points_dict = {}

for line in reader:
	x, y = [int(x) for x in line.split()]
	if x < mon_size[0]:
		monitor1 += 1
		x_pos = int(x/mon_size[0] * mon_x_div)
		y_pos = int(y/mon_size[1] * mon_y_div)
		monitor_split[x_pos][y_pos] += 1
	else:
		monitor2 += 1

print monitor_split

if monitor1 > 0:
	for x in range(mon_x_div):
		y_values = ''
		for y in range(mon_y_div):
			y_per = monitor_split[y][x] / monitor1
			if y_per == 1:
				y_per = 100
			y_per = str(y_per) + '%'
	   		y_values += y_per.rjust(4)
	   	print y_values
else:
	print "movements.txt has no points in it"