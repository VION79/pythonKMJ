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

## String Method ####

profession = "Developer"
profession.upper()
'DEVELOPER'

"Developer".upper()
'DEVELOPER'

profession.lower()
'developer'

profession.swapcase()
'dEVELOPER'

# immutable - incapable of change
# mutable - capable of change
# string - immutable

profession
'Developer'

"once upon a time".title()
'Once Upon A Time'

"once upon a time".capitalize()
'Once upon a time'

"ronald mcdonald".title()
'Ronald Mcdonald'

profession = "             Developer         "
profession.lstrip()
'Developer         '

profession.rstrip()
'             Developer'

profession.strip()
'Developer'

profession.replace("e", "*")
'             D*v*lop*r         '

profession.strip().replace("e", "*")
'D*v*lop*r'

animal = "rhinoceros"
animal.startswith("rhino")
True

animal.startswith("rino")
False

animal.endswith("ros")
True

animal.endswith("z")
False

"ino" in animal
True

"ceros" in animal
True

"xz" in animal
False

"z" not in animal
True

"rhino" not in animal
False

# Define a 'scientist' variable set to the string 'albert einstein'
# Invoke the title method on the string/variable
# Assign the returned string to a 'proper_name' variable
scientist = "albert einstein"
proper_name = scientist.title()

# The 'wasteful_string' below has a lot of useless whitespace
# Invoke the correct method on wasteful_string to clear ALL whitespace (beginning and end)
# Assign the returned string from the correct method to an 'unwasteful_string' variable
wasteful_string = "     9:00PM     "
unwasteful_string = wasteful_string.strip()

# The party_attendees string below contains a list of people attending our party
# Use the 'in' operator to determine if "Ron" is attending the party
# Assign the resulting Boolean to an 'is_attending' variable
party_attendees = "Sharon, James, Ron, Blake"
is_attending = "Ron" in party_attendees

# Declare a cleanup function that accepts a single string input
# The function should
#  1) remove all leading and trailing whitespace from the input string
#  2) capitalize the first letter of the input string
#  3) return the new string
# EXAMPLES:
# 
# cleanup("  hello  ")               =&gt; "Hello"
# cleanup("   see you tomorrow   ")  =&gt; "See you tomorrow"

input_string = "  hello  "
def cleanup(input_string):
    return input_string.strip().capitalize()





