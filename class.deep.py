'''CLASS deep diving
  (1) ENCAPSULATION
  (2) INHERITENCE
  (3) POLIMORPHISM
'''
print("========== ENCAPSULATION ============")

'''
C++ JAVA > public private protected
PHP TypeScript > public #private _protected
Phyton > public  __private  _protected
'''
# ENCAPSULATION > public __private _protected


# class Account():
#     # state
#     description = "The class makes bank accounts"

#     # constructor

#     def __init__(self, owner, amount):
#         self.__owner = owner
#         self.__amount = amount

#     # method

#     def get_balance(self):
#         print(f"the owner {self.__owner} has {self.__amount} usd")

#     def deposit(self, amount):
#         print("depsoit: ", amount)
#         self.__amount += amount

#     def withdraw(self, amount):
#         print("withdraw: ", amount)
#         self.__amount = self.__amount - amount

#     def __call__(self):
#         print("Hello!!!!")

#     @classmethod
#     def get_name(cls):
#         print(" The classmethod is working")

#     @staticmethod
#     @property  # getter
#     def holder(self):
#         return self.__owner


# my_account = Account("Nolan", 1000)
# my_account.get_balance()


# print("-----------")
# my_account.deposit(3500)
# my_account.get_balance()
# my_account.withdraw(400)
# my_account.get_balance()
# Account.get_name()
# print(Account.description)
# my_account()
# Account.abc()


# print("-----------")

# try:
#     result = my_account.__amount
#     print("result:", result)
# except Exception as err:
#     print("No target state found:", err)

# account_owner = my_account.holder  # state
# print("account_owner:", account_owner)

# print("owner before: ", my_account.holder)  # state

# # my_account.change_ownership("Martin")
# my_account.holder = "Martin"

# print("owner after: ", my_account.holder)  # state

# print("========== INHERITENCE  ============")

# '''
# Parent provides only public & protected(state and methods) to children!

# '''


class Animal(object):
    # state
    description = "The class creates animals"
    _status = "Animal is alive"
    # constructor

    def __init__(self, voice):

        self.voice = voice

    # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class dog(Animal):  # Child

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, I can protect you")

    def make_voice(self):
        print(f"This {self.name} says {self.voice}")


class cat(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class fish(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # merthod
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes, I can swim")


Dog = dog("Rex", "wow", True)
Cat = cat("TOM", "meow", True)
Fish = fish("Nemo", "ZzZ", False)


# Dog.introduce()
# Fish.introduce()
# Cat.introduce()

# print("-------")
# Dog.make_voice()
# Fish.make_voice()
# Cat.make_voice()

# print("-------")
# print(Animal.description)
# print(dog.description)

# print("-------")
# print(Dog.voice, Fish.voice)


# print("========== POLIMORPHISM ============")
# Dog.make_voice()
# Fish.make_voice()
# Cat.make_voice()
# print(Animal._status)

# print("-------")
# # Fish > fish > Animal > object
# a = isinstance(Fish, fish)
# b = isinstance(Fish, Animal)
# c = isinstance(Fish, object)
# d = isinstance("MIT", object)
# result = a and b and c and d
# print(f"the result: {result}")

# # fish > Animal > object

# data1 = issubclass(fish, Animal)
# data2 = issubclass(Animal, object)
# print(data1)


class Student:
    def __init__(self, name, age, gpa):
        self.__name = name
        self.__age = age
        self.__gpa = gpa

    def get_info(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"GPA: {self.__gpa}")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Name cannot be empty")
            return
        self.__name = new_name


# Test qilish
student = Student("Nolan", 20, 3.7)

student.get_info()
print("-" * 20)

# Property orqali o'qish
print(student.name)
print("-" * 20)

# Property orqali yozish (setter)
student.name = "John"
student.get_info()
print("-" * 20)

# Validatsiyani tekshirish
student.name = ""
student.get_info()
