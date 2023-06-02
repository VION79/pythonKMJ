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

#### Test #### 

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

#####################
## String Method ####
#####################

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

#### Test ####

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

#################
##### LIST ######
#################

# Mutable data structure that holds an ordered collection of elements
#In
[1, 2, 3, 4]
#Out
[1, 2, 3, 4]
#In
[True, False, False, True]
#Out
[True, False, False, True]
#In
Party_attendees = ["Myung", "Michael", "Jason"]
Party_attendees
#Out
['Myung', 'Michael', 'Jason']
#In
len(Party_attendees)
#out
3
#In
type(Party_attendees)
#out
list
#in
presidents = ["Washington", "Jefferson"]
presidents
#out
['Washington', 'Jefferson']
#in
presidents.append("Madison")
presidents
#out
['Washington', 'Jefferson', 'Madison']
#in
popcorn = ["Salted", "Unsalted", "Caramel"]
popcorn
#out
['Salted', 'Unsalted', 'Caramel']
#in
popcorn.pop()
#out
'Caramel'
#in
popcorn
#out
['Salted', 'Unsalted']
#in
popcorn.remove("Salted")
popcorn
#out
['Unsalted']
#in
"cat" in "caterpillar"
#out
True
#in
planets = ["Mercury", "Venus", "Earth", "Mars"]
"Earth" in planets
#out
True
#in
"earth" in planets
False
#in
"Pluto" not in planets
#out
True
#in
"Mars" not in planets
#out
False

#### Test ####

# Create an empty list and assign it to the variable "empty".
empty = []

# Create a list with a single Boolean — True — and assign it to the variable "active".
active = [True]

# Create a list with 5 integers of your choice and assign it to the variable "favorite_numbers".
favorite_numbers = [1, 2, 3, 5, 6]

# Create a list with 3 strings  — "red", "green", "blue" — and assign it to the variable "colors".
colors = ["red", "green", "blue"]

# Declare an is_long function that accepts a single list as an argument
# It should return True if the list has more than 5 elements, and False otherwise
def is_long(list):
    return len(list) > 5

#######################################
##### Index Position and Slicing ######
#######################################

in 
spiderman = "Spiderman"
len(spiderman)

out
9

in
spiderman[0]
spiderman[1]
spiderman[4]
spiderman[8]

out
9

in
spiderman[-1]
spiderman[-9]

out
'S'

in
superheros = ["Spiderman", "Batman", "Superman", "Wolverine", "Ironman"]
len(superheros)

out
5

in
superheros[0]

out
'Spiderman'

in
superheros[-5]

out
'Spiderman'

in
superheros[4]

out
'Ironman'

in
superheros[-1]

out
'Ironman'

in
superheros[1:3]

out
['Batman', 'Superman']

in
superheros[2:4]

out
['Superman', 'Wolverine']

in
spiderman[1:5]

out
'pide'

in
superheros[0:2]

out
['Spiderman', 'Batman']

in
superheros[:2]

out
['Spiderman', 'Batman']

in
spiderman[0:6]

out
'Spider'

in
spiderman[:6]

out
'Spider'

in
superheros[2:5]

out
['Superman', 'Wolverine', 'Ironman']

in
superheros[2:6]

out
['Superman', 'Wolverine', 'Ironman']

in
superheros[2:]

out
['Superman', 'Wolverine', 'Ironman']

in
superheros[:]

out
['Spiderman', 'Batman', 'Superman', 'Wolverine', 'Ironman']

in
spiderman[3:9]

out
'derman'

in
spiderman[3:]

out
'derman'

in
spiderman[3:-1]

out
'derma'

in
spiderman[3:8]

out
'derma'

######### Test ###############

# The nuts list below contains 7 strings
nuts = ["Almonds", "Cashews", "Hazelnuts", "Brazil", "Macadamia", "Pecan", "Pistachio"]

# Extract the "Cashews" string by indexing into the "nuts" list above
# Assign the value to the variable below
cashews = nuts[1]

# Extract the "Pecan" string by indexing into the "nuts" list above
# Assign the value to the variable below
pecan = nuts[-2]

# Extract the "Pistachio" string by indexing into the "nuts" list above
# Assign the value to the variable below
pistachio = nuts[6]

# Extract the "Almonds" string by indexing into the "nuts" list above
# Assign the value to the variable below
almonds = nuts[-7]

#######################################
##### Dictionaries ######
#######################################

#An unordered collection of key-value pairs

in
#Filet mignon -29.99
menu = {
    "Filet Mignon": 29.99,
    "Big Mac": 3.99,
    "Pizza": 0.99,
    "Salmon": 29.99,
    "Pizza": 1.99
}
menu

out
{'Filet Mignon': 29.99, 'Big Mac': 3.99, 'Pizza': 1.99, 'Salmon': 29.99}

in
len(menu)

out
4

in
menu["tuna"]

out
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[64], line 1
----> 1 menu["tuna"]

KeyError: 'tuna'

#in
menu["Burrito"] = 13.99
menu

#out
{'Filet Mignon': 29.99,
 'Big Mac': 3.99,
 'Pizza': 1.99,
 'Salmon': 29.99,
 'Burrito': 13.99}

#in
menu["Pizza"] = 4.25
menu

#out
{'Filet Mignon': 29.99,
 'Big Mac': 3.99,
 'Pizza': 4.25,
 'Salmon': 29.99,
 'Burrito': 13.99}

#in
menu.pop("Filet Mignon")

#out
29.99

#in
menu

#out
{'Big Mac': 3.99, 'Pizza': 4.25, 'Salmon': 29.99, 'Burrito': 13.99}

#in
"Pizza" in menu
#out
True

#in
"Hot Pockets" in menu
#out
False

#in
"Bubble Gum" not in menu
#out
True

#in
"Burrito" not in menu
#out
False

#in
29.99 in menu
#out
False

#in
# 29.99 is not one of the keys therefore the result is false
menu.values()
#out
dict_values([3.99, 4.25, 29.99, 13.99])

#in
29.99 in menu.values()
#out
True

######## Test ###########
# Create an empty dictionary and assign it to the variable empty.
empty = {}

# Create a dictionary with three key-value pairs. 
# The keys should be strings and the values should be integer values. 
# Assign the dictionary to a my_dict variable.

my_dict = {
    "one": 1,
    "two": 2,
    "three": 3
}








