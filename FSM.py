""" Oline, Kasper og Andreas"""
from ledboard import *


class Rule:
    """ RULE"""
    def __init__(self, signal, state, next_state, action):
        self.state = state
        self.next_state = next_state
        self.action = action
        self.signal = signal


class State:
    """ STATE"""
    init = 0
    read_password = 1
    read_time =1
    verify = 2
    active = 3
    finished = 4
    led_time = 5
    led = 6
    logout = 7



class Signal:
    """ SIGNAL"""
    @staticmethod
    def all_symbols(signal):
        """ S"""
        return True

    @staticmethod
    def all_digits(signal):
        """ digits"""
        return ord("0") <= ord(signal) <= ord("9")

    @staticmethod
    def verify(signal):
        """ verify"""
        return signal == "*"

    @staticmethod
    def done(signal):
        """ done"""
        return signal == "Y"

    @staticmethod
    def hash(signal):
        """ hash"""
        return signal == "#"


class KpcAgent:
    """ KPC"""

    def __init(self, keypad):
        self.fsm = FSM(self)
        self.keypad = keypad
        self.led = LEDboard()
        self.file_name = "passord.txt"
        self.password_buffer = ""
        self.override_signal = None
        self.led_id = ""
        self.led_duration = ""# har vi tall eller strings som kommer inn her?
        self.Legal_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def init_passcode_entry(self):
        """ init"""
        self.password_buffer = ""
        self.led_id = ""
        self.led_duration = ""
        self.override_signal = None
        self.led.power_up()
        #flash

    def get_next_signal(self):
        """ next_signal"""
        if self.override_signal:
            result = self.override_signal
            self.override_signal = None
            return result
        else:
            return self.keypad.poll_buttons()

    def verify_login(self):
        """ Verify"""
        if self.password_buffer == self.read_password(self.file_name):  #lese fra fil
            self.override_signal += "Y"

        else:
            self.override_signal += "N"
            self.led.wrong()
            self.init_passcode_entry()

    def add_next_digit(self, digit):
        """ add"""
        if digit in self.Legal_numbers:
            self.password_buffer += digit

    def validate_passcode_change(self):
        """ Validate"""
        validate = True
        if len(self.password_buffer) < 4:
            validate = False
        for num in self.password_buffer:
            if num not in self.Legal_numbers:
                validate = False
        if validate:
            with open(self.file_name, "w+") as password_file:
                password_file.write(self.password_buffer)
        else:
            self.led.wrong()

    def read_password(self, file):
        """read"""
        with open(file) as password_file:
            password = password_file.read().strip()
            print(password)
            return password

    def light_one_led(self):
        """ one led"""
        self.led.power_up()

    def exit_action(self):
        """ exit"""
        self.led.turn_off_LEDs()


class FSM:
    """ FSM"""
    def __init__(self, agent, state):
        self.agent = agent
        self.rule_list = []
        self.signal = None
        self.state = state.init

    def setup_rules(self):
        """ setup"""
        self.rule_list = [
            Rule(Signal.all_symbols, State.init, State.read, KpcAgent.init_passcode_entry),
            Rule(Signal.all_digits, State.read, State.read, KpcAgent.add_next),
        ]

    def add_rule(self, rule):
        """ add_rule"""
        self.rule_list.append(rule)

    def get_next_signal(self):
        """ get next signal"""
        return KpcAgent.get_next_signal

    def run_rules(self, state, signal):
        """ run rules"""
        for rule in self.rule_list:
            if rule.state == state and rule.signal == signal:
                self.state = rule.next_state
                self.fire_rule(rule)

    def main_loop(self):
        """ main"""
        while self.state != State.finished:
            self.run_rules(self.state, self.get_next_signal )

    def fire_rule(self, rule):
        """ fire"""
        KpcAgent.do_action(rule.actuion)
