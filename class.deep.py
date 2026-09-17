'''CLASS deep diving
  (1) ENCAPSULATION
  (2) INHERITENCE
  (3) POLIMORPHISM
'''
print("========== ENCAPSULATION ============")
'''
C++ JAVA > public private protected
PHP TypeScript > public private protected
Phyton > public __private _protected
'''
# ENCAPSULATION > public __private _protected


class Account():
    # state
    description = "The class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method

    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("depsoit: ", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw: ", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    def change_ownership(self, new_owner):
        print("change_ownershi:", new_owner)
        self.__owner = new_owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter: ", new_owner)
        self.__owner = new_owner


my_account = Account("Nolan", 1000)
my_account.get_balance()

print("-----------")
my_account.deposit(3500)
my_account.get_balance()
my_account.withdraw(400)
my_account.get_balance()

print("-----------")

try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("No target state found:", err)

account_owner = my_account.holder  # state
print("account_owner:", account_owner)

print("owner before: ", my_account.holder)  # state

# my_account.change_ownership("Martin")
my_account.holder = "Martin"

print("owner after: ", my_account.holder)  # state

print("========== INHERITENCE  ============")

'''
Parent provides only public & protected(state and methods) to children!

'''


class Animal:
    # state
    description = "The class creates animals"

    # constructor
    def __init__(self, voice):
        self._status = "Animal is alive"
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

    # merthod
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


Dog.introduce()
Fish.introduce()
Cat.introduce()

print("-------")
Dog.make_voice()
Fish.make_voice()
Cat.make_voice()

print("-------")
print(Animal.description)
print(dog.description)

print("-------")
print(Dog.voice, Fish.voice)
print(Dog._status)
print(Fish._status)


print("========== POLIMORPHISM ============")
Dog.make_voice()
Fish.make_voice()

print("-------")
# Fish > fish > Animal > object
a = isinstance(Fish, fish)
b = isinstance(Fish, Animal)
c = isinstance(Fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print(f"the result: {result}")

# fish > Animal > object

data1 = issubclass(fish, Animal)
data2 = issubclass(Animal, object)
print(data1)
