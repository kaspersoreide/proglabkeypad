from keypad import Keypad
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

class KPC_Agent:

    def __init(self):
        self.fsm = FSM()
        self.keypad = 0
        self.led = 0
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
        #flash

    def get_next_signal(self, keypad):
        if self.override_signal:
            result = self.override_signal
            self.override_signal = None
            return result
        else:
            return keypad.poll_buttons()

    def verify_login(self):
        if self.password_buffer == self.read_password(self.file_name): ##lese fra fil
            self.override_signal += "Y"
        else:
            self.override_signal+="N"

    def add_next_

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

    def read_password(file):
        with open(file) as password_file:
            password = password_file.read().strip()
            print(password)
            return password
    def do_

    def light_one_led(self):


    def flash_leds(self):


    def twinkle_led(self):


    def exit_action(self):









class FSM:
    def __init__(self, agent, state):
        self.agent = agent
        self.rule_list = []
        self.signal = None
        self.state = state.init


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
