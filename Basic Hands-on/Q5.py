'''Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.'''


class GetAndPrintString(object):

    def getString(self):
        self.value = input('Enter some string: ')

    def printString(self):
        print(self.value.upper())
        print(str.upper(self.value))


s = GetAndPrintString()
s.getString()
s.printString()
