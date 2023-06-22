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

## Passing Series to Python's Built-In Functions ##
#################################################

#in
pokemon.head()
#out
0     Bulbasaur
1       Ivysaur
2      Venusaur
3    Charmander
4    Charmeleon
Name: Pokemon, dtype: object

#in
len(pokemon)
#out
721

#in
type("hello")
#out
str

#in
type(pokemon)
#out
pandas.core.series.Series

#in
dir(pokemon)
#out
['T',
 '_AXIS_LEN',
 '_AXIS_ORDERS',
 '_AXIS_TO_AXIS_NUMBER',
 '_HANDLED_TYPES',
 '__abs__',
 '__add__',
 '__and__',
 '__annotations__',
 '__array__',
 '__array_priority__',
 '__array_ufunc__',
 '__array_wrap__',
 '__bool__',
 '__class__',
 '__contains__',
 '__copy__',
 '__deepcopy__',
 '__delattr__',
 '__delitem__',
 '__dict__',
 '__dir__',
 '__divmod__',
 '__doc__',
 '__eq__',
 '__finalize__',
 '__float__',
 '__floordiv__',
 '__format__',
 '__ge__',
 '__getattr__',
 '__getattribute__',
 '__getitem__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__iand__',
 '__ifloordiv__',
 '__imod__',
 '__imul__',
 '__init__',
 '__init_subclass__',
 '__int__',
 '__invert__',
 '__ior__',
 '__ipow__',
 '__isub__',
 '__iter__',
 '__itruediv__',
 '__ixor__',
 '__le__',
 '__len__',
 '__long__',
 '__lt__',
 '__matmul__',
 '__mod__',
 '__module__',
 '__mul__',
 '__ne__',
 '__neg__',
 '__new__',
 '__nonzero__',
 '__or__',
 '__pos__',
 '__pow__',
 '__radd__',
 '__rand__',
 '__rdivmod__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rfloordiv__',
 '__rmatmul__',
 '__rmod__',
 '__rmul__',
 '__ror__',
 '__round__',
 '__rpow__',
 '__rsub__',
 '__rtruediv__',
 '__rxor__',
 '__setattr__',
 '__setitem__',
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 '__truediv__',
 '__weakref__',
 '__xor__',
 '_accessors',
 '_accum_func',
 '_add_numeric_operations',
 '_agg_by_level',
 '_agg_examples_doc',
 '_agg_see_also_doc',
 '_align_frame',
 '_align_series',
 '_append',
 '_arith_method',
 '_as_manager',
 '_attrs',
 '_binop',
 '_cacher',
 '_can_hold_na',
 '_check_inplace_and_allows_duplicate_labels',
 '_check_inplace_setting',
 '_check_is_chained_assignment_possible',
 '_check_label_or_level_ambiguity',
 '_check_setitem_copy',
 '_clear_item_cache',
 '_clip_with_one_bound',
 '_clip_with_scalar',
 '_cmp_method',
 '_consolidate',
 '_consolidate_inplace',
 '_construct_axes_dict',
 '_construct_axes_from_arguments',
 '_construct_result',
 '_constructor',
 '_constructor_expanddim',
 '_convert',
 '_convert_dtypes',
 '_data',
 '_dir_additions',
 '_dir_deletions',
 '_drop_axis',
 '_drop_labels_or_levels',
 '_duplicated',
 '_find_valid_index',
 '_flags',
 '_get_axis',
 '_get_axis_name',
 '_get_axis_number',
 '_get_axis_resolvers',
 '_get_block_manager_axis',
 '_get_bool_data',
 '_get_cacher',
 '_get_cleaned_column_resolvers',
 '_get_index_resolvers',
 '_get_label_or_level_values',
 '_get_numeric_data',
 '_get_value',
 '_get_values',
 '_get_values_tuple',
 '_get_with',
 '_gotitem',
 '_hidden_attrs',
 '_indexed_same',
 '_info_axis',
 '_info_axis_name',
 '_info_axis_number',
 '_init_dict',
 '_init_mgr',
 '_inplace_method',
 '_internal_names',
 '_internal_names_set',
 '_is_cached',
 '_is_copy',
 '_is_label_or_level_reference',
 '_is_label_reference',
 '_is_level_reference',
 '_is_mixed_type',
 '_is_view',
 '_item_cache',
 '_ixs',
 '_logical_func',
 '_logical_method',
 '_map_values',
 '_maybe_update_cacher',
 '_memory_usage',
 '_metadata',
 '_mgr',
 '_min_count_stat_function',
 '_name',
 '_needs_reindex_multi',
 '_protect_consolidate',
 '_reduce',
 '_reindex_axes',
 '_reindex_indexer',
 '_reindex_multi',
 '_reindex_with_indexers',
 '_rename',
 '_replace_single',
 '_repr_data_resource_',
 '_repr_latex_',
 '_reset_cache',
 '_reset_cacher',
 '_set_as_cached',
 '_set_axis',
 '_set_axis_name',
 '_set_axis_nocheck',
 '_set_is_copy',
 '_set_labels',
 '_set_name',
 '_set_value',
 '_set_values',
 '_set_with',
 '_set_with_engine',
 '_slice',
 '_stat_axis',
 '_stat_axis_name',
 '_stat_axis_number',
 '_stat_function',
 '_stat_function_ddof',
 '_take',
 '_take_with_is_copy',
 '_typ',
 '_update_inplace',
 '_validate_dtype',
 '_values',
 '_where',
 'abs',
 'add',
 'add_prefix',
 'add_suffix',
 'agg',
 'aggregate',
 'align',
 'all',
 'any',
 'append',
 'apply',
 'argmax',
 'argmin',
 'argsort',
 'array',
 'asfreq',
 'asof',
 'astype',
 'at',
 'at_time',
 'attrs',
 'autocorr',
 'axes',
 'backfill',
 'between',
 'between_time',
 'bfill',
 'bool',
 'clip',
 'combine',
 'combine_first',
 'compare',
 'convert_dtypes',
 'copy',
 'corr',
 'count',
 'cov',
 'cummax',
 'cummin',
 'cumprod',
 'cumsum',
 'describe',
 'diff',
 'div',
 'divide',
 'divmod',
 'dot',
 'drop',
 'drop_duplicates',
 'droplevel',
 'dropna',
 'dtype',
 'dtypes',
 'duplicated',
 'empty',
 'eq',
 'equals',
 'ewm',
 'expanding',
 'explode',
 'factorize',
 'ffill',
 'fillna',
 'filter',
 'first',
 'first_valid_index',
 'flags',
 'floordiv',
 'ge',
 'get',
 'groupby',
 'gt',
 'hasnans',
 'head',
 'hist',
 'iat',
 'idxmax',
 'idxmin',
 'iloc',
 'index',
 'infer_objects',
 'info',
 'interpolate',
 'is_monotonic',
 'is_monotonic_decreasing',
 'is_monotonic_increasing',
 'is_unique',
 'isin',
 'isna',
 'isnull',
 'item',
 'items',
 'iteritems',
 'keys',
 'kurt',
 'kurtosis',
 'last',
 'last_valid_index',
 'le',
 'loc',
 'lt',
 'mad',
 'map',
 'mask',
 'max',
 'mean',
 'median',
 'memory_usage',
 'min',
 'mod',
 'mode',
 'mul',
 'multiply',
 'name',
 'nbytes',
 'ndim',
 'ne',
 'nlargest',
 'notna',
 'notnull',
 'nsmallest',
 'nunique',
 'pad',
 'pct_change',
 'pipe',
 'plot',
 'pop',
 'pow',
 'prod',
 'product',
 'quantile',
 'radd',
 'rank',
 'ravel',
 'rdiv',
 'rdivmod',
 'reindex',
 'reindex_like',
 'rename',
 'rename_axis',
 'reorder_levels',
 'repeat',
 'replace',
 'resample',
 'reset_index',
 'rfloordiv',
 'rmod',
 'rmul',
 'rolling',
 'round',
 'rpow',
 'rsub',
 'rtruediv',
 'sample',
 'searchsorted',
 'sem',
 'set_axis',
 'set_flags',
 'shape',
 'shift',
 'size',
 'skew',
 'slice_shift',
 'sort_index',
 'sort_values',
 'squeeze',
 'std',
 'str',
 'sub',
 'subtract',
 'sum',
 'swapaxes',
 'swaplevel',
 'tail',
 'take',
 'to_clipboard',
 'to_csv',
 'to_dict',
 'to_excel',
 'to_frame',
 'to_hdf',
 'to_json',
 'to_latex',
 'to_list',
 'to_markdown',
 'to_numpy',
 'to_period',
 'to_pickle',
 'to_sql',
 'to_string',
 'to_timestamp',
 'to_xarray',
 'transform',
 'transpose',
 'truediv',
 'truncate',
 'tz_convert',
 'tz_localize',
 'unique',
 'unstack',
 'update',
 'value_counts',
 'values',
 'var',
 'view',
 'where',
 'xs']

