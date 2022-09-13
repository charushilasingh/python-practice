# Shopping cart :buying things with tas of 6 % included in bill

# quantity of the shopping items

flower_pot = int(input("How many flower pots ? :"))
flower_seeds = int(input("How many flower seeds ? :"))
soil = int(input("How many soil Bags?:"))

# cost of each shoppingitem
flower_pot_Price = 4.00
flower_seeds_Price = 1.00
soil_Price = 5.00

# sales tax
tax_rate = 0.06

# calculate the cost of items
Cost_of_items = (
    (flower_pot * flower_pot_Price)
    + (flower_seeds * flower_seeds_Price)
    + (soil * soil_Price)
)

# total cost

Total_cost = (Cost_of_items * tax_rate) + Cost_of_items

print("Total Cost : ", Total_cost)
