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



