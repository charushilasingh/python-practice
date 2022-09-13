# List Operations
from operator import length_hint


My_List = ["play", "sing", "Dance", "write"]
print(My_List)

# Length
Lenghth_list = len(My_List)
print("Lenghth_list =  ", Lenghth_list)

# Existence of item in list
print("draw" in My_List)  # output False
print("play" in My_List)  # output True
print("PLAY" in My_List)  # output false # in upper not in lower case sensetive

# index
print(My_List.index("sing"))
print(My_List.index("play"))
# print(My_List.index("vhg"))  # not present in list error
print(My_List[2])
print(My_List[-1])  # end first

# Change List Item value
My_List[0] = "Rangoli"
print(My_List[0])
print(My_List)
# other list item value
# My_List[My_List.index("Dance")] = "cook"
My_List[My_List.index("Dance")] = "cook"
print(My_List)

# Append item
My_List.append("garden")  # at last addition
print(My_List)

# Insert item to a limit
My_List.insert(2, "walking")
print(My_List)
# other method to insert item to a limit with index use

My_List.insert(My_List.index("write"), "rock")  # index write before that addition
print(My_List)

# Remove item from a list
My_List.remove("walking")
print(My_List)

# Remove item  at a specified index
My_List.pop(1)
print(My_List)

# Empty a List
My_List.clear()
print(My_List)  # empty a list

# concatenate
months = ["jan", "feb", "march", "april"]
seasons = ["autum", "winter", "spring", "summer"]
print(months, seasons)
print(months + seasons)

# Extend
# no need to crate new list everytime just use extend in already present list
months.extend(seasons)
print(months)
# print(months + seasons)
# # seasons remain unchanged months list changed

# slicing
# use of index tp acces the item but if range then slicing best option
# Returns specified number of range

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "voilet"]
print("length", len(rainbow))
print(rainbow[1:4])
print(rainbow[3:])
print(rainbow[:5])
print(rainbow[-5:-2])
