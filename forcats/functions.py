import pandas as pd

def cat_lump(x, n=5, prop=None, other_level="Other"):
    """
    Lump together least common categories into an "Other" category
    
    Parameters
    ----------
    x : pd.Series
      series to be modified
    n : int
      number of levels to preserve
    prop : float
      optional instead of n. Choose the minimum proportion for a level.
      Must be between 0 and 1. Overrides n.
    other_level : str
      "other" category label
      
    Returns
    -------
    y : pd.Series
      modified series (with categorical type)
    """
    counts = x.value_counts()
    if prop:
        assert 0 <= prop <= 1
        min_count = int(prop * x.size)
        if min_count > counts.min():
            repl = counts.loc[counts<min_count].index
            x = x.replace(repl, other_level)
    elif len(counts) > n:
        repl = counts.iloc[n:].index
        x = x.replace(repl, other_level)
    return x



def cat_count(x, sort = False, prop = False):
    """
    Count entries in a factor
    
    Parameters
    ----------
    x : pd.Series
      series to be counted      
    sort : boolean
      If `True`, sort the result so that the most common values are displayed at the top.
    prop : boolean
      If `True`, compute the fraction of marginal table.
      
    Returns
    -------
    y : pd.core.frame.DataFrame
      A df with columns `f`, `n` and `p`, if prop is `True`.
    """

    
    counts = x.value_counts(sort = sort)
    df = pd.DataFrame({'f':counts.index, 'n':counts.values})
    
    if(prop):    
        df['p'] = df['n']/sum(df['n'])
    
    return df
        
