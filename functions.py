''' FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) scope
'''


print("====== DEFINE vs CALL ========")
# built in function > print() type()
# Function - reusable block of codes!
# Instead of block {} in JAVA, Python uses indentation!

# DEFINE - buil
# parametr => define qismida beriladi


def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute
# argument => call qismda keladi
result1 = greet('Nolan')
print("result1: ", result1)

result2 = greeting("Justin bro")
print("result2: ", result2)

print("====== Keyword & default arguments ========")


# DEFINE


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, are you {age} years old ?"


# CALL
result3 = give_greet(name="Justin bro", age=28)
print("result3 : ", result3)

result4 = give_greet(name="Nolan")
print("result4 : ", result4)

print("====== Scope ========")
b = 100  # 3


# DEFINE
def calculate(a, b):  # 2
    c = a*b  # 1
    print(f"the c value: {c}")


# CALL
calculate(5, 50)
