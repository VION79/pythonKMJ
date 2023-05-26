# Declare a function that accepts a temprature in Celsius and returns it in Fahrenheit

def convert_to_fahrenheit(celsius_temp):
    product = celsius_temp * 1.8
    return product + 32

convert_to_fahrenheit(0)
32.0

convert_to_fahrenheit(14)
57.2

convert_to_fahrenheit(celsius_temp = 24)
75.2

def convert_to_fahrenheit(celsius_temp = 0):
    product = celsius_temp * 1.8
    return product + 32

convert_to_fahrenheit()
32.0

##############################    

# Define a easy_money function that accepts no parameters 
# and always returns the value 100.
def easy_money ():
    return 100


# Define a best_food_ever function that accepts 
# no parameters and always returns the string “Sushi”.
def best_food_ever ():
    return "Sushi"


# Define a convert_to_currency function that accepts a single parameter (an integer). 
# The function should convert the argument to a string, prefix it with a dollar sign, and return the result.
# 
# EXAMPLES:
# convert_to_currency(15)    =&gt; "$15"
# convert_to_currency(8)     =&gt; "$8"

def convert_to_currency (integer):
    return "$" + str(integer)

profession = "Developer"
profession.upper()

