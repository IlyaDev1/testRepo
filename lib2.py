class User:
    __name = ''
    __balance = 0

    def __init__(self):
        print(self)

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setBalance(self, value):
        self.__balance = value

    def getBalance(self):
        return self.__balance

    name = property(getName, setName)
    balance = property(getBalance, setBalance)
