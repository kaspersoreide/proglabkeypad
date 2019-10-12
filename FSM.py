from keypad import Keypad
from ledboard import *
class Rule:
    def __init__(self, signal, state, next_state, action):
        self.state = state
        self.next_state= next_state
        self.action = action
        self.signal = signal

class State:
    init = 0
    read= 1
    verify = 2
    active = 3
    finished = 4


class Signal:
    @staticmethod
    def all_symbols(signal):
        return True

    @staticmethod
    def all_digits(signal):
        return ord("0")<=ord(signal)<=ord("9")

    @staticmethod
    def verify(signal):
        return signal == "*"

    @staticmethod
    def done(signal):
        return signal =="Y"

    @staticmethod
    def hash(signal):
        return signal == "#"


class KPC_Agent:

    def __init(self, keypad):
        self.fsm = FSM()
        self.keypad = keypad
        self.led = LEDboard()
        self.file_name = "passord.txt"
        self.password_buffer = ""
        self.override_signal = None
        self.led_id = ""
        self.led_duration = ""# har vi tall eller strings som kommer inn her?
        self.Legal_numbers =['0','1','2','3','4','5','6','7','8','9']

    def init_passcode_entry(self):
        self.password_buffer = ""
        self.led_id= ""
        self.led_duration = ""
        self.override_signal = None
        self.led.flash_LEDs()
        #flash

    def get_next_signal(self):
        if self.override_signal:
            result = self.override_signal
            self.override_signal = None
            return result
        else:
            return self.keypad.poll_buttons()

    def verify_login(self):
        if self.password_buffer == self.read_password(self.file_name): ##lese fra fil
            self.override_signal += "Y"
        else:
            self.override_signal+="N"
        self.init_passcode_entry()

<<<<<<< HEAD
    def add_
=======
    def add_next_digit(self, digit):
        if digit in self.Legal_numbers:
            self.password_buffer+= digit
>>>>>>> a217a5a4288e8bd0e86b23ceda3422524cddea3b

    def validate_passcode_change(self):
        validate = True
        if len(self.password_buffer)<4:
            validate = False
        for num in self.password_buffer:
            if num not in self.Legal_numbers:
                validate = False
        if validate:
            with open(self.file_name, "w+") as password_file:
                password_file.write(self.password_buffer)

    def read_password(self, file):
        with open(file) as password_file:
            password = password_file.read().strip()
            print(password)
            return password

    def light_one_led(self):


    def flash_leds(self):
        self.led.flash_LEDs()


    def twinkle_led(self):


    def exit_action(self):
        self.led.turn_off_LEDs()




class FSM:
    def __init__(self, agent, state):
        self.agent = agent
        self.rule_list = []
        self.signal = None
        self.state = state.init

    def setup_rules(self):
        self.rule_list = [
            Rule(Signal.all_symbols, State.init, State.read, KPC_Agent.init_passcode_entry),
            Rule(Signal.all_digits, State.read, State.read, KPC_Agent.add_next),
        ]

    def add_rule(self, rule):
        self.rule_list.append(rule)

    def get_next_signal(self):
        return KPC_Agent.get_next_signal

    def run_rules(self, state, signal):

        for rule in self.rule_list:
            if rule.state == state and rule.signal == signal:
                self.state = rule.next_state
                self.fire_rule(rule)

    def main_loop(self):
        while self.state != State.finished:
            self.run_rules(self.state, self.get_next_signal )


    def fire_rule(self, rule):
        KPC_Agent.do_action(rule.actuion)
