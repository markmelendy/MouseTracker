#! python
import pyautogui, sys

print('Press Ctrl-C to quit.')
movement_file = open("movements.txt", 'w')

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        movement_file.write(positionStr)
        print positionStr,
        print '\b' * (len(positionStr) + 2),
        sys.stdout.flush()
except KeyboardInterrupt:
    movement_file.close()
    print '\n'