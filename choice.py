
#
# wrapper class for the game choices
#
class Choice:
    def __init__(self, code, message, action):
        self.code = code
        self.message = message
        self.action = action

    def perform(self):
        self.action()