# fix_df_cols

I dislike columns with names that slow my work. This package will convert all columns names to [snake_case](https://en.wikipedia.org/wiki/Snake_case), using the following rules:

1. Everything (all columns) are converted to lowercase.
2. All spaces are replaces with underscores.
3. Everything that isn't a letter, digit, or underscore (in a column name) is removed.

## Installation

TODO

## Usage

Create a pd.DataFrame as normal, then run clean() method to fix the column
names. This adds a clean() method to all pd.DataFrames, calling this method
fixes the columns in place.
```python
from src.fixdfcols import CleanDF
bad_df = pd.DataFrame(columns=['abc -@#ab%@', '12 3', 'a**bcCCC'])
# bad_df.columns
#   Index(['abc -@#ab%@', '12 3', 'a**bc'], dtype='object')
bad_df.clean()
# bad_df.columns
#   Index(['abc_ab', '12_3', 'abc'], dtype='object')
```
Standalone example
```python
# a python list or pd.Index works as a manual fix 
from src.fixdfcols import FixCols
clean_cols = FixCols(['abc -@#ab%@', '12 3', 'a**bcEB']).columns_clean
# clean_cols
# ['abc_ab', '12_3', 'abceb']
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
