class person:
    def __init__(self,name,occu):
        print("hello i am ",end=" ")
        self.name = name
        self.occ = occu
    def info(self):
        print("{} and i am a {}".format(self.name,self.occ))
a = person("Praneet","Data Scientist")
a.info()
class car:
    def __init__(self,brand,model,year):
        print("Details of the car")
        self.brand = brand
        self.model = model
        self.year = year
    def info(self):
        print("The car brand is {} , model is {} and it's manufacturing year is {}".format(self.brand,self.model,self.year))
car1 = car("ford","Mustang",2007)
car1.info()

class me:
    name = "Praneet Raj"
    age = 20
    education = "At Lpu"
    def info(self):
        print("Hey i am {}, my age is{} and my education is {}".format(self.name,self.age,self.education))
a = me()
a.info()
print("\n")
b = me()
b.name = "Mehul"
b.age = 21 
b.education = "At Pbs"
b.info()