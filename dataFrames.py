## dataFrames ##

#in
import pandas as pd
pd.read_csv("nba.csv")
#out
Name	Team	Number	Position	Age	Height	Weight	College	Salary
0	Avery Bradley	Boston Celtics	0.0	PG	25.0	6-2	180.0	Texas	7730337.0
1	Jae Crowder	Boston Celtics	99.0	SF	25.0	6-6	235.0	Marquette	6796117.0
2	John Holland	Boston Celtics	30.0	SG	27.0	6-5	205.0	Boston University	NaN
3	R.J. Hunter	Boston Celtics	28.0	SG	22.0	6-5	185.0	Georgia State	1148640.0
4	Jonas Jerebko	Boston Celtics	8.0	PF	29.0	6-10	231.0	NaN	5000000.0
...	...	...	...	...	...	...	...	...	...
453	Shelvin Mack	Utah Jazz	8.0	PG	26.0	6-3	203.0	Butler	2433333.0
454	Raul Neto	Utah Jazz	25.0	PG	24.0	6-1	179.0	NaN	900000.0
455	Tibor Pleiss	Utah Jazz	21.0	C	26.0	7-3	256.0	NaN	2900000.0
456	Jeff Withey	Utah Jazz	24.0	C	26.0	7-0	231.0	Kansas	947276.0
457	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
458 rows × 9 columns

#in
nba = pd.read_csv("nba.csv")
nba
#out
Name	Team	Number	Position	Age	Height	Weight	College	Salary
0	Avery Bradley	Boston Celtics	0.0	PG	25.0	6-2	180.0	Texas	7730337.0
1	Jae Crowder	Boston Celtics	99.0	SF	25.0	6-6	235.0	Marquette	6796117.0
2	John Holland	Boston Celtics	30.0	SG	27.0	6-5	205.0	Boston University	NaN
3	R.J. Hunter	Boston Celtics	28.0	SG	22.0	6-5	185.0	Georgia State	1148640.0
4	Jonas Jerebko	Boston Celtics	8.0	PF	29.0	6-10	231.0	NaN	5000000.0
...	...	...	...	...	...	...	...	...	...
453	Shelvin Mack	Utah Jazz	8.0	PG	26.0	6-3	203.0	Butler	2433333.0
454	Raul Neto	Utah Jazz	25.0	PG	24.0	6-1	179.0	NaN	900000.0
455	Tibor Pleiss	Utah Jazz	21.0	C	26.0	7-3	256.0	NaN	2900000.0
456	Jeff Withey	Utah Jazz	24.0	C	26.0	7-0	231.0	Kansas	947276.0
457	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
458 rows × 9 columns

## Methods and Attributes between Series and DataFrames ##

#in
s = pd.Series([1, 2, 3, 4, 5])
s
#out
0    1
1    2
2    3
3    4
4    5
dtype: int64

#in
nba.head()
nba.head(n = 5)
#out
Name	Team	Number	Position	Age	Height	Weight	College	Salary
0	Avery Bradley	Boston Celtics	0.0	PG	25.0	6-2	180.0	Texas	7730337.0
1	Jae Crowder	Boston Celtics	99.0	SF	25.0	6-6	235.0	Marquette	6796117.0
2	John Holland	Boston Celtics	30.0	SG	27.0	6-5	205.0	Boston University	NaN
3	R.J. Hunter	Boston Celtics	28.0	SG	22.0	6-5	185.0	Georgia State	1148640.0
4	Jonas Jerebko	Boston Celtics	8.0	PF	29.0	6-10	231.0	NaN	5000000.0

