import RPi.GPIO as GPIO

class Keypad:
    def __init__(self):
        #index mapped to GPIO-pins
        self.rows = [18, 23, 24, 25]
        self.cols = [17, 27, 22] 
        for r in rows:
            GPIO.setup(r, GPIO.OUT)
        for c in cols:
            GPIO.setup(c, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    def poll_buttons:

