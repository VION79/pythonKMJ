#in
import pandas as pd

## Create a Series Object from a Python List 

#in
ice_cream = ["Chocolate", "Vanilla", "Strawberry", "Rum Raisin"]

pd.Series(ice_cream)

#out
0     Chocolate
1       Vanilla
2    Strawberry
3    Rum Raisin
dtype: object

#in
lottery = [4, 8, 15, 16, 23, 42]

pd.Series(lottery)

#out
0     4
1     8
2    15
3    16
4    23
5    42
dtype: int64

#in
registrations = [True, False, False, False, True]

pd.Series(registrations)

#out
0     True
1    False
2    False
3    False
4     True
dtype: bool

## Create a Series Object from a Dictionary

#in
sushi = {
    "Salmon": "Orange",
    "Tuna": "Red",
    "Eel": "Brown"
}

pd.Series(sushi)

#out
Salmon    Orange
Tuna         Red
Eel        Brown
dtype: object

## TEst ##

# Import the pandas library and assign it its "pd" alias
import pandas as pd

# Create a list with 4 countries - United States, France, Germany, Italy
# Create a new Series by passing in the list of countries
# Assign the Series to a "countries" variable
countries = pd.Series(["United States", "France", "Germany", "Italy"])

# Create a list with 3 colors - red, green, blue
# Create a new Series by passing in the list of colors
# Assign the Series to a "colors" variable
colors = pd.Series(["red", "green", "blue"])

# Given the "recipe" dictionary below,
# create a new Series by passing in the dictionary as the data source
# Assign the resulting Series to a "series_dict" variable
recipe = {
  "Flour": True,
  "Sugar": True,
  "Salt": False
}
series_dict = pd.Series(recipe)

## Intro to Methods

#in
"hello".upper()

#out
'HELLO'

#in
values = [1, 2, 3]
values.append(4)
values

#out
[1, 2, 3, 4]

#in
prices = pd.Series([2.99, 4.45, 1.36])
prices

#out
0    2.99
1    4.45
2    1.36
dtype: float64

#in
prices.sum()

#out
8.8

#in
prices.product()

#out
18.095480000000006

#in
prices.mean()

#out
2.9333333333333336

## Intro to Attributes

#in
adjectives = pd.Series(["Smart", "Handsome", "Charming", "Brilliant", "Humble"])
adjectives

#out
0        Smart
1     Handsome
2     Charming
3    Brilliant
4       Humble
dtype: object

#in
adjective.size

#out
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[14], line 1
----> 1 adjective.size

NameError: name 'adjective' is not defined

#in
adjectives.size

#out
5

#in
adjectives.is_unique #This checks for any duplicates

#out
True

#in
adjectives.values

#out
array(['Smart', 'Handsome', 'Charming', 'Brilliant', 'Humble'],
      dtype=object)

#in
type(adjectives.values)

#out
numpy.ndarray

#in
adjectives.index

#out
RangeIndex(start=0, stop=5, step=1)

#in
type(adjectives.index)

#out
pandas.core.indexes.range.RangeIndex

#in
adjectives.dtype

#out
dtype('O')

##### Test #####
import pandas as pd

# The Series below stores the number of home runs
# that a baseball player hit per game
home_runs = pd.Series([3, 4, 8, 2])

# Find the total number of home runs (i.e. the sum) and assign it
# to the total_home_runs variable below
total_home_runs = home_runs.sum()

# Find the average number of home runs and assign it
# to the average_home_runs variable below
average_home_runs = home_runs.mean()