#in
nba.head(8)
#out
Name	Team	Number	Position	Age	Height	Weight	College	Salary
0	Avery Bradley	Boston Celtics	0.0	PG	25.0	6-2	180.0	Texas	7730337.0
1	Jae Crowder	Boston Celtics	99.0	SF	25.0	6-6	235.0	Marquette	6796117.0
2	John Holland	Boston Celtics	30.0	SG	27.0	6-5	205.0	Boston University	NaN
3	R.J. Hunter	Boston Celtics	28.0	SG	22.0	6-5	185.0	Georgia State	1148640.0
4	Jonas Jerebko	Boston Celtics	8.0	PF	29.0	6-10	231.0	NaN	5000000.0
5	Amir Johnson	Boston Celtics	90.0	PF	29.0	6-9	240.0	NaN	12000000.0
6	Jordan Mickey	Boston Celtics	55.0	PF	21.0	6-8	235.0	LSU	1170960.0
7	Kelly Olynyk	Boston Celtics	41.0	C	25.0	7-0	238.0	Gonzaga	2165160.0

#in
nba.tail()
nba.tail(5)
#out
Name	Team	Number	Position	Age	Height	Weight	College	Salary
453	Shelvin Mack	Utah Jazz	8.0	PG	26.0	6-3	203.0	Butler	2433333.0
454	Raul Neto	Utah Jazz	25.0	PG	24.0	6-1	179.0	NaN	900000.0
455	Tibor Pleiss	Utah Jazz	21.0	C	26.0	7-3	256.0	NaN	2900000.0
456	Jeff Withey	Utah Jazz	24.0	C	26.0	7-0	231.0	Kansas	947276.0
457	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN

#in
nba.tail(1)
#out
Name	Team	Number	Position	Age	Height	Weight	College	Salary
457	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN

#in
s.index
#out
RangeIndex(start=0, stop=5, step=1)

#in
nba.index
#out
RangeIndex(start=0, stop=458, step=1)

#in
s.values
#out
array([1, 2, 3, 4, 5], dtype=int64)

#in
nba.values
#out
array([['Avery Bradley', 'Boston Celtics', 0.0, ..., 180.0, 'Texas',
        7730337.0],
       ['Jae Crowder', 'Boston Celtics', 99.0, ..., 235.0, 'Marquette',
        6796117.0],
       ['John Holland', 'Boston Celtics', 30.0, ..., 205.0,
        'Boston University', nan],
       ...,
       ['Tibor Pleiss', 'Utah Jazz', 21.0, ..., 256.0, nan, 2900000.0],
       ['Jeff Withey', 'Utah Jazz', 24.0, ..., 231.0, 'Kansas', 947276.0],
       [nan, nan, nan, ..., nan, nan, nan]], dtype=object)

#in
s.shape
#out
(5,)

#in
nba.shape
#out
(458, 9)

#in
s
#out
0    1
1    2
2    3
3    4
4    5
dtype: int64

#in
s.dtype
#out
dtype('int64')

#in
s.dtypes
#out
dtype('int64')

#in
nba.dtypes
#out
Name         object
Team         object
Number      float64
Position     object
Age         float64
Height       object
Weight      float64
College      object
Salary      float64
dtype: object
#in
s.hasnans
#out
False

#in
nab.hasnans
#out
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[23], line 1
----> 1 nab.hasnans

NameError: name 'nab' is not defined

#in
nba.hasnans
#out
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[24], line 1
----> 1 nba.hasnans

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\generic.py:5902, in NDFrame.__getattr__(self, name)
   5895 if (
   5896     name not in self._internal_names_set
   5897     and name not in self._metadata
   5898     and name not in self._accessors
   5899     and self._info_axis._can_hold_identifiers_and_holds_name(name)
   5900 ):
   5901     return self[name]
-> 5902 return object.__getattribute__(self, name)

AttributeError: 'DataFrame' object has no attribute 'hasnans'

#in
nba.columns
#out
Index(['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight',
       'College', 'Salary'],
      dtype='object')

#in
s.columns
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[27], line 1
----> 1 s.columns

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\generic.py:5902, in NDFrame.__getattr__(self, name)
   5895 if (
   5896     name not in self._internal_names_set
   5897     and name not in self._metadata
   5898     and name not in self._accessors
   5899     and self._info_axis._can_hold_identifiers_and_holds_name(name)
   5900 ):
   5901     return self[name]
-> 5902 return object.__getattribute__(self, name)

AttributeError: 'Series' object has no attribute 'columns'

#in
s.axes
#out
[RangeIndex(start=0, stop=5, step=1)]