#in
sorted(pokemon)
#out
['Abomasnow',
 'Abra',
 'Absol',
 'Accelgor',
 'Aegislash',
 'Aerodactyl',
 'Aggron',
 'Aipom',
 'Alakazam',
 'Alomomola',
 'Altaria',
 'Amaura',
 'Ambipom',
 'Amoonguss',
 'Ampharos',
 'Anorith',
 'Arbok',
 'Arcanine',
 'Arceus',
 'Archen',
 'Archeops',
 'Ariados',
 'Armaldo',
 'Aromatisse',
 'Aron',
 'Articuno',
 'Audino',
 'Aurorus',
 'Avalugg',
 'Axew',
 'Azelf',
 'Azumarill',
 'Azurill',
 'Bagon',
 'Baltoy',
 'Banette',
 'Barbaracle',
 'Barboach',
 'Basculin',
 'Bastiodon',
 'Bayleef',
 'Beartic',
 'Beautifly',
 'Beedrill',
 'Beheeyem',
 'Beldum',
 'Bellossom',
 'Bellsprout',
 'Bergmite',
 'Bibarel',
 'Bidoof',
 'Binacle',
 'Bisharp',
 'Blastoise',
 'Blaziken',
 'Blissey',
 'Blitzle',
 'Boldore',
 'Bonsly',
 'Bouffalant',
 'Braixen',
 'Braviary',
 'Breloom',
 'Bronzong',
 'Bronzor',
 'Budew',
 'Buizel',
 'Bulbasaur',
 'Buneary',
 'Bunnelby',
 'Burmy',
 'Butterfree',
 'Cacnea',
 'Cacturne',
 'Camerupt',
 'Carbink',
 'Carnivine',
 'Carracosta',
 'Carvanha',
 'Cascoon',
 'Castform',
 'Caterpie',
 'Celebi',
 'Chandelure',
 'Chansey',
 'Charizard',
 'Charmander',
 'Charmeleon',
 'Chatot',
 'Cherrim',
 'Cherubi',
 'Chesnaught',
 'Chespin',
 'Chikorita',
 'Chimchar',
 'Chimecho',
 'Chinchou',
 'Chingling',
 'Cinccino',
 'Clamperl',
 'Clauncher',
 'Clawitzer',
 'Claydol',
 'Clefable',
 'Clefairy',
 'Cleffa',
 'Cloyster',
 'Cobalion',
 'Cofagrigus',
 'Combee',
 'Combusken',
 'Conkeldurr',
 'Corphish',
 'Corsola',
 'Cottonee',
 'Cradily',
 'Cranidos',
 'Crawdaunt',
 'Cresselia',
 'Croagunk',
 'Crobat',
 'Croconaw',
 'Crustle',
 'Cryogonal',
 'Cubchoo',
 'Cubone',
 'Cyndaquil',
 'Darkrai',
 'Darmanitan',
 'Darumaka',
 'Dedenne',
 'Deerling',
 'Deino',
 'Delcatty',
 'Delibird',
 'Delphox',
 'Deoxys',
 'Dewgong',
 'Dewott',
 'Dialga',
 'Diancie',
 'Diggersby',
 'Diglett',
 'Ditto',
 'Dodrio',
 'Doduo',
 'Donphan',
 'Doublade',
 'Dragalge',
 'Dragonair',
 'Dragonite',
 'Drapion',
 'Dratini',
 'Drifblim',
 'Drifloon',
 'Drilbur',
 'Drowzee',
 'Druddigon',
 'Ducklett',
 'Dugtrio',
 'Dunsparce',
 'Duosion',
 'Durant',
 'Dusclops',
 'Dusknoir',
 'Duskull',
 'Dustox',
 'Dwebble',
 'Eelektrik',
 'Eelektross',
 'Eevee',
 'Ekans',
 'Electabuzz',
 'Electivire',
 'Electrike',
 'Electrode',
 'Elekid',
 'Elgyem',
 'Emboar',
 'Emolga',
 'Empoleon',
 'Entei',
 'Escavalier',
 'Espeon',
 'Espurr',
 'Excadrill',
 'Exeggcute',
 'Exeggutor',
 'Exploud',
 "Farfetch'd",
 'Fearow',
 'Feebas',
 'Fennekin',
 'Feraligatr',
 'Ferroseed',
 'Ferrothorn',
 'Finneon',
 'Flaaffy',
 'Flabébé',
 'Flareon',
 'Fletchinder',
 'Fletchling',
 'Floatzel',
 'Floette',
 'Florges',
 'Flygon',
 'Foongus',
 'Forretress',
 'Fraxure',
 'Frillish',
 'Froakie',
 'Frogadier',
 'Froslass',
 'Furfrou',
 'Furret',
 'Gabite',
 'Gallade',
 'Galvantula',
 'Garbodor',
 'Garchomp',
 'Gardevoir',
 'Gastly',
 'Gastrodon',
 'Genesect',
 'Gengar',
 'Geodude',
 'Gible',
 'Gigalith',
 'Girafarig',
 'Giratina',
 'Glaceon',
 'Glalie',
 'Glameow',
 'Gligar',
 'Gliscor',
 'Gloom',
 'Gogoat',
 'Golbat',
 'Goldeen',
 'Golduck',
 'Golem',
 'Golett',
 'Golurk',
 'Goodra',
 'Goomy',
 'Gorebyss',
 'Gothita',
 'Gothitelle',
 'Gothorita',
 'Gourgeist',
 'Granbull',
 'Graveler',
 'Greninja',
 'Grimer',
 'Grotle',
 'Groudon',
 'Grovyle',
 'Growlithe',
 'Grumpig',
 'Gulpin',
 'Gurdurr',
 'Gyarados',
 'Happiny',
 'Hariyama',
 'Haunter',
 'Hawlucha',
 'Haxorus',
 'Heatmor',
 'Heatran',
 'Heliolisk',
 'Helioptile',
 'Heracross',
 'Herdier',
 'Hippopotas',
 'Hippowdon',
 'Hitmonchan',
 'Hitmonlee',
 'Hitmontop',
 'Ho-oh',
 'Honchkrow',
 'Honedge',
 'Hoopa',
 'Hoothoot',
 'Hoppip',
 'Horsea',
 'Houndoom',
 'Houndour',
 'Huntail',
 'Hydreigon',
 'Hypno',
 'Igglybuff',
 'Illumise',
 'Infernape',
 'Inkay',
 'Ivysaur',
 'Jellicent',
 'Jigglypuff',
 'Jirachi',
 'Jolteon',
 'Joltik',
 'Jumpluff',
 'Jynx',
 'Kabuto',
 'Kabutops',
 'Kadabra',
 'Kakuna',
 'Kangaskhan',
 'Karrablast',
 'Kecleon',
 'Keldeo',
 'Kingdra',
 'Kingler',
 'Kirlia',
 'Klang',
 'Klefki',
 'Klink',
 'Klinklang',
 'Koffing',
 'Krabby',
 'Kricketot',
 'Kricketune',
 'Krokorok',
 'Krookodile',
 'Kyogre',
 'Kyurem',
 'Lairon',
 'Lampent',
 'Landorus',
 'Lanturn',
 'Lapras',
 'Larvesta',
 'Larvitar',
 'Latias',
 'Latios',
 'Leafeon',
 'Leavanny',
 'Ledian',
 'Ledyba',
 'Lickilicky',
 'Lickitung',
 'Liepard',
 'Lileep',
 'Lilligant',
 'Lillipup',
 'Linoone',
 'Litleo',
 'Litwick',
 'Lombre',
 'Lopunny',
 'Lotad',
 'Loudred',
 'Lucario',
 'Ludicolo',
 'Lugia',
 'Lumineon',
 'Lunatone',
 'Luvdisc',
 'Luxio',
 'Luxray',
 'Machamp',
 'Machoke',
 'Machop',
 'Magby',
 'Magcargo',
 'Magikarp',
 'Magmar',
 'Magmortar',
 'Magnemite',
 'Magneton',
 'Magnezone',
 'Makuhita',
 'Malamar',
 'Mamoswine',
 'Manaphy',
 'Mandibuzz',
 'Manectric',
 'Mankey',
 'Mantine',
 'Mantyke',
 'Maractus',
 'Mareep',
 'Marill',
 'Marowak',
 'Marshtomp',
 'Masquerain',
 'Mawile',
 'Medicham',
 'Meditite',
 'Meganium',
 'Meloetta',
 'Meowstic',
 'Meowth',
 'Mesprit',
 'Metagross',
 'Metang',
 'Metapod',
 'Mew',
 'Mewtwo',
 'Mienfoo',
 'Mienshao',
 'Mightyena',
 'Milotic',
 'Miltank',
 'Mime Jr.',
 'Minccino',
 'Minun',
 'Misdreavus',
 'Mismagius',
 'Moltres',
 'Monferno',
 'Mothim',
 'Mr. Mime',
 'Mudkip',
 'Muk',
 'Munchlax',
 'Munna',
 'Murkrow',
 'Musharna',
 'Natu',
 'Nidoking',
 'Nidoqueen',
 'Nidoran',
 'Nidoran♂',
 'Nidorina',
 'Nidorino',
 'Nincada',
 'Ninetales',
 'Ninjask',
 'Noctowl',
 'Noibat',
 'Noivern',
 'Nosepass',
 'Numel',
 'Nuzleaf',
 'Octillery',
 'Oddish',
 'Omanyte',
 'Omastar',
 'Onix',
 'Oshawott',
 'Pachirisu',
 'Palkia',
 'Palpitoad',
 'Pancham',
 'Pangoro',
 'Panpour',
 'Pansage',
 'Pansear',
 'Paras',
 'Parasect',
 'Patrat',
 'Pawniard',
 'Pelipper',
 'Persian',
 'Petilil',
 'Phanpy',
 'Phantump',
 'Phione',
 'Pichu',
 'Pidgeot',
 'Pidgeotto',
 'Pidgey',
 'Pidove',
 'Pignite',
 'Pikachu',
 'Piloswine',
 'Pineco',
 'Pinsir',
 'Piplup',
 'Plusle',
 'Politoed',
 'Poliwag',
 'Poliwhirl',
 'Poliwrath',
 'Ponyta',
 'Poochyena',
 'Porygon',
 'Porygon-Z',
 'Porygon2',
 'Primeape',
 'Prinplup',
 'Probopass',
 'Psyduck',
 'Pumpkaboo',
 'Pupitar',
 'Purrloin',
 'Purugly',
 'Pyroar',
 'Quagsire',
 'Quilava',
 'Quilladin',
 'Qwilfish',
 'Raichu',
 'Raikou',
 'Ralts',
 'Rampardos',
 'Rapidash',
 'Raticate',
 'Rattata',
 'Rayquaza',
 'Regice',
 'Regigigas',
 'Regirock',
 'Registeel',
 'Relicanth',
 'Remoraid',
 'Reshiram',
 'Reuniclus',
 'Rhydon',
 'Rhyhorn',
 'Rhyperior',
 'Riolu',
 'Roggenrola',
 'Roselia',
 'Roserade',
 'Rotom',
 'Rufflet',
 'Sableye',
 'Salamence',
 'Samurott',
 'Sandile',
 'Sandshrew',
 'Sandslash',
 'Sawk',
 'Sawsbuck',
 'Scatterbug',
 'Sceptile',
 'Scizor',
 'Scolipede',
 'Scrafty',
 'Scraggy',
 'Scyther',
 'Seadra',
 'Seaking',
 'Sealeo',
 'Seedot',
 'Seel',
 'Seismitoad',
 'Sentret',
 'Serperior',
 'Servine',
 'Seviper',
 'Sewaddle',
 'Sharpedo',
 'Shaymin',
 'Shedinja',
 'Shelgon',
 'Shellder',
 'Shellos',
 'Shelmet',
 'Shieldon',
 'Shiftry',
 'Shinx',
 'Shroomish',
 'Shuckle',
 'Shuppet',
 'Sigilyph',
 'Silcoon',
 'Simipour',
 'Simisage',
 'Simisear',
 'Skarmory',
 'Skiddo',
 'Skiploom',
 'Skitty',
 'Skorupi',
 'Skrelp',
 'Skuntank',
 'Slaking',
 'Slakoth',
 'Sliggoo',
 'Slowbro',
 'Slowking',
 'Slowpoke',
 'Slugma',
 'Slurpuff',
 'Smeargle',
 'Smoochum',
 'Sneasel',
 'Snivy',
 'Snorlax',
 'Snorunt',
 'Snover',
 'Snubbull',
 'Solosis',
 'Solrock',
 'Spearow',
 'Spewpa',
 'Spheal',
 'Spinarak',
 'Spinda',
 'Spiritomb',
 'Spoink',
 'Spritzee',
 'Squirtle',
 'Stantler',
 'Staraptor',
 'Staravia',
 'Starly',
 'Starmie',
 'Staryu',
 'Steelix',
 'Stoutland',
 'Stunfisk',
 'Stunky',
 'Sudowoodo',
 'Suicune',
 'Sunflora',
 'Sunkern',
 'Surskit',
 'Swablu',
 'Swadloon',
 'Swalot',
 'Swampert',
 'Swanna',
 'Swellow',
 'Swinub',
 'Swirlix',
 'Swoobat',
 'Sylveon',
 'Taillow',
 'Talonflame',
 'Tangela',
 'Tangrowth',
 'Tauros',
 'Teddiursa',
 'Tentacool',
 'Tentacruel',
 'Tepig',
 'Terrakion',
 'Throh',
 'Thundurus',
 'Timburr',
 'Tirtouga',
 'Togekiss',
 'Togepi',
 'Togetic',
 'Torchic',
 'Torkoal',
 'Tornadus',
 'Torterra',
 'Totodile',
 'Toxicroak',
 'Tranquill',
 'Trapinch',
 'Treecko',
 'Trevenant',
 'Tropius',
 'Trubbish',
 'Turtwig',
 'Tympole',
 'Tynamo',
 'Typhlosion',
 'Tyranitar',
 'Tyrantrum',
 'Tyrogue',
 'Tyrunt',
 'Umbreon',
 'Unfezant',
 'Unown',
 'Ursaring',
 'Uxie',
 'Vanillish',
 'Vanillite',
 'Vanilluxe',
 'Vaporeon',
 'Venipede',
 'Venomoth',
 'Venonat',
 'Venusaur',
 'Vespiquen',
 'Vibrava',
 'Victini',
 'Victreebel',
 'Vigoroth',
 'Vileplume',
 'Virizion',
 'Vivillon',
 'Volbeat',
 'Volcanion',
 'Volcarona',
 'Voltorb',
 'Vullaby',
 'Vulpix',
 'Wailmer',
 'Wailord',
 'Walrein',
 'Wartortle',
 'Watchog',
 'Weavile',
 'Weedle',
 'Weepinbell',
 'Weezing',
 'Whimsicott',
 'Whirlipede',
 'Whiscash',
 'Whismur',
 'Wigglytuff',
 'Wingull',
 'Wobbuffet',
 'Woobat',
 'Wooper',
 'Wormadam',
 'Wurmple',
 'Wynaut',
 'Xatu',
 'Xerneas',
 'Yamask',
 'Yanma',
 'Yanmega',
 'Yveltal',
 'Zangoose',
 'Zapdos',
 'Zebstrika',
 'Zekrom',
 'Zigzagoon',
 'Zoroark',
 'Zorua',
 'Zubat',
 'Zweilous',
 'Zygarde']

#in
type(sorted(pokemon))
#out
list

