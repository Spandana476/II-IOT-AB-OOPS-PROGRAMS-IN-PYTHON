class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.__salary=salary
        
    def show_salary(self):
        print("salary:", self.__salary)

emp = Employee("Robert", 60000)
print(emp.name)
emp.show_salary()
