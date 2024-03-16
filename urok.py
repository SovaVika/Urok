class Student:
    print("Hello")
    def __init__ (self):
        self.height = 160
        self.money = 100
        print("Init")

s = Student()
s2 = Student()
s.money = 200
print(s.money, s2.money)