#in
sorted(google)
#out
[49.95,
 50.07,
 50.12,
 50.7,
 50.74,
 50.95,
 51.1,
 51.1,
 51.13,
 52.38,
 52.61,
 52.95,
 53.02,
 53.7,
 53.9,
 54.1,
 54.65,
 55.69,
 55.94,
 56.93,
 58.69,
 58.86,
 59.07,
 59.13,
 59.62,
 59.86,
 60.35,
 63.37,
 64.74,
 65.47,
 66.22,
 67.46,
 67.56,
 68.47,
 68.63,
 68.8,
 69.12,
 69.36,
 70.17,
 70.38,
 70.93,
 71.98,
 73.9,
 74.51,
 74.62,
 82.47,
 83.68,
 83.69,
 83.85,
 84.27,
 84.59,
 84.62,
 84.91,
 85.14,
 85.63,
 85.74,
 86.13,
 86.16,
 86.19,
 86.19,
 86.63,
 87.29,
 87.41,
 87.71,
 88.06,
 88.15,
 88.47,
 88.81,
 89.21,
 89.22,
 89.26,
 89.4,
 89.54,
 89.56,
 89.61,
 89.61,
 89.7,
 89.8,
 89.89,
 89.9,
 89.93,
 89.93,
 89.95,
 90.11,
 90.13,
 90.16,
 90.27,
 90.35,
 90.43,
 90.58,
 90.62,
 90.81,
 90.9,
 90.91,
 91.42,
 91.78,
 92.26,
 92.34,
 92.41,
 92.42,
 92.5,
 92.51,
 92.55,
 92.84,
 92.86,
 92.89,
 92.94,
 93.06,
 93.39,
 93.41,
 93.61,
 93.61,
 93.86,
 93.9,
 93.9,
 93.95,
 94.05,
 94.18,
 94.19,
 94.31,
 94.35,
 94.52,
 94.53,
 95.07,
 95.22,
 95.59,
 95.6,
 95.63,
 95.69,
 95.74,
 95.85,
 95.86,
 95.93,
 96.28,
 96.3,
 96.35,
 96.37,
 96.4,
 96.52,
 96.55,
 96.66,
 96.67,
 96.78,
 96.83,
 96.86,
 96.88,
 96.88,
 97.15,
 97.34,
 97.43,
 97.52,
 97.57,
 97.59,
 97.71,
 97.92,
 97.92,
 98.55,
 98.7,
 98.85,
 98.88,
 98.95,
 99.11,
 99.22,
 99.89,
 101.25,
 101.85,
 102.01,
 102.08,
 102.88,
 105.32,
 107.8,
 109.27,
 109.62,
 109.78,
 109.89,
 111.03,
 111.65,
 112.9,
 112.98,
 113.38,
 113.79,
 113.9,
 114.14,
 114.25,
 114.51,
 115.41,
 115.53,
 116.45,
 119.46,
 119.47,
 120.68,
 127.6,
 127.87,
 128.59,
 129.47,
 129.65,
 130.27,
 131.08,
 132.86,
 132.87,
 136.87,
 137.03,
 137.26,
 137.42,
 138.5,
 138.58,
 139.04,
 139.58,
 139.64,
 139.65,
 139.86,
 139.86,
 139.95,
 139.99,
 140.0,
 140.88,
 141.11,
 141.14,
 141.15,
 141.23,
 141.23,
 141.65,
 141.85,
 141.86,
 141.88,
 142.41,
 142.68,
 142.7,
 142.86,
 142.98,
 143.01,
 143.21,
 143.41,
 143.49,
 143.74,
 143.78,
 143.81,
 143.86,
 144.08,
 144.08,
 144.51,
 144.71,
 144.72,
 145.3,
 145.32,
 145.35,
 145.48,
 145.48,
 145.62,
 145.64,
 145.66,
 145.75,
 145.9,
 146.03,
 146.21,
 146.33,
 146.41,
 146.53,
 146.6,
 146.93,
 147.29,
 147.55,
 147.62,
 147.71,
 147.78,
 147.9,
 147.92,
 147.97,
 148.32,
 148.41,
 148.48,
 148.5,
 148.56,
 148.56,
 148.57,
 148.72,
 148.86,
 149.28,
 149.35,
 149.4,
 149.45,
 149.62,
 149.69,
 149.91,
 149.95,
 149.96,
 150.03,
 150.29,
 150.33,
 150.33,
 150.44,
 150.85,
 150.9,
 151.05,
 151.16,
 151.32,
 151.35,
 151.39,
 151.4,
 151.45,
 151.49,
 151.74,
 151.9,
 152.35,
 152.67,
 152.83,
 152.85,
 152.9,
 153.1,
 153.67,
 153.8,
 153.93,
 154.13,
 154.2,
 154.26,
 154.66,
 154.72,
 154.8,
 154.85,
 154.93,
 154.98,
 155.17,
 155.18,
 155.2,
 155.34,
 155.53,
 155.57,
 155.68,
 155.79,
 155.84,
 155.88,
 156.19,
 156.22,
 156.34,
 156.81,
 156.81,
 156.98,
 157.0,
 157.38,
 157.46,
 157.52,
 157.72,
 158.07,
 158.8,
 159.18,
 159.23,
 159.3,
 159.69,
 160.5,
 160.84,
 161.6,
 161.77,
 162.05,
 162.19,
 162.43,
 162.48,
 162.58,
 163.42,
 163.86,
 164.33,
 164.58,
 164.81,
 164.86,
 164.91,
 165.4,
 165.44,
 165.57,
 165.83,
 166.38,
 166.86,
 167.5,
 168.36,
 168.42,
 168.58,
 168.83,
 168.89,
 169.1,
 169.22,
 169.42,
 169.48,
 169.73,
 169.78,
 169.79,
 169.94,
 170.05,
 170.11,
 170.65,
 170.77,
 170.95,
 171.02,
 171.15,
 171.16,
 171.17,
 171.33,
 171.33,
 171.49,
 171.49,
 171.86,
 172.08,
 172.55,
 172.68,
 172.83,
 173.05,
 173.07,
 173.28,
 173.41,
 173.68,
 173.86,
 173.92,
 174.13,
 174.15,
 174.16,
 175.4,
 175.98,
 176.33,
 176.35,
 176.38,
 176.47,
 176.68,
 176.76,
 176.87,
 177.54,
 177.66,
 178.66,
 178.82,
 178.84,
 178.91,
 179.08,
 179.15,
 179.21,
 179.5,
 179.67,
 180.82,
 181.07,
 181.12,
 181.13,
 181.17,
 181.19,
 181.34,
 182.04,
 182.22,
 182.56,
 182.72,
 183.05,
 183.11,
 183.29,
 183.43,
 183.78,
 183.87,
 183.94,
 184.07,
 184.19,
 184.19,
 184.27,
 184.36,
 184.53,
 184.66,
 184.71,
 184.82,
 185.29,
 185.31,
 185.42,
 185.45,
 185.46,
 185.72,
 185.78,
 185.88,
 186.06,
 186.08,
 186.44,
 186.53,
 186.68,
 186.74,
 186.88,
 186.91,
 187.03,
 187.06,
 187.51,
 187.57,
 187.6,
 187.91,
 188.04,
 188.28,
 188.41,
 188.46,
 188.51,
 188.74,
 188.79,
 188.85,
 188.87,
 188.9,
 188.96,
 189.06,
 189.08,
 189.11,
 189.2,
 189.29,
 189.39,
 189.46,
 189.47,
 189.5,
 189.53,
 189.56,
 189.65,
 189.88,
 190.18,
 190.28,
 190.29,
 190.31,
 190.31,
 190.32,
 190.43,
 190.48,
 190.54,
 190.58,
 190.59,
 191.01,
 191.12,
 191.3,
 191.49,
 191.66,
 191.74,
 191.85,
 191.99,
 192.0,
 192.15,
 192.36,
 192.56,
 192.71,
 192.78,
 192.78,
 193.06,
 193.07,
 193.09,
 193.11,
 193.26,
 193.31,
 193.37,
 193.39,
 193.56,
 193.67,
 193.87,
 193.88,
 194.03,
 194.18,
 194.49,
 194.55,
 194.58,
 194.66,
 194.76,
 194.8,
 194.8,
 194.8,
 194.86,
 194.99,
 195.0,
 195.02,
 195.05,
 195.15,
 195.25,
 195.3,
 195.35,
 195.54,
 195.75,
 195.92,
 196.2,
 196.45,
 196.55,
 196.65,
 196.89,
 196.95,
 197.18,
 197.19,
 197.2,
 197.29,
 197.32,
 197.79,
 197.82,
 198.05,
 198.11,
 198.12,
 198.22,
 198.29,
 198.3,
 198.39,
 198.88,
 199.24,
 199.25,
 199.3,
 199.31,
 199.53,
 199.78,
 199.9,
 200.06,
 200.52,
 200.69,
 200.75,
 200.79,
 200.86,
 200.88,
 200.96,
 201.04,
 201.26,
 201.29,
 201.29,
 201.32,
 201.52,
 201.53,
 201.55,
 201.57,
 201.59,
 201.69,
 201.7,
 201.79,
 201.79,
 201.82,
 201.91,
 201.91,
 201.92,
 201.97,
 201.98,
 202.07,
 202.23,
 202.25,
 202.58,
 202.64,
 202.72,
 202.85,
 202.88,
 203.08,
 203.21,
 203.22,
 203.23,
 203.46,
 203.47,
 203.74,
 203.79,
 203.79,
 204.04,
 204.2,
 204.21,
 204.27,
 204.4,
 204.44,
 204.48,
 204.6,
 204.63,
 204.74,
 204.99,
 204.99,
 205.04,
 205.12,
 205.38,
 205.65,
 205.7,
 206.1,
 206.6,
 206.82,
 206.84,
 206.87,
 206.99,
 207.04,
 207.14,
 207.22,
 207.29,
 207.37,
 207.64,
 207.68,
 207.79,
 207.98,
 208.03,
 208.18,
 208.41,
 208.42,
 208.54,
 208.64,
 208.7,
 208.76,
 208.89,
 209.12,
 209.27,
 209.29,
 209.44,
 209.46,
 209.73,
 209.76,
 209.8,
 209.83,
 209.86,
 210.01,
 210.04,
 210.11,
 210.52,
 210.58,
 210.66,
 211.05,
 211.22,
 211.38,
 211.39,
 211.53,
 211.86,
 211.94,
 212.07,
 212.09,
 212.11,
 212.13,
 212.21,
 212.45,
 212.77,
 212.82,
 212.95,
 213.04,
 213.07,
 213.11,
 213.13,
 213.2,
 213.37,
 213.44,
 213.51,
 213.54,
 213.63,
 213.74,
 213.99,
 214.1,
 214.29,
 214.29,
 214.42,
 214.66,
 214.85,
 214.86,
 214.87,
 214.91,
 215.25,
 215.3,
 215.61,
 215.78,
 215.8,
 216.08,
 216.11,
 216.13,
 216.28,
 216.46,
 216.53,
 216.56,
 216.66,
 216.71,
 216.92,
 217.34,
 217.4,
 217.59,
 217.82,
 217.9,
 218.0,
 218.06,
 218.33,
 218.45,
 218.61,
 218.74,
 218.82,
 218.87,
 219.12,
 219.17,
 219.32,
 219.36,
 219.53,
 219.58,
 219.7,
 219.71,
 219.87,
 219.92,
 220.01,
 220.03,
 220.2,
 220.25,
 221.08,
 221.24,
 221.28,
 221.29,
 221.29,
 221.3,
 221.76,
 221.82,
 221.9,
 221.94,
 222.08,
 222.18,
 222.22,
 222.23,
 222.25,
 222.4,
 222.42,
 222.42,
 222.6,
 222.87,
 223.14,
 223.2,
 223.39,
 223.63,
 223.78,
 223.89,
 224.16,
 224.35,
 224.5,
 224.55,
 224.78,
 224.87,
 224.9,
 224.95,
 225.16,
 225.26,
 225.34,
 225.39,
 225.47,
 225.6,
 225.88,
 226.12,
 226.25,
 226.28,
 226.64,
 226.74,
 226.9,
 227.08,
 227.13,
 227.15,
 227.29,
 227.33,
 227.56,
 227.59,
 227.65,
 227.87,
 228.05,
 228.05,
 228.08,
 228.28,
 228.32,
 228.5,
 228.53,
 228.54,
 228.55,
 228.77,
 228.85,
 228.87,
 228.92,
 229.04,
 229.06,
 229.08,
 229.19,
 229.32,
 229.57,
 229.61,
 229.77,
 229.94,
 229.97,
 230.01,
 230.05,
 230.23,
 230.42,
 230.5,
 230.5,
 230.6,
 230.66,
 230.68,
 230.71,
 230.71,
 230.78,
 230.79,
 230.91,
 231.05,
 231.17,
 231.22,
 231.27,
 231.36,
 231.41,
 231.58,
 231.58,
 231.75,
 231.8,
 231.86,
 231.86,
 231.97,
 231.97,
 232.03,
 232.14,
 232.23,
 232.27,
 232.39,
 232.39,
 232.6,
 232.62,
 232.62,
 232.66,
 232.73,
 232.8,
 232.86,
 232.89,
 232.91,
 233.02,
 233.14,
 233.17,
 233.22,
 233.32,
 233.35,
 233.4,
 233.46,
 233.51,
 233.52,
 233.56,
 233.67,
 233.7,
 233.75,
 233.77,
 233.78,
 233.87,
 234.06,
 234.08,
 234.13,
 234.17,
 234.27,
 234.3,
 234.39,
 234.65,
 234.72,
 234.74,
 234.77,
 234.91,
 234.92,
 235.05,
 235.06,
 235.07,
 235.23,
 235.24,
 235.27,
 235.28,
 235.31,
 235.32,
 235.35,
 235.45,
 235.45,
 235.5,
 235.52,
 235.58,
 235.59,
 235.66,
 235.79,
 235.8,
 235.81,
 235.83,
 236.05,
 236.06,
 236.07,
 236.08,
 236.1,
 236.16,
 236.19,
 236.38,
 236.42,
 236.54,
 236.64,
 236.65,
 236.75,
 236.77,
 236.84,
 236.9,
 236.93,
 237.2,
 237.26,
 237.27,
 237.31,
 237.32,
 237.36,
 237.46,
 237.5,
 237.57,
 237.68,
 237.69,
 237.69,
 237.69,
 237.77,
 237.83,
 237.85,
 237.96,
 238.05,
 238.17,
 238.24,
 238.3,
 238.32,
 238.32,
 238.34,
 238.51,
 238.53,
 238.53,
 238.76,
 239.26,
 239.27,
 239.29,
 239.3,
 239.32,
 239.69,
 239.87,
 239.91,
 ...]

 #in
 list(pokemon)
 #out
 ['Bulbasaur',
 'Ivysaur',
 'Venusaur',
 'Charmander',
 'Charmeleon',
 'Charizard',
 'Squirtle',
 'Wartortle',
 'Blastoise',
 'Caterpie',
 'Metapod',
 'Butterfree',
 'Weedle',
 'Kakuna',
 'Beedrill',
 'Pidgey',
 'Pidgeotto',
 'Pidgeot',
 'Rattata',
 'Raticate',
 'Spearow',
 'Fearow',
 'Ekans',
 'Arbok',
 'Pikachu',
 'Raichu',
 'Sandshrew',
 'Sandslash',
 'Nidoran',
 'Nidorina',
 'Nidoqueen',
 'Nidoran♂',
 'Nidorino',
 'Nidoking',
 'Clefairy',
 'Clefable',
 'Vulpix',
 'Ninetales',
 'Jigglypuff',
 'Wigglytuff',
 'Zubat',
 'Golbat',
 'Oddish',
 'Gloom',
 'Vileplume',
 'Paras',
 'Parasect',
 'Venonat',
 'Venomoth',
 'Diglett',
 'Dugtrio',
 'Meowth',
 'Persian',
 'Psyduck',
 'Golduck',
 'Mankey',
 'Primeape',
 'Growlithe',
 'Arcanine',
 'Poliwag',
 'Poliwhirl',
 'Poliwrath',
 'Abra',
 'Kadabra',
 'Alakazam',
 'Machop',
 'Machoke',
 'Machamp',
 'Bellsprout',
 'Weepinbell',
 'Victreebel',
 'Tentacool',
 'Tentacruel',
 'Geodude',
 'Graveler',
 'Golem',
 'Ponyta',
 'Rapidash',
 'Slowpoke',
 'Slowbro',
 'Magnemite',
 'Magneton',
 "Farfetch'd",
 'Doduo',
 'Dodrio',
 'Seel',
 'Dewgong',
 'Grimer',
 'Muk',
 'Shellder',
 'Cloyster',
 'Gastly',
 'Haunter',
 'Gengar',
 'Onix',
 'Drowzee',
 'Hypno',
 'Krabby',
 'Kingler',
 'Voltorb',
 'Electrode',
 'Exeggcute',
 'Exeggutor',
 'Cubone',
 'Marowak',
 'Hitmonlee',
 'Hitmonchan',
 'Lickitung',
 'Koffing',
 'Weezing',
 'Rhyhorn',
 'Rhydon',
 'Chansey',
 'Tangela',
 'Kangaskhan',
 'Horsea',
 'Seadra',
 'Goldeen',
 'Seaking',
 'Staryu',
 'Starmie',
 'Mr. Mime',
 'Scyther',
 'Jynx',
 'Electabuzz',
 'Magmar',
 'Pinsir',
 'Tauros',
 'Magikarp',
 'Gyarados',
 'Lapras',
 'Ditto',
 'Eevee',
 'Vaporeon',
 'Jolteon',
 'Flareon',
 'Porygon',
 'Omanyte',
 'Omastar',
 'Kabuto',
 'Kabutops',
 'Aerodactyl',
 'Snorlax',
 'Articuno',
 'Zapdos',
 'Moltres',
 'Dratini',
 'Dragonair',
 'Dragonite',
 'Mewtwo',
 'Mew',
 'Chikorita',
 'Bayleef',
 'Meganium',
 'Cyndaquil',
 'Quilava',
 'Typhlosion',
 'Totodile',
 'Croconaw',
 'Feraligatr',
 'Sentret',
 'Furret',
 'Hoothoot',
 'Noctowl',
 'Ledyba',
 'Ledian',
 'Spinarak',
 'Ariados',
 'Crobat',
 'Chinchou',
 'Lanturn',
 'Pichu',
 'Cleffa',
 'Igglybuff',
 'Togepi',
 'Togetic',
 'Natu',
 'Xatu',
 'Mareep',
 'Flaaffy',
 'Ampharos',
 'Bellossom',
 'Marill',
 'Azumarill',
 'Sudowoodo',
 'Politoed',
 'Hoppip',
 'Skiploom',
 'Jumpluff',
 'Aipom',
 'Sunkern',
 'Sunflora',
 'Yanma',
 'Wooper',
 'Quagsire',
 'Espeon',
 'Umbreon',
 'Murkrow',
 'Slowking',
 'Misdreavus',
 'Unown',
 'Wobbuffet',
 'Girafarig',
 'Pineco',
 'Forretress',
 'Dunsparce',
 'Gligar',
 'Steelix',
 'Snubbull',
 'Granbull',
 'Qwilfish',
 'Scizor',
 'Shuckle',
 'Heracross',
 'Sneasel',
 'Teddiursa',
 'Ursaring',
 'Slugma',
 'Magcargo',
 'Swinub',
 'Piloswine',
 'Corsola',
 'Remoraid',
 'Octillery',
 'Delibird',
 'Mantine',
 'Skarmory',
 'Houndour',
 'Houndoom',
 'Kingdra',
 'Phanpy',
 'Donphan',
 'Porygon2',
 'Stantler',
 'Smeargle',
 'Tyrogue',
 'Hitmontop',
 'Smoochum',
 'Elekid',
 'Magby',
 'Miltank',
 'Blissey',
 'Raikou',
 'Entei',
 'Suicune',
 'Larvitar',
 'Pupitar',
 'Tyranitar',
 'Lugia',
 'Ho-oh',
 'Celebi',
 'Treecko',
 'Grovyle',
 'Sceptile',
 'Torchic',
 'Combusken',
 'Blaziken',
 'Mudkip',
 'Marshtomp',
 'Swampert',
 'Poochyena',
 'Mightyena',
 'Zigzagoon',
 'Linoone',
 'Wurmple',
 'Silcoon',
 'Beautifly',
 'Cascoon',
 'Dustox',
 'Lotad',
 'Lombre',
 'Ludicolo',
 'Seedot',
 'Nuzleaf',
 'Shiftry',
 'Taillow',
 'Swellow',
 'Wingull',
 'Pelipper',
 'Ralts',
 'Kirlia',
 'Gardevoir',
 'Surskit',
 'Masquerain',
 'Shroomish',
 'Breloom',
 'Slakoth',
 'Vigoroth',
 'Slaking',
 'Nincada',
 'Ninjask',
 'Shedinja',
 'Whismur',
 'Loudred',
 'Exploud',
 'Makuhita',
 'Hariyama',
 'Azurill',
 'Nosepass',
 'Skitty',
 'Delcatty',
 'Sableye',
 'Mawile',
 'Aron',
 'Lairon',
 'Aggron',
 'Meditite',
 'Medicham',
 'Electrike',
 'Manectric',
 'Plusle',
 'Minun',
 'Volbeat',
 'Illumise',
 'Roselia',
 'Gulpin',
 'Swalot',
 'Carvanha',
 'Sharpedo',
 'Wailmer',
 'Wailord',
 'Numel',
 'Camerupt',
 'Torkoal',
 'Spoink',
 'Grumpig',
 'Spinda',
 'Trapinch',
 'Vibrava',
 'Flygon',
 'Cacnea',
 'Cacturne',
 'Swablu',
 'Altaria',
 'Zangoose',
 'Seviper',
 'Lunatone',
 'Solrock',
 'Barboach',
 'Whiscash',
 'Corphish',
 'Crawdaunt',
 'Baltoy',
 'Claydol',
 'Lileep',
 'Cradily',
 'Anorith',
 'Armaldo',
 'Feebas',
 'Milotic',
 'Castform',
 'Kecleon',
 'Shuppet',
 'Banette',
 'Duskull',
 'Dusclops',
 'Tropius',
 'Chimecho',
 'Absol',
 'Wynaut',
 'Snorunt',
 'Glalie',
 'Spheal',
 'Sealeo',
 'Walrein',
 'Clamperl',
 'Huntail',
 'Gorebyss',
 'Relicanth',
 'Luvdisc',
 'Bagon',
 'Shelgon',
 'Salamence',
 'Beldum',
 'Metang',
 'Metagross',
 'Regirock',
 'Regice',
 'Registeel',
 'Latias',
 'Latios',
 'Kyogre',
 'Groudon',
 'Rayquaza',
 'Jirachi',
 'Deoxys',
 'Turtwig',
 'Grotle',
 'Torterra',
 'Chimchar',
 'Monferno',
 'Infernape',
 'Piplup',
 'Prinplup',
 'Empoleon',
 'Starly',
 'Staravia',
 'Staraptor',
 'Bidoof',
 'Bibarel',
 'Kricketot',
 'Kricketune',
 'Shinx',
 'Luxio',
 'Luxray',
 'Budew',
 'Roserade',
 'Cranidos',
 'Rampardos',
 'Shieldon',
 'Bastiodon',
 'Burmy',
 'Wormadam',
 'Mothim',
 'Combee',
 'Vespiquen',
 'Pachirisu',
 'Buizel',
 'Floatzel',
 'Cherubi',
 'Cherrim',
 'Shellos',
 'Gastrodon',
 'Ambipom',
 'Drifloon',
 'Drifblim',
 'Buneary',
 'Lopunny',
 'Mismagius',
 'Honchkrow',
 'Glameow',
 'Purugly',
 'Chingling',
 'Stunky',
 'Skuntank',
 'Bronzor',
 'Bronzong',
 'Bonsly',
 'Mime Jr.',
 'Happiny',
 'Chatot',
 'Spiritomb',
 'Gible',
 'Gabite',
 'Garchomp',
 'Munchlax',
 'Riolu',
 'Lucario',
 'Hippopotas',
 'Hippowdon',
 'Skorupi',
 'Drapion',
 'Croagunk',
 'Toxicroak',
 'Carnivine',
 'Finneon',
 'Lumineon',
 'Mantyke',
 'Snover',
 'Abomasnow',
 'Weavile',
 'Magnezone',
 'Lickilicky',
 'Rhyperior',
 'Tangrowth',
 'Electivire',
 'Magmortar',
 'Togekiss',
 'Yanmega',
 'Leafeon',
 'Glaceon',
 'Gliscor',
 'Mamoswine',
 'Porygon-Z',
 'Gallade',
 'Probopass',
 'Dusknoir',
 'Froslass',
 'Rotom',
 'Uxie',
 'Mesprit',
 'Azelf',
 'Dialga',
 'Palkia',
 'Heatran',
 'Regigigas',
 'Giratina',
 'Cresselia',
 'Phione',
 'Manaphy',
 'Darkrai',
 'Shaymin',
 'Arceus',
 'Victini',
 'Snivy',
 'Servine',
 'Serperior',
 'Tepig',
 'Pignite',
 'Emboar',
 'Oshawott',
 'Dewott',
 'Samurott',
 'Patrat',
 'Watchog',
 'Lillipup',
 'Herdier',
 'Stoutland',
 'Purrloin',
 'Liepard',
 'Pansage',
 'Simisage',
 'Pansear',
 'Simisear',
 'Panpour',
 'Simipour',
 'Munna',
 'Musharna',
 'Pidove',
 'Tranquill',
 'Unfezant',
 'Blitzle',
 'Zebstrika',
 'Roggenrola',
 'Boldore',
 'Gigalith',
 'Woobat',
 'Swoobat',
 'Drilbur',
 'Excadrill',
 'Audino',
 'Timburr',
 'Gurdurr',
 'Conkeldurr',
 'Tympole',
 'Palpitoad',
 'Seismitoad',
 'Throh',
 'Sawk',
 'Sewaddle',
 'Swadloon',
 'Leavanny',
 'Venipede',
 'Whirlipede',
 'Scolipede',
 'Cottonee',
 'Whimsicott',
 'Petilil',
 'Lilligant',
 'Basculin',
 'Sandile',
 'Krokorok',
 'Krookodile',
 'Darumaka',
 'Darmanitan',
 'Maractus',
 'Dwebble',
 'Crustle',
 'Scraggy',
 'Scrafty',
 'Sigilyph',
 'Yamask',
 'Cofagrigus',
 'Tirtouga',
 'Carracosta',
 'Archen',
 'Archeops',
 'Trubbish',
 'Garbodor',
 'Zorua',
 'Zoroark',
 'Minccino',
 'Cinccino',
 'Gothita',
 'Gothorita',
 'Gothitelle',
 'Solosis',
 'Duosion',
 'Reuniclus',
 'Ducklett',
 'Swanna',
 'Vanillite',
 'Vanillish',
 'Vanilluxe',
 'Deerling',
 'Sawsbuck',
 'Emolga',
 'Karrablast',
 'Escavalier',
 'Foongus',
 'Amoonguss',
 'Frillish',
 'Jellicent',
 'Alomomola',
 'Joltik',
 'Galvantula',
 'Ferroseed',
 'Ferrothorn',
 'Klink',
 'Klang',
 'Klinklang',
 'Tynamo',
 'Eelektrik',
 'Eelektross',
 'Elgyem',
 'Beheeyem',
 'Litwick',
 'Lampent',
 'Chandelure',
 'Axew',
 'Fraxure',
 'Haxorus',
 'Cubchoo',
 'Beartic',
 'Cryogonal',
 'Shelmet',
 'Accelgor',
 'Stunfisk',
 'Mienfoo',
 'Mienshao',
 'Druddigon',
 'Golett',
 'Golurk',
 'Pawniard',
 'Bisharp',
 'Bouffalant',
 'Rufflet',
 'Braviary',
 'Vullaby',
 'Mandibuzz',
 'Heatmor',
 'Durant',
 'Deino',
 'Zweilous',
 'Hydreigon',
 'Larvesta',
 'Volcarona',
 'Cobalion',
 'Terrakion',
 'Virizion',
 'Tornadus',
 'Thundurus',
 'Reshiram',
 'Zekrom',
 'Landorus',
 'Kyurem',
 'Keldeo',
 'Meloetta',
 'Genesect',
 'Chespin',
 'Quilladin',
 'Chesnaught',
 'Fennekin',
 'Braixen',
 'Delphox',
 'Froakie',
 'Frogadier',
 'Greninja',
 'Bunnelby',
 'Diggersby',
 'Fletchling',
 'Fletchinder',
 'Talonflame',
 'Scatterbug',
 'Spewpa',
 'Vivillon',
 'Litleo',
 'Pyroar',
 'Flabébé',
 'Floette',
 'Florges',
 'Skiddo',
 'Gogoat',
 'Pancham',
 'Pangoro',
 'Furfrou',
 'Espurr',
 'Meowstic',
 'Honedge',
 'Doublade',
 'Aegislash',
 'Spritzee',
 'Aromatisse',
 'Swirlix',
 'Slurpuff',
 'Inkay',
 'Malamar',
 'Binacle',
 'Barbaracle',
 'Skrelp',
 'Dragalge',
 'Clauncher',
 'Clawitzer',
 'Helioptile',
 'Heliolisk',
 'Tyrunt',
 'Tyrantrum',
 'Amaura',
 'Aurorus',
 'Sylveon',
 'Hawlucha',
 'Dedenne',
 'Carbink',
 'Goomy',
 'Sliggoo',
 'Goodra',
 'Klefki',
 'Phantump',
 'Trevenant',
 'Pumpkaboo',
 'Gourgeist',
 'Bergmite',
 'Avalugg',
 'Noibat',
 'Noivern',
 'Xerneas',
 'Yveltal',
 'Zygarde',
 'Diancie',
 'Hoopa',
 'Volcanion']

 #in
 dict(pokemon)
 #out
 {0: 'Bulbasaur',
 1: 'Ivysaur',
 2: 'Venusaur',
 3: 'Charmander',
 4: 'Charmeleon',
 5: 'Charizard',
 6: 'Squirtle',
 7: 'Wartortle',
 8: 'Blastoise',
 9: 'Caterpie',
 10: 'Metapod',
 11: 'Butterfree',
 12: 'Weedle',
 13: 'Kakuna',
 14: 'Beedrill',
 15: 'Pidgey',
 16: 'Pidgeotto',
 17: 'Pidgeot',
 18: 'Rattata',
 19: 'Raticate',
 20: 'Spearow',
 21: 'Fearow',
 22: 'Ekans',
 23: 'Arbok',
 24: 'Pikachu',
 25: 'Raichu',
 26: 'Sandshrew',
 27: 'Sandslash',
 28: 'Nidoran',
 29: 'Nidorina',
 30: 'Nidoqueen',
 31: 'Nidoran♂',
 32: 'Nidorino',
 33: 'Nidoking',
 34: 'Clefairy',
 35: 'Clefable',
 36: 'Vulpix',
 37: 'Ninetales',
 38: 'Jigglypuff',
 39: 'Wigglytuff',
 40: 'Zubat',
 41: 'Golbat',
 42: 'Oddish',
 43: 'Gloom',
 44: 'Vileplume',
 45: 'Paras',
 46: 'Parasect',
 47: 'Venonat',
 48: 'Venomoth',
 49: 'Diglett',
 50: 'Dugtrio',
 51: 'Meowth',
 52: 'Persian',
 53: 'Psyduck',
 54: 'Golduck',
 55: 'Mankey',
 56: 'Primeape',
 57: 'Growlithe',
 58: 'Arcanine',
 59: 'Poliwag',
 60: 'Poliwhirl',
 61: 'Poliwrath',
 62: 'Abra',
 63: 'Kadabra',
 64: 'Alakazam',
 65: 'Machop',
 66: 'Machoke',
 67: 'Machamp',
 68: 'Bellsprout',
 69: 'Weepinbell',
 70: 'Victreebel',
 71: 'Tentacool',
 72: 'Tentacruel',
 73: 'Geodude',
 74: 'Graveler',
 75: 'Golem',
 76: 'Ponyta',
 77: 'Rapidash',
 78: 'Slowpoke',
 79: 'Slowbro',
 80: 'Magnemite',
 81: 'Magneton',
 82: "Farfetch'd",
 83: 'Doduo',
 84: 'Dodrio',
 85: 'Seel',
 86: 'Dewgong',
 87: 'Grimer',
 88: 'Muk',
 89: 'Shellder',
 90: 'Cloyster',
 91: 'Gastly',
 92: 'Haunter',
 93: 'Gengar',
 94: 'Onix',
 95: 'Drowzee',
 96: 'Hypno',
 97: 'Krabby',
 98: 'Kingler',
 99: 'Voltorb',
 100: 'Electrode',
 101: 'Exeggcute',
 102: 'Exeggutor',
 103: 'Cubone',
 104: 'Marowak',
 105: 'Hitmonlee',
 106: 'Hitmonchan',
 107: 'Lickitung',
 108: 'Koffing',
 109: 'Weezing',
 110: 'Rhyhorn',
 111: 'Rhydon',
 112: 'Chansey',
 113: 'Tangela',
 114: 'Kangaskhan',
 115: 'Horsea',
 116: 'Seadra',
 117: 'Goldeen',
 118: 'Seaking',
 119: 'Staryu',
 120: 'Starmie',
 121: 'Mr. Mime',
 122: 'Scyther',
 123: 'Jynx',
 124: 'Electabuzz',
 125: 'Magmar',
 126: 'Pinsir',
 127: 'Tauros',
 128: 'Magikarp',
 129: 'Gyarados',
 130: 'Lapras',
 131: 'Ditto',
 132: 'Eevee',
 133: 'Vaporeon',
 134: 'Jolteon',
 135: 'Flareon',
 136: 'Porygon',
 137: 'Omanyte',
 138: 'Omastar',
 139: 'Kabuto',
 140: 'Kabutops',
 141: 'Aerodactyl',
 142: 'Snorlax',
 143: 'Articuno',
 144: 'Zapdos',
 145: 'Moltres',
 146: 'Dratini',
 147: 'Dragonair',
 148: 'Dragonite',
 149: 'Mewtwo',
 150: 'Mew',
 151: 'Chikorita',
 152: 'Bayleef',
 153: 'Meganium',
 154: 'Cyndaquil',
 155: 'Quilava',
 156: 'Typhlosion',
 157: 'Totodile',
 158: 'Croconaw',
 159: 'Feraligatr',
 160: 'Sentret',
 161: 'Furret',
 162: 'Hoothoot',
 163: 'Noctowl',
 164: 'Ledyba',
 165: 'Ledian',
 166: 'Spinarak',
 167: 'Ariados',
 168: 'Crobat',
 169: 'Chinchou',
 170: 'Lanturn',
 171: 'Pichu',
 172: 'Cleffa',
 173: 'Igglybuff',
 174: 'Togepi',
 175: 'Togetic',
 176: 'Natu',
 177: 'Xatu',
 178: 'Mareep',
 179: 'Flaaffy',
 180: 'Ampharos',
 181: 'Bellossom',
 182: 'Marill',
 183: 'Azumarill',
 184: 'Sudowoodo',
 185: 'Politoed',
 186: 'Hoppip',
 187: 'Skiploom',
 188: 'Jumpluff',
 189: 'Aipom',
 190: 'Sunkern',
 191: 'Sunflora',
 192: 'Yanma',
 193: 'Wooper',
 194: 'Quagsire',
 195: 'Espeon',
 196: 'Umbreon',
 197: 'Murkrow',
 198: 'Slowking',
 199: 'Misdreavus',
 200: 'Unown',
 201: 'Wobbuffet',
 202: 'Girafarig',
 203: 'Pineco',
 204: 'Forretress',
 205: 'Dunsparce',
 206: 'Gligar',
 207: 'Steelix',
 208: 'Snubbull',
 209: 'Granbull',
 210: 'Qwilfish',
 211: 'Scizor',
 212: 'Shuckle',
 213: 'Heracross',
 214: 'Sneasel',
 215: 'Teddiursa',
 216: 'Ursaring',
 217: 'Slugma',
 218: 'Magcargo',
 219: 'Swinub',
 220: 'Piloswine',
 221: 'Corsola',
 222: 'Remoraid',
 223: 'Octillery',
 224: 'Delibird',
 225: 'Mantine',
 226: 'Skarmory',
 227: 'Houndour',
 228: 'Houndoom',
 229: 'Kingdra',
 230: 'Phanpy',
 231: 'Donphan',
 232: 'Porygon2',
 233: 'Stantler',
 234: 'Smeargle',
 235: 'Tyrogue',
 236: 'Hitmontop',
 237: 'Smoochum',
 238: 'Elekid',
 239: 'Magby',
 240: 'Miltank',
 241: 'Blissey',
 242: 'Raikou',
 243: 'Entei',
 244: 'Suicune',
 245: 'Larvitar',
 246: 'Pupitar',
 247: 'Tyranitar',
 248: 'Lugia',
 249: 'Ho-oh',
 250: 'Celebi',
 251: 'Treecko',
 252: 'Grovyle',
 253: 'Sceptile',
 254: 'Torchic',
 255: 'Combusken',
 256: 'Blaziken',
 257: 'Mudkip',
 258: 'Marshtomp',
 259: 'Swampert',
 260: 'Poochyena',
 261: 'Mightyena',
 262: 'Zigzagoon',
 263: 'Linoone',
 264: 'Wurmple',
 265: 'Silcoon',
 266: 'Beautifly',
 267: 'Cascoon',
 268: 'Dustox',
 269: 'Lotad',
 270: 'Lombre',
 271: 'Ludicolo',
 272: 'Seedot',
 273: 'Nuzleaf',
 274: 'Shiftry',
 275: 'Taillow',
 276: 'Swellow',
 277: 'Wingull',
 278: 'Pelipper',
 279: 'Ralts',
 280: 'Kirlia',
 281: 'Gardevoir',
 282: 'Surskit',
 283: 'Masquerain',
 284: 'Shroomish',
 285: 'Breloom',
 286: 'Slakoth',
 287: 'Vigoroth',
 288: 'Slaking',
 289: 'Nincada',
 290: 'Ninjask',
 291: 'Shedinja',
 292: 'Whismur',
 293: 'Loudred',
 294: 'Exploud',
 295: 'Makuhita',
 296: 'Hariyama',
 297: 'Azurill',
 298: 'Nosepass',
 299: 'Skitty',
 300: 'Delcatty',
 301: 'Sableye',
 302: 'Mawile',
 303: 'Aron',
 304: 'Lairon',
 305: 'Aggron',
 306: 'Meditite',
 307: 'Medicham',
 308: 'Electrike',
 309: 'Manectric',
 310: 'Plusle',
 311: 'Minun',
 312: 'Volbeat',
 313: 'Illumise',
 314: 'Roselia',
 315: 'Gulpin',
 316: 'Swalot',
 317: 'Carvanha',
 318: 'Sharpedo',
 319: 'Wailmer',
 320: 'Wailord',
 321: 'Numel',
 322: 'Camerupt',
 323: 'Torkoal',
 324: 'Spoink',
 325: 'Grumpig',
 326: 'Spinda',
 327: 'Trapinch',
 328: 'Vibrava',
 329: 'Flygon',
 330: 'Cacnea',
 331: 'Cacturne',
 332: 'Swablu',
 333: 'Altaria',
 334: 'Zangoose',
 335: 'Seviper',
 336: 'Lunatone',
 337: 'Solrock',
 338: 'Barboach',
 339: 'Whiscash',
 340: 'Corphish',
 341: 'Crawdaunt',
 342: 'Baltoy',
 343: 'Claydol',
 344: 'Lileep',
 345: 'Cradily',
 346: 'Anorith',
 347: 'Armaldo',
 348: 'Feebas',
 349: 'Milotic',
 350: 'Castform',
 351: 'Kecleon',
 352: 'Shuppet',
 353: 'Banette',
 354: 'Duskull',
 355: 'Dusclops',
 356: 'Tropius',
 357: 'Chimecho',
 358: 'Absol',
 359: 'Wynaut',
 360: 'Snorunt',
 361: 'Glalie',
 362: 'Spheal',
 363: 'Sealeo',
 364: 'Walrein',
 365: 'Clamperl',
 366: 'Huntail',
 367: 'Gorebyss',
 368: 'Relicanth',
 369: 'Luvdisc',
 370: 'Bagon',
 371: 'Shelgon',
 372: 'Salamence',
 373: 'Beldum',
 374: 'Metang',
 375: 'Metagross',
 376: 'Regirock',
 377: 'Regice',
 378: 'Registeel',
 379: 'Latias',
 380: 'Latios',
 381: 'Kyogre',
 382: 'Groudon',
 383: 'Rayquaza',
 384: 'Jirachi',
 385: 'Deoxys',
 386: 'Turtwig',
 387: 'Grotle',
 388: 'Torterra',
 389: 'Chimchar',
 390: 'Monferno',
 391: 'Infernape',
 392: 'Piplup',
 393: 'Prinplup',
 394: 'Empoleon',
 395: 'Starly',
 396: 'Staravia',
 397: 'Staraptor',
 398: 'Bidoof',
 399: 'Bibarel',
 400: 'Kricketot',
 401: 'Kricketune',
 402: 'Shinx',
 403: 'Luxio',
 404: 'Luxray',
 405: 'Budew',
 406: 'Roserade',
 407: 'Cranidos',
 408: 'Rampardos',
 409: 'Shieldon',
 410: 'Bastiodon',
 411: 'Burmy',
 412: 'Wormadam',
 413: 'Mothim',
 414: 'Combee',
 415: 'Vespiquen',
 416: 'Pachirisu',
 417: 'Buizel',
 418: 'Floatzel',
 419: 'Cherubi',
 420: 'Cherrim',
 421: 'Shellos',
 422: 'Gastrodon',
 423: 'Ambipom',
 424: 'Drifloon',
 425: 'Drifblim',
 426: 'Buneary',
 427: 'Lopunny',
 428: 'Mismagius',
 429: 'Honchkrow',
 430: 'Glameow',
 431: 'Purugly',
 432: 'Chingling',
 433: 'Stunky',
 434: 'Skuntank',
 435: 'Bronzor',
 436: 'Bronzong',
 437: 'Bonsly',
 438: 'Mime Jr.',
 439: 'Happiny',
 440: 'Chatot',
 441: 'Spiritomb',
 442: 'Gible',
 443: 'Gabite',
 444: 'Garchomp',
 445: 'Munchlax',
 446: 'Riolu',
 447: 'Lucario',
 448: 'Hippopotas',
 449: 'Hippowdon',
 450: 'Skorupi',
 451: 'Drapion',
 452: 'Croagunk',
 453: 'Toxicroak',
 454: 'Carnivine',
 455: 'Finneon',
 456: 'Lumineon',
 457: 'Mantyke',
 458: 'Snover',
 459: 'Abomasnow',
 460: 'Weavile',
 461: 'Magnezone',
 462: 'Lickilicky',
 463: 'Rhyperior',
 464: 'Tangrowth',
 465: 'Electivire',
 466: 'Magmortar',
 467: 'Togekiss',
 468: 'Yanmega',
 469: 'Leafeon',
 470: 'Glaceon',
 471: 'Gliscor',
 472: 'Mamoswine',
 473: 'Porygon-Z',
 474: 'Gallade',
 475: 'Probopass',
 476: 'Dusknoir',
 477: 'Froslass',
 478: 'Rotom',
 479: 'Uxie',
 480: 'Mesprit',
 481: 'Azelf',
 482: 'Dialga',
 483: 'Palkia',
 484: 'Heatran',
 485: 'Regigigas',
 486: 'Giratina',
 487: 'Cresselia',
 488: 'Phione',
 489: 'Manaphy',
 490: 'Darkrai',
 491: 'Shaymin',
 492: 'Arceus',
 493: 'Victini',
 494: 'Snivy',
 495: 'Servine',
 496: 'Serperior',
 497: 'Tepig',
 498: 'Pignite',
 499: 'Emboar',
 500: 'Oshawott',
 501: 'Dewott',
 502: 'Samurott',
 503: 'Patrat',
 504: 'Watchog',
 505: 'Lillipup',
 506: 'Herdier',
 507: 'Stoutland',
 508: 'Purrloin',
 509: 'Liepard',
 510: 'Pansage',
 511: 'Simisage',
 512: 'Pansear',
 513: 'Simisear',
 514: 'Panpour',
 515: 'Simipour',
 516: 'Munna',
 517: 'Musharna',
 518: 'Pidove',
 519: 'Tranquill',
 520: 'Unfezant',
 521: 'Blitzle',
 522: 'Zebstrika',
 523: 'Roggenrola',
 524: 'Boldore',
 525: 'Gigalith',
 526: 'Woobat',
 527: 'Swoobat',
 528: 'Drilbur',
 529: 'Excadrill',
 530: 'Audino',
 531: 'Timburr',
 532: 'Gurdurr',
 533: 'Conkeldurr',
 534: 'Tympole',
 535: 'Palpitoad',
 536: 'Seismitoad',
 537: 'Throh',
 538: 'Sawk',
 539: 'Sewaddle',
 540: 'Swadloon',
 541: 'Leavanny',
 542: 'Venipede',
 543: 'Whirlipede',
 544: 'Scolipede',
 545: 'Cottonee',
 546: 'Whimsicott',
 547: 'Petilil',
 548: 'Lilligant',
 549: 'Basculin',
 550: 'Sandile',
 551: 'Krokorok',
 552: 'Krookodile',
 553: 'Darumaka',
 554: 'Darmanitan',
 555: 'Maractus',
 556: 'Dwebble',
 557: 'Crustle',
 558: 'Scraggy',
 559: 'Scrafty',
 560: 'Sigilyph',
 561: 'Yamask',
 562: 'Cofagrigus',
 563: 'Tirtouga',
 564: 'Carracosta',
 565: 'Archen',
 566: 'Archeops',
 567: 'Trubbish',
 568: 'Garbodor',
 569: 'Zorua',
 570: 'Zoroark',
 571: 'Minccino',
 572: 'Cinccino',
 573: 'Gothita',
 574: 'Gothorita',
 575: 'Gothitelle',
 576: 'Solosis',
 577: 'Duosion',
 578: 'Reuniclus',
 579: 'Ducklett',
 580: 'Swanna',
 581: 'Vanillite',
 582: 'Vanillish',
 583: 'Vanilluxe',
 584: 'Deerling',
 585: 'Sawsbuck',
 586: 'Emolga',
 587: 'Karrablast',
 588: 'Escavalier',
 589: 'Foongus',
 590: 'Amoonguss',
 591: 'Frillish',
 592: 'Jellicent',
 593: 'Alomomola',
 594: 'Joltik',
 595: 'Galvantula',
 596: 'Ferroseed',
 597: 'Ferrothorn',
 598: 'Klink',
 599: 'Klang',
 600: 'Klinklang',
 601: 'Tynamo',
 602: 'Eelektrik',
 603: 'Eelektross',
 604: 'Elgyem',
 605: 'Beheeyem',
 606: 'Litwick',
 607: 'Lampent',
 608: 'Chandelure',
 609: 'Axew',
 610: 'Fraxure',
 611: 'Haxorus',
 612: 'Cubchoo',
 613: 'Beartic',
 614: 'Cryogonal',
 615: 'Shelmet',
 616: 'Accelgor',
 617: 'Stunfisk',
 618: 'Mienfoo',
 619: 'Mienshao',
 620: 'Druddigon',
 621: 'Golett',
 622: 'Golurk',
 623: 'Pawniard',
 624: 'Bisharp',
 625: 'Bouffalant',
 626: 'Rufflet',
 627: 'Braviary',
 628: 'Vullaby',
 629: 'Mandibuzz',
 630: 'Heatmor',
 631: 'Durant',
 632: 'Deino',
 633: 'Zweilous',
 634: 'Hydreigon',
 635: 'Larvesta',
 636: 'Volcarona',
 637: 'Cobalion',
 638: 'Terrakion',
 639: 'Virizion',
 640: 'Tornadus',
 641: 'Thundurus',
 642: 'Reshiram',
 643: 'Zekrom',
 644: 'Landorus',
 645: 'Kyurem',
 646: 'Keldeo',
 647: 'Meloetta',
 648: 'Genesect',
 649: 'Chespin',
 650: 'Quilladin',
 651: 'Chesnaught',
 652: 'Fennekin',
 653: 'Braixen',
 654: 'Delphox',
 655: 'Froakie',
 656: 'Frogadier',
 657: 'Greninja',
 658: 'Bunnelby',
 659: 'Diggersby',
 660: 'Fletchling',
 661: 'Fletchinder',
 662: 'Talonflame',
 663: 'Scatterbug',
 664: 'Spewpa',
 665: 'Vivillon',
 666: 'Litleo',
 667: 'Pyroar',
 668: 'Flabébé',
 669: 'Floette',
 670: 'Florges',
 671: 'Skiddo',
 672: 'Gogoat',
 673: 'Pancham',
 674: 'Pangoro',
 675: 'Furfrou',
 676: 'Espurr',
 677: 'Meowstic',
 678: 'Honedge',
 679: 'Doublade',
 680: 'Aegislash',
 681: 'Spritzee',
 682: 'Aromatisse',
 683: 'Swirlix',
 684: 'Slurpuff',
 685: 'Inkay',
 686: 'Malamar',
 687: 'Binacle',
 688: 'Barbaracle',
 689: 'Skrelp',
 690: 'Dragalge',
 691: 'Clauncher',
 692: 'Clawitzer',
 693: 'Helioptile',
 694: 'Heliolisk',
 695: 'Tyrunt',
 696: 'Tyrantrum',
 697: 'Amaura',
 698: 'Aurorus',
 699: 'Sylveon',
 700: 'Hawlucha',
 701: 'Dedenne',
 702: 'Carbink',
 703: 'Goomy',
 704: 'Sliggoo',
 705: 'Goodra',
 706: 'Klefki',
 707: 'Phantump',
 708: 'Trevenant',
 709: 'Pumpkaboo',
 710: 'Gourgeist',
 711: 'Bergmite',
 712: 'Avalugg',
 713: 'Noibat',
 714: 'Noivern',
 715: 'Xerneas',
 716: 'Yveltal',
 717: 'Zygarde',
 718: 'Diancie',
 719: 'Hoopa',
 720: 'Volcanion'}

