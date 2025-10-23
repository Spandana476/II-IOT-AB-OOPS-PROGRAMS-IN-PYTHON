class student:
    def __init__(self,name):
        self.name = name
    def show(self):
        print('Hello,my name is',self.name)
    def __del__(self):
        print("object destroyed")
        
s1=student("Spandana")
s2=student("iot")
s2.show()
del s1
s1.show()
        
