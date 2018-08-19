# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#**************define a (badly designed) class
class BadVehicle:
    def run():
        print("Inside Run - Vehicle");

car = BadVehicle();
print(car)

#Add some properties to the object dynamically
car.make="Maruti"
car.chasis_no=132124
car.noOfSeats=2
print(car.make)


#***********define a (properly designed) class
class Vehicle:
    raise_amount=1.6
    #constructors overloading is not suppored. The most recent cnstr is taken
    #contructor - 2 args
    def __init__(self, make):
        self.make=make
        self.price=10000
        
    def __init__(self, make, price): #this cnstr is always taken
        self.make=make
        self.price=price
    
    #define a method
    def printDetails(self):
        return "{} starting price is {}".format(self.make,str(self.price))
    
    def printOnRoadPrice(self):
        self.onRoadPrice = self.price*self.raise_amount
        return self.onRoadPrice

#create objects   
car1 =Vehicle("Hyundai", 1200000)
car1.printDetails()
car1.printOnRoadPrice()

car2 = Vehicle("Mahindra", 1000000)
car2.printDetails()
print("{}".format(car2.printOnRoadPrice()))


#********Inheritance
class ThreeWheeler(Vehicle):
    def __init__(self, make, price, meter_type):
        super().__init__(make,price)
        self.meter_type=meter_type
    
    #Method overriding
    def printDetails(self):
        return "{} rickshaw with {} meter: starting price is {}".format(self.make, self.meter_type, str(self.price))
    
auto=ThreeWheeler("Bajaj", 50000, "digital")
auto.printDetails()
auto.printOnRoadPrice()
#some inbuild funtions are:
print(isinstance(auto,Vehicle))
print(isinstance(auto,ThreeWheeledVehicle))
print(issubclass(ThreeWheeledVehicle,Vehicle))
dir(auto)


#**********Abstraction (Access modifiers)
class Institution:
    def __init__(self):
        self.__donation=10000 #private prop
        self._fees=5000 #protected prop
        self.name="Baldwin" #public prop
    
    def printAll(self):
        print("printAll")
    
    def _printSome(self):
        print("printSome")
        
    def __printDont(self):
        print("printDont")

school = Institution()
school._fees #protected is visible here
school.name #public is visible here
dir(school)

school.printAll() #works
school._printSome() #works
school.__printDont() #not works

#Polymorphism
def summ(a):
    return "10"+str(a)
summ(10)
summ("A")

#argsC and argsV
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info('Siva','Sub',name="Sid")


#Multiple inheritance
class Father:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class Mother:
    def __init__(self,c,d):
        self.c=c
        self.d=d

class Child(Father,Mother):
    def __init__(self,a,b,c,d,e):
        Father.__init__(self,a,b)
        Mother.__init__(self,c,d)
        self.e=e

child_1=Child(1,2,3,4,5)
print(child_1.e)


#define an empty class
class EmptyClass:
    pass