#in
max(pokemon)
#out
'Zygarde'

#in
min(pokemon)
#out
'Abomasnow'

#in
max(google)
#out
782.22

#in
min(google)
#out
49.95

## The sort_values Method ##
#################################################

#in
pokemon.sort_value()
#out
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[30], line 1
----> 1 pokemon.sort_value()

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\generic.py:5902, in NDFrame.__getattr__(self, name)
   5895 if (
   5896     name not in self._internal_names_set
   5897     and name not in self._metadata
   5898     and name not in self._accessors
   5899     and self._info_axis._can_hold_identifiers_and_holds_name(name)
   5900 ):
   5901     return self[name]
-> 5902 return object.__getattribute__(self, name)

AttributeError: 'Series' object has no attribute 'sort_value'

#in
pokemon.sort_values()
#out
459    Abomasnow
62          Abra
358        Absol
616     Accelgor
680    Aegislash
         ...    
570      Zoroark
569        Zorua
40         Zubat
633     Zweilous
717      Zygarde
Name: Pokemon, Length: 721, dtype: object

#in
pokemon.sort_values().head()
#out
459    Abomasnow
62          Abra
358        Absol
616     Accelgor
680    Aegislash
Name: Pokemon, dtype: object

#in
pokemon.sort_values(ascending = True).head()
#out
459    Abomasnow
62          Abra
358        Absol
616     Accelgor
680    Aegislash
Name: Pokemon, dtype: object

