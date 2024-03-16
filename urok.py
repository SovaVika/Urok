class Student:
    print("Hello")
    def __init__ (self, name, money, height):
        self.name = name
        self.height = height
        self.money = money
        print("Init")
    def BuyPizza(self):
        self.money -= 100
        print("Now you have" , self.money, "money and pizza")

class Car:
    def __init__ (self):
        self.color = "red"
        self.model = "Bugatti"
        print("Init")

s = Student("Alex", 200, 190)
s2 = Student("Kate", 300, 170)
print(s.name,s.money,s2.name,s2.money)
s.money = 200
car = Car()
print(car.color,car.model)
print(s.money, s2.money)
s.BuyPizza()