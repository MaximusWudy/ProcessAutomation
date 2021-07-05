'''
without redefining properties or methods, you can simply inherit all the properties
from your parent to child class
'''
from OopsDemo import Calculator # import classes first, from 'filename' import 'classname'


class ChildImpl(Calculator): # parent class in parenthesis
    num2 = 200

    def __init__(self):
        # if parent constructor is not default, then you need to call the parent constructor
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj = ChildImpl()
print(obj.getCompleteData())
