def cat_lump(x, n = 5, other_level = "Other"):
    counts = x.value_counts()
    if (len(counts) > n):
        repl = counts.iloc[n:].index
        x = x.replace(repl, other_level)
    return(x)