#in
pokemon.sort_values(ascending = False)
#out
717      Zygarde
633     Zweilous
40         Zubat
569        Zorua
570      Zoroark
         ...    
680    Aegislash
616     Accelgor
358        Absol
62          Abra
459    Abomasnow
Name: Pokemon, Length: 721, dtype: object

#in
pokemon.sort_values(ascending = False).head()
#out
717     Zygarde
633    Zweilous
40        Zubat
569       Zorua
570     Zoroark
Name: Pokemon, dtype: object

#in
google.sort_values()
#out
11       49.95
9        50.07
0        50.12
10       50.70
12       50.74
         ...  
3010    771.61
3007    772.88
3009    773.18
2859    776.60
3011    782.22
Name: Stock Price, Length: 3012, dtype: float64

#in
google.sort_values(ascending = True)
#out
11       49.95
9        50.07
0        50.12
10       50.70
12       50.74
         ...  
3010    771.61
3007    772.88
3009    773.18
2859    776.60
3011    782.22
Name: Stock Price, Length: 3012, dtype: float64

#in
google.sort_values(ascending = False).head()
#out
3011    782.22
2859    776.60
3009    773.18
3007    772.88
3010    771.61
Name: Stock Price, dtype: float64

## EXERCISE ##
# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work

import pandas as pd

