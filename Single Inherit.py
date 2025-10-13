#Single Inheritance
class A:

    def displayA(self):
        print("Inheritance A Class")

class B(A):

    def displayB(self):
        print("Inheritance B Class")

obj=B()
obj.displayA()
obj.displayB()
