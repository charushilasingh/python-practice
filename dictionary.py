math_test = {
    "angelo": 77,
    "Samir": 93,
    "Rkul": 67,
    "louis": 98,
    "Anjali": 87,
    "Tina": 89,
}
print(math_test)
for student in math_test:
    print(math_test[student])  # printkey value
    print(student)  # print key

    # 0ther method
for student in math_test.values():
    print(student)  # printing values of respective keys

for student, score in math_test.items():
    print(student, score)  # prnting both keys and value at a time

# nested_dictionary

gradebook = {
    "mylene": {"English": "a", "math": "a", "science": "b", "gpa": 3.7},
    "terrell": {"English": "c", "math": "b", "science": "a", "gpa": 3.2},
    "Joseph": {"English": "b", "math": "b", "science": "b", "gpa": 3.0},
}
print(gradebook["mylene"]["English"])
for all in gradebook.values():
    print(all)

# addition of key value pair in nested

gradebook["mylene"]["art"] = "a"
print(gradebook["mylene"])

# to change in nested
gradebook["mylene"]["English"] = "B"
print(gradebook["mylene"]["English"])
print(gradebook)
print("---------------------------")
gradebook["mylene"].popitem()  # remove last item in respected dictionary
print(gradebook)
# gradebook.clear() #clear
# print(gradebook)
gradebook.pop("mylene")  # remove mylene
print(gradebook)
del gradebook["terrell"]  # delete terrell
print(gradebook)
# del gradebook
# print(gradebook)