# Below, we have a list of delicious tortilla chip flavors
flavors = ["Spicy Sweet Chili", "Cool Ranch", "Nacho Cheese", "Salsa Verde"]

# Create a new Series object, passing in the flavors list defined above
# Assign it to a 'doritos' variable. The resulting Series should look like this:
#
#
#   0    Spicy Sweet Chili
#   1           Cool Ranch
#   2         Nacho Cheese
#   3          Salsa Verde
#   dtype: object

doritos = pd.Series(flavors)

# Below, sort the doritos Series in descending order.
# Assign the sorted a Series to a 'sorted_doritos' variable.
# The sorted Series should like this:
#
#   0    Spicy Sweet Chili
#   3          Salsa Verde
#   2         Nacho Cheese
#   1           Cool Ranch
#   dtype: object

sorted_doritos = doritos.sort_values(ascending = False)

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
pd.read_csv("pokemon.csv", index_col = "Pokemon")
#out
Type
Pokemon	
Bulbasaur	Grass
Ivysaur	Grass
Venusaur	Grass
Charmander	Fire
Charmeleon	Fire
...	...
Yveltal	Dark
Zygarde	Dragon
Diancie	Rock
Hoopa	Psychic
Volcanion	Fire
721 rows × 1 columns

#in
pd.read_csv("pokemon.csv", index_col = "Pokemon").squeeze("columns")
#out
Pokemon
Bulbasaur       Grass
Ivysaur         Grass
Venusaur        Grass
Charmander       Fire
Charmeleon       Fire
               ...   
Yveltal          Dark
Zygarde        Dragon
Diancie          Rock
Hoopa         Psychic
Volcanion        Fire
Name: Type, Length: 721, dtype: object

#in
pokemon = pd.read_csv("pokemon.csv", index_col = "Pokemon").squeeze("columns")
pokemon
#out
Pokemon
Bulbasaur       Grass
Ivysaur         Grass
Venusaur        Grass
Charmander       Fire
Charmeleon       Fire
               ...   
Yveltal          Dark
Zygarde        Dragon
Diancie          Rock
Hoopa         Psychic
Volcanion        Fire
Name: Type, Length: 721, dtype: object

#in
pokemon = pd.read_csv("pokemon.csv", index_col = "Pokemon").squeeze("columns")
pokemon.head()
#out
Pokemon
Bulbasaur     Grass
Ivysaur       Grass
Venusaur      Grass
Charmander     Fire
Charmeleon     Fire
Name: Type, dtype: object

#in
pokemon.sort_index()
#out
Pokemon
Abomasnow      Grass
Abra         Psychic
Absol           Dark
Accelgor         Bug
Aegislash      Steel
              ...   
Zoroark         Dark
Zorua           Dark
Zubat         Poison
Zweilous        Dark
Zygarde       Dragon
Name: Type, Length: 721, dtype: object

#in
pokemon.sort_index(ascending = True)
#out
Pokemon
Abomasnow      Grass
Abra         Psychic
Absol           Dark
Accelgor         Bug
Aegislash      Steel
              ...   
Zoroark         Dark
Zorua           Dark
Zubat         Poison
Zweilous        Dark
Zygarde       Dragon
Name: Type, Length: 721, dtype: object

#in
pokemon.sort_index(ascending = False)
#out
Pokemon
Zygarde       Dragon
Zweilous        Dark
Zubat         Poison
Zorua           Dark
Zoroark         Dark
              ...   
Aegislash      Steel
Accelgor         Bug
Absol           Dark
Abra         Psychic
Abomasnow      Grass
Name: Type, Length: 721, dtype: object

## EXERCISE ##
# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work
import pandas as pd

# Below, we have a list of delicious drink flavors
# We create a sorted Series of strings and assign it to a 'gatorade' variable
flavors = ["Red", "Blue", "Green", "Orange"]
gatorade = pd.Series(flavors).sort_values()

# I'd like to return the Series to its original order 
# (sorted by the numeric index in ascending order). 
# Sort the gatorade Series by index.
# Assign the result to an 'original' variable.
original = pd.Series(flavors).sort_index()
#or
original = gatorade.sort_index()

## Check for Inclusion with Python's in Keyword ##
#################################################

#in
pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"]).squeeze("columns")
pokemon.head()
#out
0     Bulbasaur
1       Ivysaur
2      Venusaur
3    Charmander
4    Charmeleon
Name: Pokemon, dtype: object

#in
"car" in "racecar"
#out
True

#in
2 in [1, 2, 3]
#out
True

#in
"Bulbasaur" in pokemon
#out
False

#in
100 in pokemon
#out
True

#in
100 in pokemon
#out
True

#in
pokemon.index
#out
RangeIndex(start=0, stop=721, step=1)

#in
100 in pokemon.index
#out
True

