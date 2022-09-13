# String_Methods
quote = "     dream it.wish it.do it "
print(quote)
print(quote.strip())  # before strip removal
# capatilize
print(quote.capitalize())
# o/p only fisrt character : Dream it. wish it do it

# Title
print(quote.title())  # o/p fisrt character of all : Dream it. Wish it Do it

# Strip()
quote1 = "!!!!dream it.wish it.do it"
print(
    quote1.strip("!")
)  # quote = "!!!!dream it. wish it.do it " o/p : dream it. wish it.do it

# Concatenation
print(quote1 + quote)
print(quote1 + "     " + quote)

# type convesion
city = "Los Angeles"
print(type(city))

state = "CA"
zip_code = 90028
print(type(zip_code))

location = (
    city + " " + state + " " + str(zip_code)
)  # canges for typing int to string main itnt remains as it is no changes in original

print(location)
