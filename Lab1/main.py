import Avtomat_sm

class AppClass:

    def __init__(self):
        self._fsm = Avtomat_sm.AppClass_sm(self)
        self.is_valid = False
        self.counter = 0

    def IncCounter(self):
        self.counter += 1

    def ResetCounter(self):
        self.counter = 0

    def Valid(self):
        self.is_valid = True

    def Invalid(self):
        self.is_valid = False

    def check(self, string):
        self._fsm.enterStartState()
        #print(self._fsm._state)
        if(len(string) > 63):
            return False
        for char in string[:6]:
            #print(self.counter, char)
            self._fsm.nfs(self.counter, char)
            #print(self._fsm._state)
        for char in string[6:]:
            self._fsm.CheckChar(self.counter, char)
        self._fsm.EOS(self.counter)
        return self.is_valid


file = open('string.txt', 'r')
string = file.read();

Avtomat = AppClass()
result = Avtomat.check(string)
print(string)
print(result)

