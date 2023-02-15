class full_name():
    def __init__(self, first, second, age, gender):
        self.first = first
        self.second = second
        self.age = age
        self.email = first + "." + second + "@gmail.com"
        self.gender = gender

    def myfunc(self):
        print(self.email)

    def myfunc2(self):
        if self.gender == "male":
            print(65 - self.age)
        else :
            print(63 - self.age)

first = str(input())
second = str(input())
age = int(input())
gender = str(input())
p1 = full_name(first, second, age, gender)
p1.myfunc()
p1.myfunc2()