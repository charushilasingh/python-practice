# for loop
# iterate over a string
Name = "Vaibhav"
for item in Name:
    print(item)

# Iterate over a list
continents = [
    "asia",
    "africa",
    "north america",
    "south america",
    "antartica",
    "europe",
    "australia",
]
for item in continents:
    print(item)

# create a break statement
for item in continents:
    print(item)
    if item == "antartica":
        break

# create continue statement
print(continents)
for item in continents:
    if item == "North america":
        continue
    print(item)

# range
for x in range(11):
    print(x)

for x in range(3, 8):
    print(x)

for x in range(10, 100, 10):  # start stop step
    print(x)
