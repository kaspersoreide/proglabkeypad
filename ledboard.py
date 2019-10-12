import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class LEDboard:
    def __init__(self);
        self.LEDs = [16, 20, 21]
        self.leds_enabled = [False, False, False,
                             False, False, False]
        for i in range(3):
            GPIO.setup(self.LEDs[i], GPIO.OUT)
    def disable_LEDs(self):
        for i in range(3):
            GPIO.output(self.LEDs[i], GPIO.LOW)
    def flash_LEDs(self):
        for i in range(6):
            if not leds_enabled[i]:
                continue
            self.disable_LEDs()
            led_index = i // 2
            switch = i % 2
            pin1 = self.LEDs[led_index]
            pin2 = self.LEDs[(led_index + 1) % 3]
            if switch == 1:
                GPIO.output(pin2, GPIO.HIGH)
            else:
                GPIO.output(pin1, GPIO.HIGH)
    def enable_LEDs():
        for i in range(6):
            self.leds_enabled[i] = True

ledboard = LEDboard()
ledboard.enable_LEDs()
while True:
    ledboard.flash_LEDs()

