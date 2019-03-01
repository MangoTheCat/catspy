def cat_lump(x, n=5, other_level="Other"):
    """
    Lump together least common categories into an "Other" category
    
    Parameters
    ----------
    x : pd.Series
      series to be modified
    n : int
      number of levels to preserve
    other_level : str
      "other" category label
      
    Returns
    -------
    y : pd.Series
      modified series (with categorical type)
    """
    counts = x.value_counts()
    if len(counts) > n:
        repl = counts.iloc[n:].index
        x = x.replace(repl, other_level)
    return x
