# classes are user defined blueprint or prototype
# a class consists of methods, class variables, instance variables, constructor, etc.
'''
- 'self' is mandatory for calling variable names into method
- instance and class variables have whole different purpose
- constructor name should be __init__
'''
class Calculator:
    # class variables
    num = 100

    # default constructor
    def __init__(self, a, b): # argument, self is object reference
        self.a = a # argument saved as instance variables
        self.b = b
        print("I am called automatically when object is created")
    # method
    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.a + self.b + self.num # class variable can also be referenced

calculator = Calculator(2,3) # syntax to create objects in python
calculator.getData()
print(calculator.num)
print(calculator.Summation())