#in
pokemon.values
#out
array(['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon',
       'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie',
       'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey',
       'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow',
       'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash',
       'Nidoran', 'Nidorina', 'Nidoqueen', 'Nidoran♂', 'Nidorino',
       'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales',
       'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom',
       'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett',
       'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey',
       'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl',
       'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke',
       'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool',
       'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash',
       'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', "Farfetch'd",
       'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder',
       'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee',
       'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute',
       'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan',
       'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey',
       'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking',
       'Staryu', 'Starmie', 'Mr. Mime', 'Scyther', 'Jynx', 'Electabuzz',
       'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras',
       'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon',
       'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl',
       'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair',
       'Dragonite', 'Mewtwo', 'Mew', 'Chikorita', 'Bayleef', 'Meganium',
       'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw',
       'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba',
       'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou', 'Lanturn',
       'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu',
       'Xatu', 'Mareep', 'Flaaffy', 'Ampharos', 'Bellossom', 'Marill',
       'Azumarill', 'Sudowoodo', 'Politoed', 'Hoppip', 'Skiploom',
       'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Wooper',
       'Quagsire', 'Espeon', 'Umbreon', 'Murkrow', 'Slowking',
       'Misdreavus', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco',
       'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Snubbull',
       'Granbull', 'Qwilfish', 'Scizor', 'Shuckle', 'Heracross',
       'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo', 'Swinub',
       'Piloswine', 'Corsola', 'Remoraid', 'Octillery', 'Delibird',
       'Mantine', 'Skarmory', 'Houndour', 'Houndoom', 'Kingdra', 'Phanpy',
       'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue',
       'Hitmontop', 'Smoochum', 'Elekid', 'Magby', 'Miltank', 'Blissey',
       'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar', 'Tyranitar',
       'Lugia', 'Ho-oh', 'Celebi', 'Treecko', 'Grovyle', 'Sceptile',
       'Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp',
       'Swampert', 'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone',
       'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Lotad',
       'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow',
       'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia', 'Gardevoir',
       'Surskit', 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth',
       'Vigoroth', 'Slaking', 'Nincada', 'Ninjask', 'Shedinja', 'Whismur',
       'Loudred', 'Exploud', 'Makuhita', 'Hariyama', 'Azurill',
       'Nosepass', 'Skitty', 'Delcatty', 'Sableye', 'Mawile', 'Aron',
       'Lairon', 'Aggron', 'Meditite', 'Medicham', 'Electrike',
       'Manectric', 'Plusle', 'Minun', 'Volbeat', 'Illumise', 'Roselia',
       'Gulpin', 'Swalot', 'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord',
       'Numel', 'Camerupt', 'Torkoal', 'Spoink', 'Grumpig', 'Spinda',
       'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu',
       'Altaria', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock',
       'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy',
       'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas',
       'Milotic', 'Castform', 'Kecleon', 'Shuppet', 'Banette', 'Duskull',
       'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'Wynaut', 'Snorunt',
       'Glalie', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail',
       'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon',
       'Salamence', 'Beldum', 'Metang', 'Metagross', 'Regirock', 'Regice',
       'Registeel', 'Latias', 'Latios', 'Kyogre', 'Groudon', 'Rayquaza',
       'Jirachi', 'Deoxys', 'Turtwig', 'Grotle', 'Torterra', 'Chimchar',
       'Monferno', 'Infernape', 'Piplup', 'Prinplup', 'Empoleon',
       'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel',
       'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray', 'Budew',
       'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon',
       'Burmy', 'Wormadam', 'Mothim', 'Combee', 'Vespiquen', 'Pachirisu',
       'Buizel', 'Floatzel', 'Cherubi', 'Cherrim', 'Shellos', 'Gastrodon',
       'Ambipom', 'Drifloon', 'Drifblim', 'Buneary', 'Lopunny',
       'Mismagius', 'Honchkrow', 'Glameow', 'Purugly', 'Chingling',
       'Stunky', 'Skuntank', 'Bronzor', 'Bronzong', 'Bonsly', 'Mime Jr.',
       'Happiny', 'Chatot', 'Spiritomb', 'Gible', 'Gabite', 'Garchomp',
       'Munchlax', 'Riolu', 'Lucario', 'Hippopotas', 'Hippowdon',
       'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak', 'Carnivine',
       'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow', 'Weavile',
       'Magnezone', 'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire',
       'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon',
       'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'Probopass',
       'Dusknoir', 'Froslass', 'Rotom', 'Uxie', 'Mesprit', 'Azelf',
       'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina',
       'Cresselia', 'Phione', 'Manaphy', 'Darkrai', 'Shaymin', 'Arceus',
       'Victini', 'Snivy', 'Servine', 'Serperior', 'Tepig', 'Pignite',
       'Emboar', 'Oshawott', 'Dewott', 'Samurott', 'Patrat', 'Watchog',
       'Lillipup', 'Herdier', 'Stoutland', 'Purrloin', 'Liepard',
       'Pansage', 'Simisage', 'Pansear', 'Simisear', 'Panpour',
       'Simipour', 'Munna', 'Musharna', 'Pidove', 'Tranquill', 'Unfezant',
       'Blitzle', 'Zebstrika', 'Roggenrola', 'Boldore', 'Gigalith',
       'Woobat', 'Swoobat', 'Drilbur', 'Excadrill', 'Audino', 'Timburr',
       'Gurdurr', 'Conkeldurr', 'Tympole', 'Palpitoad', 'Seismitoad',
       'Throh', 'Sawk', 'Sewaddle', 'Swadloon', 'Leavanny', 'Venipede',
       'Whirlipede', 'Scolipede', 'Cottonee', 'Whimsicott', 'Petilil',
       'Lilligant', 'Basculin', 'Sandile', 'Krokorok', 'Krookodile',
       'Darumaka', 'Darmanitan', 'Maractus', 'Dwebble', 'Crustle',
       'Scraggy', 'Scrafty', 'Sigilyph', 'Yamask', 'Cofagrigus',
       'Tirtouga', 'Carracosta', 'Archen', 'Archeops', 'Trubbish',
       'Garbodor', 'Zorua', 'Zoroark', 'Minccino', 'Cinccino', 'Gothita',
       'Gothorita', 'Gothitelle', 'Solosis', 'Duosion', 'Reuniclus',
       'Ducklett', 'Swanna', 'Vanillite', 'Vanillish', 'Vanilluxe',
       'Deerling', 'Sawsbuck', 'Emolga', 'Karrablast', 'Escavalier',
       'Foongus', 'Amoonguss', 'Frillish', 'Jellicent', 'Alomomola',
       'Joltik', 'Galvantula', 'Ferroseed', 'Ferrothorn', 'Klink',
       'Klang', 'Klinklang', 'Tynamo', 'Eelektrik', 'Eelektross',
       'Elgyem', 'Beheeyem', 'Litwick', 'Lampent', 'Chandelure', 'Axew',
       'Fraxure', 'Haxorus', 'Cubchoo', 'Beartic', 'Cryogonal', 'Shelmet',
       'Accelgor', 'Stunfisk', 'Mienfoo', 'Mienshao', 'Druddigon',
       'Golett', 'Golurk', 'Pawniard', 'Bisharp', 'Bouffalant', 'Rufflet',
       'Braviary', 'Vullaby', 'Mandibuzz', 'Heatmor', 'Durant', 'Deino',
       'Zweilous', 'Hydreigon', 'Larvesta', 'Volcarona', 'Cobalion',
       'Terrakion', 'Virizion', 'Tornadus', 'Thundurus', 'Reshiram',
       'Zekrom', 'Landorus', 'Kyurem', 'Keldeo', 'Meloetta', 'Genesect',
       'Chespin', 'Quilladin', 'Chesnaught', 'Fennekin', 'Braixen',
       'Delphox', 'Froakie', 'Frogadier', 'Greninja', 'Bunnelby',
       'Diggersby', 'Fletchling', 'Fletchinder', 'Talonflame',
       'Scatterbug', 'Spewpa', 'Vivillon', 'Litleo', 'Pyroar', 'Flabébé',
       'Floette', 'Florges', 'Skiddo', 'Gogoat', 'Pancham', 'Pangoro',
       'Furfrou', 'Espurr', 'Meowstic', 'Honedge', 'Doublade',
       'Aegislash', 'Spritzee', 'Aromatisse', 'Swirlix', 'Slurpuff',
       'Inkay', 'Malamar', 'Binacle', 'Barbaracle', 'Skrelp', 'Dragalge',
       'Clauncher', 'Clawitzer', 'Helioptile', 'Heliolisk', 'Tyrunt',
       'Tyrantrum', 'Amaura', 'Aurorus', 'Sylveon', 'Hawlucha', 'Dedenne',
       'Carbink', 'Goomy', 'Sliggoo', 'Goodra', 'Klefki', 'Phantump',
       'Trevenant', 'Pumpkaboo', 'Gourgeist', 'Bergmite', 'Avalugg',
       'Noibat', 'Noivern', 'Xerneas', 'Yveltal', 'Zygarde', 'Diancie',
       'Hoopa', 'Volcanion'], dtype=object)

#in
"Bulbasaur" in pokemon.values
#out
True

#in
"Pikachu" in pokemon.values
#out
True

#in
"nonsense" in pokemon.values
#out
False

## Excersise ##
# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work
 
import pandas as pd
 
# This challenge includes a coffee.csv with 2 columns: 
# Coffee and Calories. Import the CSV. Assign the Coffee
# column to be the index and the Calories column to be the
# Series' values. Assign the Series to a 'coffee' variable.
coffee = pd.read_csv("coffee.csv", index_col = "Coffee").squeeze("columns")
 
# Check whether the coffee 'Flat White' is present in the data.
# Assign the result to a `flat_white` variable
flat_white = "Flat White" in coffee.index
 
# Check whether the coffee 'Cortado' is present in the data.
# Assign the result to a `cortado` variable
cortado = "Cortado" in coffee.index
 
# Check whether the coffee 'Blackberry Mocha' is present in the data.
# Assign the result to a `blackberry_mocha` variable
blackberry_mocha = "Blackberry Mocha" in coffee.index
 
# Check whether the value 221 is present in the data.
# Assign the result to a 'high_calorie' variable.
high_calorie = 221 in coffee.values
 
# Check whether the value 400 is present in the data.
# Assign the result to a 'super_high_calorie' variable.
super_high_calorie = 400 in coffee.values

## Extract Series Value by Index Position ##
#################################################

#in
import pandas as pd
pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"]).squeeze("columns")
pokemon.head()
#out
0     Bulbasaur
1       Ivysaur
2      Venusaur
3    Charmander
4    Charmeleon
Name: Pokemon, dtype: object

#in
pokemon[]
#out
  Cell In[4], line 1
    pokemon[]
            ^
SyntaxError: invalid syntax

#in
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
pokemon[0]
#out

#in
pokemon[500]
#out
'Oshawott'

#in
pokemon[1500]
#out
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexes\range.py:391, in RangeIndex.get_loc(self, key, method, tolerance)
    390 try:
--> 391     return self._range.index(new_key)
    392 except ValueError as err:

ValueError: 1500 is not in range

The above exception was the direct cause of the following exception:

KeyError                                  Traceback (most recent call last)
Cell In[8], line 1
----> 1 pokemon[1500]

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\series.py:981, in Series.__getitem__(self, key)
    978     return self._values[key]
    980 elif key_is_scalar:
--> 981     return self._get_value(key)
    983 if is_hashable(key):
    984     # Otherwise index.get_value will raise InvalidIndexError
    985     try:
    986         # For labels that don't resolve as scalars like tuples and frozensets

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\series.py:1089, in Series._get_value(self, label, takeable)
   1086     return self._values[label]
   1088 # Similar to Index.get_value, but we do not fall back to positional
-> 1089 loc = self.index.get_loc(label)
   1090 return self.index._get_values_for_loc(self, loc, label)

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexes\range.py:393, in RangeIndex.get_loc(self, key, method, tolerance)
    391         return self._range.index(new_key)
    392     except ValueError as err:
--> 393         raise KeyError(key) from err
    394 self._check_indexing_error(key)
    395 raise KeyError(key)

KeyError: 1500

#in
pokemon[] #holddown shift button and press tab button to see all the possible options to go into []
#out
Cell In[9], line 1
    pokemon[] #holddown shift button and press tab button to see all the possible options to go into []
            ^
SyntaxError: invalid syntax

#in
pokemon[[100, 200, 300]]
#out
100    Electrode
200        Unown
300     Delcatty
Name: Pokemon, dtype: object

#in
pokemon[27:35]
#out
27    Sandslash
28      Nidoran
29     Nidorina
30    Nidoqueen
31     Nidoran♂
32     Nidorino
33     Nidoking
34     Clefairy
Name: Pokemon, dtype: object

#in
pokemon[0:7]
#out
0     Bulbasaur
1       Ivysaur
2      Venusaur
3    Charmander
4    Charmeleon
5     Charizard
6      Squirtle
Name: Pokemon, dtype: object

#in
pokemon.head(7)
#out
0     Bulbasaur
1       Ivysaur
2      Venusaur
3    Charmander
4    Charmeleon
5     Charizard
6      Squirtle
Name: Pokemon, dtype: object

#in
pokemon[700:]
#out
700     Hawlucha
701      Dedenne
702      Carbink
703        Goomy
704      Sliggoo
705       Goodra
706       Klefki
707     Phantump
708    Trevenant
709    Pumpkaboo
710    Gourgeist
711     Bergmite
712      Avalugg
713       Noibat
714      Noivern
715      Xerneas
716      Yveltal
717      Zygarde
718      Diancie
719        Hoopa
720    Volcanion
Name: Pokemon, dtype: object

#in
pokemon[-1]
#out
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexes\range.py:391, in RangeIndex.get_loc(self, key, method, tolerance)
    390 try:
--> 391     return self._range.index(new_key)
    392 except ValueError as err:

ValueError: -1 is not in range

The above exception was the direct cause of the following exception:

KeyError                                  Traceback (most recent call last)
Cell In[15], line 1
----> 1 pokemon[-1]

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\series.py:981, in Series.__getitem__(self, key)
    978     return self._values[key]
    980 elif key_is_scalar:
--> 981     return self._get_value(key)
    983 if is_hashable(key):
    984     # Otherwise index.get_value will raise InvalidIndexError
    985     try:
    986         # For labels that don't resolve as scalars like tuples and frozensets

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\series.py:1089, in Series._get_value(self, label, takeable)
   1086     return self._values[label]
   1088 # Similar to Index.get_value, but we do not fall back to positional
-> 1089 loc = self.index.get_loc(label)
   1090 return self.index._get_values_for_loc(self, loc, label)

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexes\range.py:393, in RangeIndex.get_loc(self, key, method, tolerance)
    391         return self._range.index(new_key)
    392     except ValueError as err:
--> 393         raise KeyError(key) from err
    394 self._check_indexing_error(key)
    395 raise KeyError(key)

KeyError: -1

#in
pokemon[-20:-10]
#out
701      Dedenne
702      Carbink
703        Goomy
704      Sliggoo
705       Goodra
706       Klefki
707     Phantump
708    Trevenant
709    Pumpkaboo
710    Gourgeist
Name: Pokemon, dtype: object

#in
pokemon[-20:]
#out
701      Dedenne
702      Carbink
703        Goomy
704      Sliggoo
705       Goodra
706       Klefki
707     Phantump
708    Trevenant
709    Pumpkaboo
710    Gourgeist
711     Bergmite
712      Avalugg
713       Noibat
714      Noivern
715      Xerneas
716      Yveltal
717      Zygarde
718      Diancie
719        Hoopa
720    Volcanion
Name: Pokemon, dtype: object

#in
pokemon.tail(-20)
#out
20       Spearow
21        Fearow
22         Ekans
23         Arbok
24       Pikachu
         ...    
716      Yveltal
717      Zygarde
718      Diancie
719        Hoopa
720    Volcanion
Name: Pokemon, Length: 701, dtype: object

#in
pokemon = pd.read_csv("pokemon.csv", index_col = ["Pokemon"]).squeeze("columns")
pokemon.head()
#out
Pokemon
Bulbasaur     Grass
Ivysaur       Grass
Venusaur      Grass
Charmander     Fire
Charmeleon     Fire
Name: Type, dtype: object

#in
pokemon[0]
#out
'Grass'

#in
pokemon[[100, 134]]
#out
Pokemon
Electrode    Electric
Jolteon      Electric
Name: Type, dtype: object

#in
pokemon["Bulbasaur"]
#out
'Grass'

#in
pokemon["Mewtwo"]
#out
'Psychic'

#in
pokemon[["Charizard", "Jolteon", "Meowth"]]
#out
Pokemon
Charizard        Fire
Jolteon      Electric
Meowth         Normal
Name: Type, dtype: object

#in
pokemon["Digimon"]
#out
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexes\base.py:3802, in Index.get_loc(self, key, method, tolerance)
   3801 try:
-> 3802     return self._engine.get_loc(casted_key)
   3803 except KeyError as err:

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\_libs\index.pyx:138, in pandas._libs.index.IndexEngine.get_loc()

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\_libs\index.pyx:165, in pandas._libs.index.IndexEngine.get_loc()

File pandas\_libs\hashtable_class_helper.pxi:5745, in pandas._libs.hashtable.PyObjectHashTable.get_item()

File pandas\_libs\hashtable_class_helper.pxi:5753, in pandas._libs.hashtable.PyObjectHashTable.get_item()

KeyError: 'Digimon'

The above exception was the direct cause of the following exception:

KeyError                                  Traceback (most recent call last)
Cell In[25], line 1
----> 1 pokemon["Digimon"]

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\series.py:981, in Series.__getitem__(self, key)
    978     return self._values[key]
    980 elif key_is_scalar:
--> 981     return self._get_value(key)
    983 if is_hashable(key):
    984     # Otherwise index.get_value will raise InvalidIndexError
    985     try:
    986         # For labels that don't resolve as scalars like tuples and frozensets

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\series.py:1089, in Series._get_value(self, label, takeable)
   1086     return self._values[label]
   1088 # Similar to Index.get_value, but we do not fall back to positional
