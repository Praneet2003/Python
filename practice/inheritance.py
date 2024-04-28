class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def ShowDetails(self):
        print("The Employee name is {} and his/her id is {}".format(self.name,self.id))
e = Employee("Mehul",39)
e.ShowDetails()   
# If i want to add one more class as a programmer then we can use inheritance in this case.
class Programmer(Employee):
    def ShowLanguage(self):
        print("and he is a programmer Whose Default language is Python")
a = Programmer("Praneet",40)
a.ShowLanguage()