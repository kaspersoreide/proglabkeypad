from keypad import Keypad
from ledboard import *


class Rule:
    def __init__(self, state, next_state, signal,  action):
        self.state = state
        self.next_state = next_state
        self.action = action
        self.signal = signal

    def do_action(self):
        return self.action


class State:
    init = 0
    read1= 2
    read2= 3  # need two reads to represent both state where kpc is not initialized and state where it actually reads
    read_password = 1
    read_active = 2
    logout = 3
    verify = 4
    active = 5
    finished = 6
    time = 7
    led = 8


class Signal:
    @staticmethod
    def all_symbols(signal):
        return True

    @staticmethod
    def all_digits(signal):
        return ord("0")<=ord(signal)<=ord("9")

    @staticmethod
    def asterisk(signal):
        return signal == "*"

    @staticmethod
    def done(signal):
        return signal == "Y"

    @staticmethod
    def hash(signal):
        return signal == "#"


class KPC_Agent:

    def __init(self):
        self.fsm = FSM(self)
        self.keypad = Keypad()
        self.led = LEDboard()
        self.file_name = "passord.txt"
        self.password_buffer = ""
        self.override_signal = None
        self.led_id = 0
        self.led_duration = 0
        self.Legal_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def init_passcode_entry(self):
        self.reset_agent()
        self.led.flash_LEDs()
        # flash

    def reset_agent(self):
        self.password_buffer = ""
        self.led_id = ""
        self.led_duration = ""
        self.override_signal = None

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

    def add_next_digit(self, digit):
        if digit in self.Legal_numbers:
            self.password_buffer += digit

    def validate_password_change(self):
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
        self.led.lid_ldur(self.led_id, self.led_duration)

    def flash_leds(self):
        self.led.flash_LEDs()

<<<<<<< HEAD

=======
>>>>>>> 9636fba422fdf134da95bb3d484103bb97247722
    def exit_action(self):
        self.led.turn_off_LEDs()

    def do_nothing(self):
        pass




class FSM:

    def __init__(self, agent):
        self.agent = agent
        self.rule_list = []
        self.signal = None
        self.state = State.init

    def setup_rules(self):
        self.rule_list = [
            Rule(State.init, State.read_password, Signal.all_symbols, self.agent.init_passcode_entry),
            Rule(State.read_password, State.read_password, Signal.all_digits, self.agent.add_next_digit),
            Rule(State.read_password, State.verify, Signal.asterisk, self.agent.verify_login),
            Rule(State.read_password, State.init, Signal.all_symbols, self.agent.reset_agent),

            Rule(State.verify, State.active, Signal.done, self.agent.verify_login),
            Rule(State.verify, State.init, Signal.all_symbols, self.agent.reset_agent),

            Rule(State.active, State.read_active, Signal.asterisk, self.agent.reset_agent),
            Rule(State.active, State.logout, Signal.hash, self.agent.exit_action),
            Rule(State.active, State.led, Signal.all_symbols, self.agent.do_nothing),

            Rule(State.read_active, State.read_active, Signal.all_digits, self.agent.add_next_digit),
            Rule(State.read_active, State.active, Signal.asterisk, self.agent.verify_password_change),
            Rule(State.read_active, State.active, Signal.all_symbols, self.agent.reset_agent),



        ]

    def add_rule(self, rule):
        self.rule_list.append(rule)

    def get_next_signal(self):
        return self.agent.get_next_signal

    def run_rules(self, state, signal):
        for rule in self.rule_list:
            if rule.state == state and rule.signal == signal:
                self.state = rule.next_state
                self.fire_rule(rule)

    def main_loop(self):
        while self.state != State.finished:
            self.run_rules(self.state, self.get_next_signal )


    def fire_rule(self, rule):
       rule.do_action()
