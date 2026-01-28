class Student:
    def __init__(self, name ,id):
        self.name = name
        self.id = id

s1 = Student("Fatih" , "35239")

print(s1.name)
print(s1.id)


class Car:
    def __init__(car, brand ,model):
        car.brand = brand
        car.model = model

c1 = Car("mercedes" , "c250")

print(c1.model)
print(c1.brand)
        