#in
nba.axes
#out
[RangeIndex(start=0, stop=458, step=1),
 Index(['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight',
        'College', 'Salary'],
       dtype='object')]

#in
s.info()
#out
<class 'pandas.core.series.Series'>
RangeIndex: 5 entries, 0 to 4
Series name: None
Non-Null Count  Dtype
--------------  -----
5 non-null      int64
dtypes: int64(1)
memory usage: 172.0 bytes
nba.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 458 entries, 0 to 457
Data columns (total 9 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Name      457 non-null    object 
 1   Team      457 non-null    object 
 2   Number    457 non-null    float64
 3   Position  457 non-null    object 
 4   Age       457 non-null    float64
 5   Height    457 non-null    object 
 6   Weight    457 non-null    float64
 7   College   373 non-null    object 
 8   Salary    446 non-null    float64
dtypes: float64(4), object(5)
memory usage: 32.3+ KB

## Differences between Shared Methods ##

#in
pd.read_csv("revenue.csv")
#out
Date	New York	Los Angeles	Miami
0	1/1/16	985	122	499
1	1/2/16	738	788	534
2	1/3/16	14	20	933
3	1/4/16	730	904	885
4	1/5/16	114	71	253
5	1/6/16	936	502	497
6	1/7/16	123	996	115
7	1/8/16	935	492	886
8	1/9/16	846	954	823
9	1/10/16	54	285	216

#in
revenue = pd.read_csv("revenue.csv", index_col = "Date")
revenue
#out
New York	Los Angeles	Miami
Date			
1/1/16	985	122	499
1/2/16	738	788	534
1/3/16	14	20	933
1/4/16	730	904	885
1/5/16	114	71	253
1/6/16	936	502	497
1/7/16	123	996	115
1/8/16	935	492	886
1/9/16	846	954	823
1/10/16	54	285	216

#in
s = pd.Series([1, 2, 3])
s
#out
0    1
1    2
2    3
dtype: int64

#in
s.sum()
#out
6

#in
revenue.sum()
#out
New York       5475
Los Angeles    5134
Miami          5641
dtype: int64

#in
revenue.sum(axis = "columns")
#or
revenue.sum(axis = 1)
#out
Date
1/1/16     1606
1/2/16     2060
1/3/16      967
1/4/16     2519
1/5/16      438
1/6/16     1935
1/7/16     1234
1/8/16     2313
1/9/16     2623
1/10/16     555
dtype: int64

#in
revenue.sum()
revenue.sum(axis = "index")
revenue.sum(axis = 0)
#out
New York       5475
Los Angeles    5134
Miami          5641
dtype: int64

## Select One Column from a DataFrame ##

#in
import pandas as pd
nba = pd.read_csv("nba.csv")
nba.head()
#out
Name	Team	Number	Position	Age	Height	Weight	College	Salary
0	Avery Bradley	Boston Celtics	0.0	PG	25.0	6-2	180.0	Texas	7730337.0
1	Jae Crowder	Boston Celtics	99.0	SF	25.0	6-6	235.0	Marquette	6796117.0
2	John Holland	Boston Celtics	30.0	SG	27.0	6-5	205.0	Boston University	NaN
3	R.J. Hunter	Boston Celtics	28.0	SG	22.0	6-5	185.0	Georgia State	1148640.0
4	Jonas Jerebko	Boston Celtics	8.0	PF	29.0	6-10	231.0	NaN	5000000.0

#in
nba.Name
#out
0      Avery Bradley
1        Jae Crowder
2       John Holland
3        R.J. Hunter
4      Jonas Jerebko
           ...      
453     Shelvin Mack
454        Raul Neto
455     Tibor Pleiss
456      Jeff Withey
457              NaN
Name: Name, Length: 458, dtype: object

#in
type(nba.Name)
#out
pandas.core.series.Series

#in
nba.Number
#out
0       0.0
1      99.0
2      30.0
3      28.0
4       8.0
       ... 
453     8.0
454    25.0
455    21.0
456    24.0
457     NaN
Name: Number, Length: 458, dtype: float64

#in
nba.Salary
#out
0      7730337.0
1      6796117.0
2            NaN
3      1148640.0
4      5000000.0
         ...    
453    2433333.0
454     900000.0
455    2900000.0
456     947276.0
457          NaN
Name: Salary, Length: 458, dtype: float64

#in
nba.First Name
#out
  Cell In[7], line 1
    nba.First Name
              ^
SyntaxError: invalid syntax


#in
nba["Name"]
#out
0      Avery Bradley
1        Jae Crowder
2       John Holland
3        R.J. Hunter
4      Jonas Jerebko
           ...      
453     Shelvin Mack
454        Raul Neto
455     Tibor Pleiss
456      Jeff Withey
457              NaN
Name: Name, Length: 458, dtype: object

#in
nba["Number"]
#out
0       0.0
1      99.0
2      30.0
3      28.0
4       8.0
       ... 
453     8.0
454    25.0
455    21.0
456    24.0
457     NaN
Name: Number, Length: 458, dtype: float64

#in
nba["number"]
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

KeyError: 'number'

The above exception was the direct cause of the following exception:

KeyError                                  Traceback (most recent call last)
Cell In[10], line 1
----> 1 nba["number"]

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\frame.py:3807, in DataFrame.__getitem__(self, key)
   3805 if self.columns.nlevels > 1:
   3806     return self._getitem_multilevel(key)
-> 3807 indexer = self.columns.get_loc(key)
   3808 if is_integer(indexer):
   3809     indexer = [indexer]

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexes\base.py:3804, in Index.get_loc(self, key, method, tolerance)
   3802     return self._engine.get_loc(casted_key)
   3803 except KeyError as err:
-> 3804     raise KeyError(key) from err
   3805 except TypeError:
   3806     # If we have a listlike key, _check_indexing_error will raise
   3807     #  InvalidIndexError. Otherwise we fall through and re-raise
   3808     #  the TypeError.
   3809     self._check_indexing_error(key)

KeyError: 'number'

#in
nba["First Name"]
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

KeyError: 'First Name'

The above exception was the direct cause of the following exception:

KeyError                                  Traceback (most recent call last)
Cell In[11], line 1
----> 1 nba["First Name"]

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\frame.py:3807, in DataFrame.__getitem__(self, key)
   3805 if self.columns.nlevels > 1:
   3806     return self._getitem_multilevel(key)
-> 3807 indexer = self.columns.get_loc(key)
   3808 if is_integer(indexer):
   3809     indexer = [indexer]

File ~\anaconda3\envs\pandas_playground\Lib\site-packages\pandas\core\indexes\base.py:3804, in Index.get_loc(self, key, method, tolerance)
   3802     return self._engine.get_loc(casted_key)
   3803 except KeyError as err:
-> 3804     raise KeyError(key) from err
   3805 except TypeError:
   3806     # If we have a listlike key, _check_indexing_error will raise
   3807     #  InvalidIndexError. Otherwise we fall through and re-raise
   3808     #  the TypeError.
   3809     self._check_indexing_error(key)

KeyError: 'First Name'

#in
nba["Salary"].head().values
#out
array([7730337., 6796117.,      nan, 1148640., 5000000.])

## Exercise ##
# If you see a test failure when checking your solution,
# note that [left] refers to YOUR code while [right]
# refers to the correct code that the computer is comparing
# to your work
import pandas as pd 

# This challenge includes a cruise_ships.csv with 4 columns: 
# Name, Operator, Year, and Tonnage
# Import the cruise_ships.csv DataFrame and assign it to
# a cruise_ships variable
cruise_ships = pd.read_csv("cruise_ships.csv")

# Extract the "Operator" column from the DataFrame
# and assign it to an "operators" variable.
operators = cruise_ships["Operator"]
​
# Extract the "Tonnage" column from the DataFrame
# and assign it to an "tonnages" variable.
tonnages = cruise_ships["Tonnage"]
​
# Extract the "Name" column from the DataFrame
# and assign it to an "cruise_names" variable.
cruise_names = cruise_ships["Name"]