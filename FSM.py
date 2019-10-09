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




class FSM:
    def __init__(self, agent, state):
        self.agent = agent
        self.rule_list = []
        self.signal = None
        self.state = state.init


    def add_rule(self, rule):
        self.rule_list.append(rule)

    def get_next_signal(self):
        return agent.get_next_signal

    def run_rules(self, state, signal):

        for rule in self.rule_list:
            if rule.state==state and rule.signal == signal:
                self.state = rule.next_state
                self.fire_rule(rule)

    def main_loop(self):
        while self.state != State.finished:
            self.run_rules(self.state, self.get_next_signal )


    def fire_rule(self, rule):
        agent.do_action(rule.actuion)
