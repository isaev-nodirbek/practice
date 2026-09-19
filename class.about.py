# '''CLASS
#    (1) What is class
#    (2) Ordinary vs static properties
#    (3) special/magic methods
# '''

# import datetime
# print("============ What is class ================")
# # class - blueprint for object creation
# # structure > state constructor method


# class Person():
#     # state
#     message = "class state property"

#     # constructor
#     def __init__(self, name, age):  # self = this in other langauges
#         self.name = name
#         self.age = age

#     # method
#     def introduce(self):
#         print(f"{self.name} says: How dod you do!")

#     def say_age(self):
#         print(f"{self.name} says I am {self.age}!")

#     @classmethod
#     def explain(cls):
#         print("Static method property executed")


# person1 = Person("Nolan", 25)
# person2 = Person("Justin", 27)
# person3 = Person("Mark", 28)

# # ordinary state
# print("person1.name", person1.name)

# # ordinary method
# person1.introduce()
# person2.say_age()


# print("============ Ordinary vs static properties ================")

# # static state
# new_message = Person.message
# print("new_message: ", new_message)

# # static method
# Person.explain()

# print("============ special/magic methods ================")
# # Pyhton's most common special methods are below
# # __init__, __new__, __str__, __call__, __getitem__, __eq__, __len__


# class Car():
#     # state
#     description = "This class makes cars"

#     # constructor
#     def __new__(cls, *args):
#         print("* __new__ *")
#         return super().__new__(cls)

#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#     # method
#     def start_engine(self):
#         print(f" the {self.name} started engine!")

#     def stop_engine(self):
#         print(f" the {self.name} stopped engine!")

#     def __str__(self):
#         return f"The car.name: {self.name} was produced in {self.year} year"

#     def __call__(self):
#         print("Object is called as function!")
#         return True


# my_car = Car("Ferrari", 2025)
# my_car.start_engine()
# my_car.stop_engine()

# print("--------")
# your_car = Car("Toyota", 2026)
# print(your_car)
# response = your_car()  # CALL look like function
# print("response: ", response)

import datetime


class Shop ():
    def __init__(self, bread, lagman, cola):
        self.products = {"bread": bread, "lagman": lagman, "cola": cola}

    def _time(self):
        return datetime.datetime.now().strftime("%H:%M")

    def qoldiq(self):
        time = self._time()
        print(
            f"Hozir {time}da shopda bread {self.products['bread']} ta,cola {self.products['cola']} ta, lagman {self.products['lagman']} ta bor")

    def sotish(self, product, quantity):
        if product not in self.products:
            print("Bizda bu mahsulot mavjud emas")
            return
        if quantity > self.products[product]:
            print(
                f"Bizda {product} mahsulotidan dan {quantity} ta   mavjud emas")
            return
        self.products[product] -= quantity
        print(f"Soat {self._time()} da {product} dan {quantity} dona sotildi")
        self.qoldiq()

    def qabul(self, product, quantity):
        if product not in self.products:
            print("Bizda bu mahsulot mavjud emas")
            return
        self.products[product] += quantity
        print(
            f"Soat {self._time()} da {product} dan {quantity} dona qabul qilindi")
        self.qoldiq()


shop = Shop(4, 5, 2)
shop.qoldiq()
shop.sotish("bread", 2)
shop.qabul("cola", 10)
