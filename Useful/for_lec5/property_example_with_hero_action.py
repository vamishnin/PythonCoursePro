class Hero:
    def __init__(self, new_action):
        self._action = new_action

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, new_action):
        if isinstance(new_action, Action):
            self._action = new_action
        else:
            print("Incorrect action")		


class Action:
    def do_action(self):
        print("base action")

class Run(Action):
    def do_action(self):
        print("running")

class Fly(Action):
    def do_action(self):
        print("flying")		


h = Hero(Action())
actions = [Action(), Run(), Fly(), 123]
while True:
    a = int(input("Select action: 0-Action, 1-Run, 2-Fly: "))
    h.action = actions[a]
    h.action.do_action()


