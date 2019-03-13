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
