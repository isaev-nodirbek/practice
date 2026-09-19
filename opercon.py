'''OPERATORS & CONDITIONS
    (1) Operators
    (2) Condition
    (3) Logical Operators
'''

print("========= Operators ==========")
# + - > >= < <= /    // % += **

a = 19
b = 5

# print("a > b", a > b)
# print("a >= b", a >= b)
print("a / b", a/b)
result = a // b  # Butun natija yani butun son
left = a % b  # Qoldiqdagi natija
print(f"the result: {result} and left: {left}")

# a = a + 100
a += 100
print("a :", a)


print("b**2", b**2)
print("b**3", b**3)

print("="*5)

c = dict(name="Nolan", age=25)
d = dict(name="Nolan", age=25)
e = c
print("c==d", c == d)  # In Python only values are compared
print(id(c), id(d), id(e))

print("c is d", c is d)
print("c is e", c is e)


print("========= Condition ==========")
x = 15

if x > 50:
    print("Case a")
elif x > 10:
    print("Case b")
else:
    print("Case c")


print("========= Logical Operators ==========")
age = 20
# person = None
# if age > 16:
#     person = "Adult"
# else:
#     person = "Child"

# print("person:", person)

# Ternary
person = " adult" if age > 18 else "minor"
print("person:", person)

print("--------")

is_student = True
is_admin = False
is_guest = True
is_parent = False

if not is_student:
    print("Welcome here, do you want to be student")
elif is_admin:
    print("Please go to this office!")
# elif is_guest and is_parent:
elif is_parent or is_parent:
    print("Waiting room is over there!")
else:
    print("Other cases")
