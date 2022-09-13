# If_else_What_to_Wear

# current temperature by user
temperature = int(input("What is the current Temperature?: "))
# Comparision with current temperature to choose
if temperature >= 80:
    outfit = "Light Clothes , shorts with sunglasses"
elif temperature >= 79 and temperature >= 60:
    outfit = "A light jacket"
else:
    outfit = "A coat in addition to a hat, gloves, and scarf"
# Advice for the user
advice = f"Today you should wear {outfit}."
print(advice)
