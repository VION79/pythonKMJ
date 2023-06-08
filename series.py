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

## Parameter and Arguments

# Parameter - The name we give to an expected input
# Argument - The concrete value that we provide to a parameter

# Difficulty - Easy, Medium, Hard
# Volume - 1 through 10
# Subtitles - True, False

#in
fruits = ["Apple", "Orange", "Plum", "Grape", "Blueberry"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Monday"]
pd.Series(fruits)
#out
0        Apple
1       Orange
2         Plum
3        Grape
4    Blueberry
dtype: object

#in
pd.Series(weekdays)
#out
0       Monday
1      Tuesday
2    Wednesday
3     Thursday
4       Friday
dtype: object

#in
pd.Series(fruits, weekdays)
#out
Monday           Apple
Tuesday         Orange
Wednesday         Plum
Thursday         Grape
Friday       Blueberry
dtype: object

#in
pd.Series(weekdays, fruits)
#out
Apple           Monday
Orange         Tuesday
Plum         Wednesday
Grape         Thursday
Blueberry       Friday
dtype: object

#in
pd.Series(data = fruits, index = weekdays) # This approach of coding is more reader friendly
#out
Monday           Apple
Tuesday         Orange
Wednesday         Plum
Thursday         Grape
Friday       Blueberry
dtype: object

#in
pd.Series(fruits, index = weekdays)
#out
Monday           Apple
Tuesday         Orange
Wednesday         Plum
Thursday         Grape
Friday       Blueberry
dtype: object

## Test ##
# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

# The code below defines a list of delicious foods
# and some dipping sauces to dip them in
import pandas as pd

foods = ["French Fries", "Chicken Nuggets", "Celery", "Carrots"]
dipping_sauces = ["BBQ", "Honey Mustard", "Ranch", "Sriracha"]

# Create a Series and assign it to the s1 variable below. 
# Assign the foods list as the data source
# and the dipping_sauces list as the Series index 
# For this solution, use positional arguments (i.e. feed in the arguments sequentially)
s1 = pd.Series(foods, dipping_sauces)


# Create a Series and assign it to the s2 variable below. 
# Assign the dipping_sauces list as the data source
# and the foods list as the Series index 
# For this solution, use keyword arguments (i.e. provide the parameter names
# alongside the arguments)
s2 = pd.Series(data = dipping_sauces, index = foods)

#################################################
## Import Series with the pd.read_csv Function ##

#in
pd.read_csv()
#out
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[33], line 1
----> 1 pd.read_csv()

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\util\_decorators.py:211, in deprecate_kwarg.<locals>._deprecate_kwarg.<locals>.wrapper(*args, **kwargs)
    209     else:
    210         kwargs[new_arg_name] = new_arg_value
--> 211 return func(*args, **kwargs)

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\util\_decorators.py:331, in deprecate_nonkeyword_arguments.<locals>.decorate.<locals>.wrapper(*args, **kwargs)
    325 if len(args) > num_allow_args:
    326     warnings.warn(
    327         msg.format(arguments=_format_argument_list(allow_args)),
    328         FutureWarning,
    329         stacklevel=find_stack_level(),
    330     )
--> 331 return func(*args, **kwargs)

TypeError: read_csv() missing 1 required positional argument: 'filepath_or_buffer'

#in
pd.read_csv("pokemon.csv")
#out
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[1], line 1
----> 1 pd.read_csv("pokemon.csv")

NameError: name 'pd' is not defined

#in
import pandas as pd
pd.read_csv("pokemon.csv")
#out
Pokemon	Type
0	Bulbasaur	Grass
1	Ivysaur	Grass
2	Venusaur	Grass
3	Charmander	Fire
4	Charmeleon	Fire
...	...	...
716	Yveltal	Dark
717	Zygarde	Dragon
718	Diancie	Rock
719	Hoopa	Psychic
720	Volcanion	Fire

721 rows × 2 columns

#in
pd.read_csv("pokemon.csv", usecols = ["Pokemon"])
#out
Pokemon
0	Bulbasaur
1	Ivysaur
2	Venusaur
3	Charmander
4	Charmeleon
...	...
716	Yveltal
717	Zygarde
718	Diancie
719	Hoopa
720	Volcanion

721 rows × 1 columns

#in
pd.read_csv("pokemon.csv", usecols = ["Pokemon"]).squeeze()
#out
0       Bulbasaur
1         Ivysaur
2        Venusaur
3      Charmander
4      Charmeleon
          ...    
716       Yveltal
717       Zygarde
718       Diancie
719         Hoopa
720     Volcanion
Name: Pokemon, Length: 721, dtype: object

#in
pd.read_csv("pokemon.csv", usecols = ["Pokemon"]).squeeze("colums")
#out
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\generic.py:554, in NDFrame._get_axis_number(cls, axis)
    553 try:
--> 554     return cls._AXIS_TO_AXIS_NUMBER[axis]
    555 except KeyError:

KeyError: 'colums'

During handling of the above exception, another exception occurred:

ValueError                                Traceback (most recent call last)
Cell In[6], line 1
----> 1 pd.read_csv("pokemon.csv", usecols = ["Pokemon"]).squeeze("colums")

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\generic.py:1032, in NDFrame.squeeze(self, axis)
    928 @final
    929 def squeeze(self, axis=None):
    930     """
    931     Squeeze 1 dimensional axis objects into scalars.
    932 
   (...)
   1030     1
   1031     """
-> 1032     axis = range(self._AXIS_LEN) if axis is None else (self._get_axis_number(axis),)
   1033     return self.iloc[
   1034         tuple(
   1035             0 if i in axis and len(a) == 1 else slice(None)
   1036             for i, a in enumerate(self.axes)
   1037         )
   1038     ]

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\generic.py:556, in NDFrame._get_axis_number(cls, axis)
    554     return cls._AXIS_TO_AXIS_NUMBER[axis]
    555 except KeyError:
--> 556     raise ValueError(f"No axis named {axis} for object type {cls.__name__}")

ValueError: No axis named colums for object type DataFrame

#in
pd.read_csv("pokemon.csv", usecols = ["Pokemon"]).squeeze("columns")
#out
0       Bulbasaur
1         Ivysaur
2        Venusaur
3      Charmander
4      Charmeleon
          ...    
716       Yveltal
717       Zygarde
718       Diancie
719         Hoopa
720     Volcanion
Name: Pokemon, Length: 721, dtype: object

#in
pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"]).squeeze("columns")
pokemon
#out
0       Bulbasaur
1         Ivysaur
2        Venusaur
3      Charmander
4      Charmeleon
          ...    
716       Yveltal
717       Zygarde
718       Diancie
719         Hoopa
720     Volcanion
Name: Pokemon, Length: 721, dtype: object

#in
pd.read_csv("google_stock_price.csv")
#out
Stock Price
0	50.12
1	54.10
2	54.65
3	52.38
4	52.95
...	...
3007	772.88
3008	771.07
3009	773.18
3010	771.61
3011	782.22
3012 rows × 1 columns

#in
google = pd.read_csv("google_stock_price.csv", usecols = ["Stock Price"]), squeeze()
google
#out
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[11], line 1
----> 1 google = pd.read_csv("google_stock_price.csv", usecols = ["Stock Price"]), squeeze()
      2 google

NameError: name 'squeeze' is not defined

#in
google = pd.read_csv("google_stock_price.csv", usecols = ["Stock Price"]).squeeze()
google
#out
0        50.12
1        54.10
2        54.65
3        52.38
4        52.95
         ...  
3007    772.88
3008    771.07
3009    773.18
3010    771.61
3011    782.22
Name: Stock Price, Length: 3012, dtype: float64

## EXERCISE ##

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

import pandas as pd

# We have a foods.csv CSV file with 3 columns: Item Number, Menu Item, Price
# You can explore the data by clicking into the foods.csv file on the left
# Import the CSV file into a pandas Series object
# The Series should have the standard pandas numeric index
# The Series values should be the string values from the "Menu Item" column
# Assign the Series object to a "foods" variable
foods = pd.read_csv("foods.csv", usecols = ["Menu Item"]).squeeze("columns")



## The head and tail Methods on a Series ##
#################################################

#in
import pandas as pd
pd.read_csv("pokemon.csv")
#out
Pokemon	Type
0	Bulbasaur	Grass
1	Ivysaur	Grass
2	Venusaur	Grass
3	Charmander	Fire
4	Charmeleon	Fire
...	...	...
716	Yveltal	Dark
717	Zygarde	Dragon
718	Diancie	Rock
719	Hoopa	Psychic
720	Volcanion	Fire
721 rows × 2 columns

#in
pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"]).squeeze("columns")
google = pd.read_csv("google_stock_price.csv", usecols = ["Stock Price"]).squeeze()
pokemon.head()
pokemon.head(5)
pokemon.head(n = 5)
#out
0     Bulbasaur
1       Ivysaur
2      Venusaur
3    Charmander
4    Charmeleon
Name: Pokemon, dtype: object

#in
pokemon.head(10)
#out
0     Bulbasaur
1       Ivysaur
2      Venusaur
3    Charmander
4    Charmeleon
5     Charizard
6      Squirtle
7     Wartortle
8     Blastoise
9      Caterpie
Name: Pokemon, dtype: object

#in
google.tail(5)
#out
3011    782.22
Name: Stock Price, dtype: float64

## EXERCISE ##

# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

import pandas as pd

# We have a roller_coasters.csv CSV file with 4 columns: Name, Park, Country, and Height.
# You can explore the data by clicking into the CSV file on the left
# Import the CSV file into a pandas Series object
# The Series should have the standard pandas numeric index
# The Series values should be the string values from the "Name" column
# Assign the Series object to a "coasters" variable
coasters = pd.read_csv("roller_coasters.csv", usecols = ["Name"]).squeeze()

# I only want to ride the top 3 roller coasters on the list.
# Starting with the "coasters" Series, extract the first 3 rows in a new Series.
# Assign the new Series to a "top_three" variable.
top_three = coasters.head(3)

# I'm now curious about some of the last entries on the coaster list.
# Starting with the "coasters" Series, extract the last 4 rows in a new Series.
# Assign the new Series to a "bottom_four" variable.
bottom_four = coasters.tail(4)


#################################################

#################################################



