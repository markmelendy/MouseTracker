#! python
import pyautogui, sys, time, os

print('Press Ctrl-C to quit.')
movement_file = open("movements.txt", 'w')

try:
    while True:
    	time.sleep(.05)
        x, y = pyautogui.position()
        posStr = str(x) + ' ' + str(y)
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        movement_file.write(posStr)
        movement_file.write('\n')
        movement_file.flush()
        print positionStr,
        print '\b' * (len(positionStr) + 2),
        sys.stdout.flush()
except KeyboardInterrupt:
    print('\n\nKeyboard exception received. Exiting.')
    movement_file.close() 