class Person:  ## class
    def __init__(self, fname, lname):  ## constructor method
        self.firstname = fname  ## instance variable
        self.lastname = lname  ## instance variable
        
    def printname(self): ## Method
        print(self.firstname, self.lastname) ## print variable of the object

class Student(Person): ## inherit person class to student class
    def __init__(self, fname, lname, year):  ## constructor method
        super().__init__(fname, lname) ## call the parent class constructor
        self.graduationyear = year  ## instance variable
        
x = Student("Mike","Olsen", 2019)  ## create instance variable of student class 
print(x.printname())  ## method on x object
print(x.graduationyear)  ## print instance variable