input_string = input("Enter elements of a list separated by space ")
print("\n")
user_list = input_string.split()
# print list
print("list: ", user_list)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

res = [*set(user_list)]
print("List after removing duplicate elements: ", res)

# l = [1, 2, 4, 2, 1, 4, 5]
# print("Original List: ", l)
# res = [*set(l)]
# print("List after removing duplicate elements: ", res)
