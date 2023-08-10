class CheckParity:
    def __init__(self, *args):
        if isinstance(args[0], int):
            self.number = args[0]
            if len(args) > 1:
                self.parity = args[1]
        else:
            self.number = None

    def isOdd(self):
        # This function checks if the integer is Odd, and returns True else returns False
        if self.number != None:
            if self.number % 2 != 0:
                return True
            else:
                return False
        else:
            return "error"

    def isEven(self):
        # This function checks if the integer is even, and returns True else returns False
        if self.number != None:
            if self.number % 2 == 0:
                return True
            else:
                return False
        else:
            return "error"

    def getParity(self):
        # This function checks if the parity given matches
        if self.number != None:
            if self.parity == "odd":
                return self.number % 2 != 0
            elif self.parity == "even":
                return self.number % 2 == 0
            else:
                return "Parity indicated is unknown"
        else:
            return "Not an integer"


a = CheckParity(6)
b = CheckParity(5, "odd")
c = CheckParity(3.5)

print(CheckParity.isEven(a))
print(CheckParity.isOdd(a))
print(CheckParity.getParity(b))
print(CheckParity.isOdd(c))
