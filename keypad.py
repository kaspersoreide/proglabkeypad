import RPi.GPIO as GPIO

class Keypad:
    def __init__(self):
        #index mapped to GPIO-pins
        self.rows = [18, 23, 24, 25]
        self.cols = [17, 27, 22]
        self.signals = [['1', '2', '3'],
                        ['4', '5', '6'],
                        ['7', '8', '9'],
                        ['*', '0', '#']]
        for r in self.rows:
            GPIO.setup(r, GPIO.OUT)
        for c in self.cols:
            GPIO.setup(c, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    def poll_buttons(self):
        for i in range(len(self.rows)):
            GPIO.output(self.rows[i], GPIO.HIGH)
            for j in range(len(self.cols)):
                if GPIO.input(self.cols[j]) == GPIO.HIGH:
                    print(self.signals[i][j])

def test():
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.HIGH)

