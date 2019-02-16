"""
1) Class
2) OOP's Concept
3) Abstraction
4) Encpasulation
5) Inheritance
6) Polymorphism
"""

class classname(object):
    """
    class level doc string
    """
    def __init__(self, name):
        self.name = name
    def my_function(self):
        """
        :return:
        """
        print(F'Hello my Function {self.name}')
    def my_function2(self):
        print(F"hello {self.name}")
print('==============================================================')
_class = classname(name="Chandrakant")
_class.my_function()
_class.name="Vote For BJP"
_class.my_function2()
_class.my_function()

print('===============================================================')
class2 =classname(name='PPP').my_function()

print('===============================================================')
class3 =classname(name='BJP').my_function()