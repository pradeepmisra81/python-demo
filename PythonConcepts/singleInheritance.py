# Parent class
class ParentClass:
    def par_func(self):
         print("I am parent class function")

# Child class
class ChildClass(ParentClass):
    def child_func(self):
         print("I am child class function")

# Driver code 1
# obj1 = ChildClass()
# obj1.par_func()
# obj1.child_func()

# Driver code 2
obj2 = ParentClass()
obj2.par_func()
# obj2.child_func() #this will throw error: Traceback (most recent call last): \n File "singleInheritance.py", line 19, in <module> \n obj2.child_func() \n AttributeError: 'ParentClass' object has no attribute 'child_func'