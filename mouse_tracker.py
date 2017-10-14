#! python
import pyautogui, sys, time

print('Press Ctrl-C to quit.')
movement_file = open("movements.txt", 'w')

try:
    while True:
    	time.sleep(.01)
        x, y = pyautogui.position()
        posStr = str(x) + ' ' + str(y)
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        movement_file.write(posStr)
        movement_file.write('\n')
        print positionStr,
        print '\b' * (len(positionStr) + 2),
        sys.stdout.flush()
except KeyboardInterrupt:
    movement_file.close()
    print('\n\nKeyboard exception received. Exiting.')