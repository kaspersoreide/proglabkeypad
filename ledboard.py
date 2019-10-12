import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class LEDboard:
    def __init__(self):
        self.LEDs = [16, 20, 21]
        self.leds_enabled = [False, False, False,
                             False, False, False]
        for i in range(3):
            GPIO.setup(self.LEDs[i], GPIO.OUT)
    def turn_off_LEDs(self):
        for i in range(3):
            GPIO.output(self.LEDs[i], GPIO.LOW)
    def flash_LEDs(self):
        self.turn_off_LEDs()
        for i in range(6):
            if not self.leds_enabled[i]:
                continue
            led_index = i // 2
            switch = i % 2
            pin1 = self.LEDs[led_index]
            pin2 = self.LEDs[(led_index + 1) % 3] 
            self.turn_off_LEDs()
            if switch == 1:
                GPIO.output(pin2, GPIO.HIGH)
            else:
                GPIO.output(pin1, GPIO.HIGH)
    def enable_LEDs(self):
        for i in range(6):
            self.leds_enabled[i] = True
    def disable_LEDs(self):
        for i in range(6):
            self.leds_enabled[i] = False
    def lid_ldur(self, index, duration):
        self.disable_LEDs()
        self.leds_enabled[index] = True
        t = time.time()
        while time.time() - t < duration:
            self.flash_LEDs()

    def power_up(self):
        self.disable_LEDs()
        for i in range(6):
            t = time.time()
            self.leds_enabled[i] = True
            while time.time() - t < 0.7:
                self.flash_LEDs()
        self.disable_LEDs()

    def wrong(self):
        self.disable_LEDs()
        for i in range(3):
            t = time.time()
            for i in range(6):
                self.leds_enabled[i] = not self.leds_enabled[i]
            while time.time() - t < 0.4:
                self.flash_LEDs()
        self.disable_LEDs()

