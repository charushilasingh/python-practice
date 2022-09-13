# # While_loop
# x = 10
# while x > 0:
#     print(f"x is greater than 0, {x}")
#     x -= 1

# num = 2
# while num <= 10:
#     if num == 8:
#         break
#     print(num)
#     num += 2

# num = int(input("Enter any number : "))
num = 2
while num <= 100:
    if (num % 2) == 0:
        print(f" {num} is a even number")
    num += 1
    continue

# example model rocketlaunch
# if windy no rocket launch else launch no/yes
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
    if input("Is it windy? ") == "yes":
        print("mission impossible Aborted")
        break
else:
    print("we have liftoff")
