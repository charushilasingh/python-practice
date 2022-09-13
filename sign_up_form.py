# Dictionary that stores the audition sign ups
from concurrent.futures import process


auditions = {"principal": {}, "teacher": {}, "troublemaker": {}, "student": {}}
# function for the sign-up process
def sign_up():
    name = input("What is your name ?: ").capitalize()
    grade = str(input("what is your grade:?(please respond with a number)"))
    role = input(
        """ What is your prefereedrole? please select a number from the following options:
    [1]Principal
    [2] Teacher
    [3] Troublemaker
    [4] student
    """
    )
    if role == "1":
        auditions["principal"][name] = grade
    elif role == "2":
        auditions["teacher"][name] = grade
    elif role == "3":
        auditions["troublemaker"][name] = grade
    else:
        auditions["student"][name] = grade


for i in range(5):
    sign_up()


# prnt list of studentssigned up to audition
print("sig-ups for a day without ptincipal are now closed")
print("Role:Principal")
for student, grade in auditions["principal"].items():
    print(student, grade)
    print("Role:teacher")
for student, grade in auditions["teacher"].items():
    print(student, grade)
print("Role:troublemaker")
for student, grade in auditions["troublemaker"].items():
    print(student, grade)
print("Role:student")
for student, grade in auditions["student"].items():
    print(student, grade)
