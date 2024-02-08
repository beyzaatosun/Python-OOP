# -*- coding: utf-8 -*-
"""
Encapsulation
"""
class BankAccount(object):
    
    def __init__(self, name, money, adress):
        self.name=name
        self.__money=money
        self.adress=adress
    
    def getMoney(self):
        return self.__money
    
    def setMoney(self,amount):
        self.__money=amount
    
    
p1=BankAccount("raye", 1000, "türkiye")
print("get method",p1.getMoney())
p1.setMoney(5000)
print("new get method",p1.getMoney())


"""
Abstract 
"""
from abc import ABC, abstractmethod

class Polygon(ABC):
    
    @abstractmethod
    def numbersides(self):
        pass

class triangle(Polygon):
    
    def numbersides(self):
        print("I have three sides")
        
class pentagon(Polygon):
    
    def numbersides(self):
        print("I have five sides")
        
#a1=Polygon()-> bu satır hata döndürecektir çünkü abstract classtan nesne oluşturulmaz
        
b1=triangle()
b1.numbersides()

c1=pentagon()
c1.numbersides()


"""
Overriding
"""
class Animal():
    def move(self):
        print("move")

class Dog(Animal):
    def move(self):
        print("run")

d1=Animal()
d1.move()
f1=Dog()
f1.move()        

"""
Polymorphism
"""

class Employee():
    
    def salary_raise(self):
        raise_rate=0.1
        return 100+100*raise_rate

class Engineer(Employee):
    
    def salary_raise(self):
        raise_rate=0.3
        return 100+100*raise_rate
    
class Manager(Employee):
    
    def salary_raise(self):
        raise_rate=0.5
        return 100+100*raise_rate
    
e1=Employee()
print("Employee:",e1.salary_raise())

e2=Engineer()
print("Engineer:",e2.salary_raise())

e3=Manager()
print("Manager:",e3.salary_raise())
    

