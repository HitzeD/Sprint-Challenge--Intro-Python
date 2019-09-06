# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"<Human: {self.name}, {self.age}"

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
for person in humans:
    if person.name.lower()[0] == 'd':
        a.append(person.name)
# print(a)

# good above

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
for person in humans:
	if person.name.lower()[-1] == 'e':
		b.append(person.name)

# print(b)

# good up

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
for person in humans:
	if ord(person.name.lower()[0]) in range(ord('c'), ord('h')):
		c.append(person.name)
# print(c)

# good

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for person in humans:
    d.append(int(person.age) + 10)
# print(d)

# good

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for person in humans:
    e.append(f"{person.name}-{person.age}")
# print(e)

# good

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for person in humans:
    if person.age in range(27, 33):
        tuples = tuple((person.name, person.age))
        f.append(tuples)
# print(f)

# good

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = [Human(str.upper(i.name), i.age + 5) for i in humans]

print(f"G AFTER: {g}\n")

# good
print(f"HUMANS AFTER: {humans}")

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
for person in humans:
	pass
	h.append(math.sqrt(person.age))
# print(h)