-> 1089 loc = self.index.get_loc(label)
   1090 return self.index._get_values_for_loc(self, loc, label)

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexes\base.py:3804, in Index.get_loc(self, key, method, tolerance)
   3802     return self._engine.get_loc(casted_key)
   3803 except KeyError as err:
-> 3804     raise KeyError(key) from err
   3805 except TypeError:
   3806     # If we have a listlike key, _check_indexing_error will raise
   3807     #  InvalidIndexError. Otherwise we fall through and re-raise
   3808     #  the TypeError.
   3809     self._check_indexing_error(key)

KeyError: 'Digimon'

#in
pokemon[["Pikachu", "Digimon"]]
#out
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[26], line 1
----> 1 pokemon[["Pikachu", "Digimon"]]

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\series.py:1007, in Series.__getitem__(self, key)
   1004     key = np.asarray(key, dtype=bool)
   1005     return self._get_values(key)
-> 1007 return self._get_with(key)

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\series.py:1047, in Series._get_with(self, key)
   1044         return self.iloc[key]
   1046 # handle the dup indexing case GH#4246
-> 1047 return self.loc[key]

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexing.py:1073, in _LocationIndexer.__getitem__(self, key)
   1070 axis = self.axis or 0
   1072 maybe_callable = com.apply_if_callable(key, self.obj)
-> 1073 return self._getitem_axis(maybe_callable, axis=axis)

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexing.py:1301, in _LocIndexer._getitem_axis(self, key, axis)
   1298     if hasattr(key, "ndim") and key.ndim > 1:
   1299         raise ValueError("Cannot index with multidimensional key")
-> 1301     return self._getitem_iterable(key, axis=axis)
   1303 # nested tuple slicing
   1304 if is_nested_tuple(key, labels):

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexing.py:1239, in _LocIndexer._getitem_iterable(self, key, axis)
   1236 self._validate_key(key, axis)
   1238 # A collection of keys
-> 1239 keyarr, indexer = self._get_listlike_indexer(key, axis)
   1240 return self.obj._reindex_with_indexers(
   1241     {axis: [keyarr, indexer]}, copy=True, allow_dups=True
   1242 )

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexing.py:1432, in _LocIndexer._get_listlike_indexer(self, key, axis)
   1429 ax = self.obj._get_axis(axis)
   1430 axis_name = self.obj._get_axis_name(axis)
-> 1432 keyarr, indexer = ax._get_indexer_strict(key, axis_name)
   1434 return keyarr, indexer

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexes\base.py:6070, in Index._get_indexer_strict(self, key, axis_name)
   6067 else:
   6068     keyarr, indexer, new_indexer = self._reindex_non_unique(keyarr)
-> 6070 self._raise_if_missing(keyarr, indexer, axis_name)
   6072 keyarr = self.take(indexer)
   6073 if isinstance(key, Index):
   6074     # GH 42790 - Preserve name from an Index

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexes\base.py:6133, in Index._raise_if_missing(self, key, indexer, axis_name)
   6130     raise KeyError(f"None of [{key}] are in the [{axis_name}]")
   6132 not_found = list(ensure_index(key)[missing_mask.nonzero()[0]].unique())
-> 6133 raise KeyError(f"{not_found} not in index")

KeyError: "['Digimon'] not in index"

## EXERCISE ##

import pandas as pd

# I have a dictionary that maps guitar types to their colors
guitars_dict = {
    "Fender Telecaster": "Baby Blue",
    "Gibson Les Paul": "Sunburst",
    "ESP Eclipse": "Dark Green"
}

# Create a new Series object, passing in the guitars_dict dictionary as the data source.
# Assign the resulting Series to a "guitars" variable.
guitars = pd.Series(guitars_dict)

# Access the value for the index position of 0 within the "guitars" Series.
# Assign the value to a "fender_color" variable.
fender_color = guitars[0]

# Access the value for the index label of "Gibson Les Paul" in the "guitars" Series.
# Assign the value to a "gibson_color" variable.
gibson_color = guitars["Gibson Les Paul"] 

# Access the value for the index label of "ESP Eclipse" in the "guitars" Series.
# Assign the value to a "esp_color" variable.
esp_color = guitars["ESP Eclipse"]

## The get Method on a Series ##
#################################################

#in
pokemon.head()
#out
Pokemon
Bulbasaur     Grass
Ivysaur       Grass
Venusaur      Grass
Charmander     Fire
Charmeleon     Fire
Name: Type, dtype: object

#in
pokemon.get(0)
#out
'Grass'

#in
pokemon.get("Bulbasaur")
#out
'Grass'

#in
pokemon.get([5, 10])
#out
Pokemon
Charizard    Fire
Metapod       Bug
Name: Type, dtype: object

#in
pokemon.get(["Moltres", "Meowth"])
#out
Pokemon
Moltres      Fire
Meowth     Normal
Name: Type, dtype: object

#in
pokemon["Digimon"]
#out
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexes\base.py:3802, in Index.get_loc(self, key, method, tolerance)
   3801 try:
-> 3802     return self._engine.get_loc(casted_key)
   3803 except KeyError as err:

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\_libs\index.pyx:138, in pandas._libs.index.IndexEngine.get_loc()

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\_libs\index.pyx:165, in pandas._libs.index.IndexEngine.get_loc()

File pandas\_libs\hashtable_class_helper.pxi:5745, in pandas._libs.hashtable.PyObjectHashTable.get_item()

File pandas\_libs\hashtable_class_helper.pxi:5753, in pandas._libs.hashtable.PyObjectHashTable.get_item()

KeyError: 'Digimon'

The above exception was the direct cause of the following exception:

KeyError                                  Traceback (most recent call last)
Cell In[34], line 1
----> 1 pokemon["Digimon"]

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\series.py:981, in Series.__getitem__(self, key)
    978     return self._values[key]
    980 elif key_is_scalar:
--> 981     return self._get_value(key)
    983 if is_hashable(key):
    984     # Otherwise index.get_value will raise InvalidIndexError
    985     try:
    986         # For labels that don't resolve as scalars like tuples and frozensets

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\series.py:1089, in Series._get_value(self, label, takeable)
   1086     return self._values[label]
   1088 # Similar to Index.get_value, but we do not fall back to positional
-> 1089 loc = self.index.get_loc(label)
   1090 return self.index._get_values_for_loc(self, loc, label)

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexes\base.py:3804, in Index.get_loc(self, key, method, tolerance)
   3802     return self._engine.get_loc(casted_key)
   3803 except KeyError as err:
-> 3804     raise KeyError(key) from err
   3805 except TypeError:
   3806     # If we have a listlike key, _check_indexing_error will raise
   3807     #  InvalidIndexError. Otherwise we fall through and re-raise
   3808     #  the TypeError.
   3809     self._check_indexing_error(key)

KeyError: 'Digimon'

#in
pokemon.get("Digimon")
print(pokemon.get("Digimon"))
#out
None

#in
pokemon.get("Digimon", "Nonexistent")
#out
'Nonexistent'

#in
pokemon.get("Moltres", "Nonexistent")
#out
'Fire'

#in
pokemon.get(["Moltres", "Gigimon"], "Nonexistent")
#out
'Nonexistent'

#in
pokemon.get(["Moltres", "Gigimon"])
print(pokemon.get(["Moltres", "Gigimon"]))
#out
None

## Overwrite a Series Value #

#in
import pandas as pd
pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"]).squeeze("columns")
pokemon.head()
#out
0     Bulbasaur
1       Ivysaur
2      Venusaur
3    Charmander
4    Charmeleon
Name: Pokemon, dtype: object

#in
pokemon[0]
#out
'Bulbasaur'

#in
pokemon[0] = "Borisaur"
pokemon.head()
#out
0      Borisaur
1       Ivysaur
2      Venusaur
3    Charmander
4    Charmeleon
Name: Pokemon, dtype: object

#in
pokemon[1500] = "Hello"
pokemon
#out
0         Borisaur
1          Ivysaur
2         Venusaur
3       Charmander
4       Charmeleon
           ...    
717        Zygarde
718        Diancie
719          Hoopa
720      Volcanion
1500         Hello
Name: Pokemon, Length: 722, dtype: object

#in
pokemon[[1, 2, 4]] = ["Firemon", "Flamemon", "Blazemon"]
pokemon.head()
#out
0      Borisaur
1       Firemon
2      Flamemon
3    Charmander
4      Blazemon
Name: Pokemon, dtype: object

#in
pokemon = pd.read_csv("pokemon.csv", index_col = ["Pokemon"]).squeeze("columns")
pokemon.head()
#out
Pokemon
Bulbasaur     Grass
Ivysaur       Grass
Venusaur      Grass
Charmander     Fire
Charmeleon     Fire
Name: Type, dtype: object

#in
pokemon["Bulbasaur" = "Awesomemon"]
#out
 Cell In[15], line 1
    pokemon["Bulbasaur" = "Awesomemon"]
            ^
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

#in
pokemon["Bulbasaur"] = "Awesomemon"
pokemon.head()
#out
Pokemon
Bulbasaur     Awesomemon
Ivysaur            Grass
Venusaur           Grass
Charmander          Fire
Charmeleon          Fire
Name: Type, dtype: object

#in
pokemon[1] = "Grassmon"
pokemon.head()
#out
Pokemon
Bulbasaur     Awesomemon
Ivysaur         Grassmon
Venusaur           Grass
Charmander          Fire
Charmeleon          Fire
Name: Type, dtype: object

## The copy Method ##

#in
pokemon_df = pd.read_csv("pokemon.csv", usecols = ["Pokemon"])
pokemon_df
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
pokemon_series = pokemon_df.squeeze("columns")
pokemon_series
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
pokemon_series[0] = "Whatever" ##creates the ripple affect as below to be aware of
pokemon_series.head(1)
#out
0    Whatever
Name: Pokemon, dtype: object

#in
pokemon_df
#out
Pokemon
0	Whatever
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

# Big House (DataFrame)
#  Door (Series)
#   ^ change to the dorr will affect the Big House
# Therefore a copy needs to be made

#in
pokemon_df = pd.read_csv("pokemon.csv", usecols = ["Pokemon"])
pokemon_series = pokemon_df.squeeze("columns").copy()
pokemon_series[0] = "Whatever"
pokemon_series.head(1)
#out
0    Whatever
Name: Pokemon, dtype: object

#in
pokemon_df
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

## The inplace Parameter ##

#in
pd.read_csv("google_stock_price.csv", usecols = ["Stock Price"]).squeeze("columns")
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

#in
pd.read_csv("google_stock_price.csv", usecols = ["Stock Price"]).squeeze("columns").copy()
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

#in
google = (
    pd.read_csv("google_stock_price.csv", usecols = ["Stock Price"])
    .squeeze("columns")
    .copy()
)
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

#in
google.sort_values()
#out
11       49.95
9        50.07
0        50.12
10       50.70
12       50.74
         ...  
3010    771.61
3007    772.88
3009    773.18
2859    776.60
3011    782.22
Name: Stock Price, Length: 3012, dtype: float64

#in
google = google.sort_values()
google.head()
#out
11    49.95
9     50.07
0     50.12
10    50.70
12    50.74
Name: Stock Price, dtype: float64

#in
google = (
    pd.read_csv("google_stock_price.csv", usecols = ["Stock Price"])
    .squeeze("columns")
    .copy()
)
google.head()
#out
0    50.12
1    54.10
2    54.65
3    52.38
4    52.95
Name: Stock Price, dtype: float64

#in
google.sort_values()
#out
11       49.95
9        50.07
0        50.12
10       50.70
12       50.74
         ...  
3010    771.61
3007    772.88
3009    773.18
2859    776.60
3011    782.22
Name: Stock Price, Length: 3012, dtype: float64

#in
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

#in
import pandas as pd
google = (
    pd.read_csv("google_stock_price.csv", usecols = ["Stock Price"])
    .squeeze("columns")
    .copy()
)
google.sort_values(inplace = True)
google
#out
11       49.95
9        50.07
0        50.12
10       50.70
12       50.74
         ...  
3010    771.61
3007    772.88
3009    773.18
2859    776.60
3011    782.22
Name: Stock Price, Length: 3012, dtype: float64

#in
google.sort_index()
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

#in
google
#out
11       49.95
9        50.07
0        50.12
10       50.70
12       50.74
         ...  
3010    771.61
3007    772.88
3009    773.18
2859    776.60
3011    782.22
Name: Stock Price, Length: 3012, dtype: float64

#in
google.sort_index(inplace = True)
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

#in
google = (
    pd.read_csv("google_stock_price.csv", usecols = ["Stock Price"])
    .squeeze("columns")

)
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

#in
google.sort_values()
#out
11       49.95
9        50.07
0        50.12
10       50.70
12       50.74
         ...  
3010    771.61
3007    772.88
3009    773.18
2859    776.60
3011    782.22
Name: Stock Price, Length: 3012, dtype: float64

#in
google.sort_values(inplace = True)
#out
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[15], line 1
----> 1 google.sort_values(inplace = True)

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\util\_decorators.py:331, in deprecate_nonkeyword_arguments.<locals>.decorate.<locals>.wrapper(*args, **kwargs)
    325 if len(args) > num_allow_args:
    326     warnings.warn(
    327         msg.format(arguments=_format_argument_list(allow_args)),
    328         FutureWarning,
    329         stacklevel=find_stack_level(),
    330     )
--> 331 return func(*args, **kwargs)

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\series.py:3748, in Series.sort_values(self, axis, ascending, inplace, kind, na_position, ignore_index, key)
   3746 # GH 5856/5853
   3747 if inplace and self._is_cached:
-> 3748     raise ValueError(
   3749         "This Series is a view of some other array, to "
   3750         "sort in-place you must create a copy"
   3751     )
   3753 if is_list_like(ascending):
   3754     ascending = cast(Sequence[Union[bool, int]], ascending)

ValueError: This Series is a view of some other array, to sort in-place you must create a copy

#in
google2 = google.copy()
google2.sort_values(inplace = True)
google2
#out
11       49.95
9        50.07
0        50.12
10       50.70
12       50.74
         ...  
3010    771.61
3007    772.88
3009    773.18
2859    776.60
3011    782.22
Name: Stock Price, Length: 3012, dtype: float64

## Math Methods on Series Objects ##





## EXERCISE ##

##
#################################################

## EXERCISE ##



