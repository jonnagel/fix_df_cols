from pandas import Index as pd_Index
from string import ascii_lowercase, digits
import pandas as pd


class FixCols:
    def __init__(self, object):
        self.columns_clean = []
        self.columns_raw = None
        self.object = object
        self.df = None
        self.type = None
        self.seperator = '_'
        self.seperator_target = [' ']
        self.valid = list(ascii_lowercase) + list(digits) + ['_']
        if isinstance(object, list):
            self.columns_raw = object
            self.type = 'list'
            for col in self.object:
                self.columns_clean.append(self.clean(col))
        if isinstance(object, pd_Index):
            self.type = 'pd.Index'
            self.columns_raw = object
            pdi = []
            for col in self.object:
                pdi.append(self.clean(col))
            self.columns_clean = pd.Index(pdi)
        if isinstance(object, pd.DataFrame):
            self.type = 'pd.DataFrame'
            self.columns_raw = self.object.columns
            pdi = []
            for col in self.object.columns:
                pdi.append(self.clean(col))
            self.columns_clean = pd.Index(pdi)
            self.object.columns = self.columns_clean
            self.df = self.object.copy()

    def clean(self, s: str):
        s = s.lower()
        for target in self.seperator_target:
            s = [c for c in s.replace(target, self.seperator) if c in self.valid]
        return(''.join(s).replace(self.seperator+self.seperator, self.seperator))

    def __str__(self):
        return(f"{self.columns_clean}")

    def __repr__(self):
        return(f"FixCols({self.columns_raw})")


@pd.api.extensions.register_dataframe_accessor("clean")
class CleanDF():
    """
    """
    def __init__(self, pandas_obj):
        pandas_obj.columns = FixCols(pandas_obj.columns).columns_clean
        self._obj = pandas_obj
    def __call__(self):
        # allow for look of method call AKA w/ parentheses 
        pass


