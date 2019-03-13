import pandas as pd

from forcats.functions import cat_lump

import pytest


@pytest.fixture()
def data():

    # First column is as strings, second is as pandas categorical data type
    df = pd.DataFrame(
        {
            "A": ["a", "a", "a", "a", "b", "b", "b", "c", "c", "d"],
            "B": pd.Categorical(["a", "a", "a", "a", "b", "b", "b", "c", "c", "d"]),
        }
    )
    return df


def test_cat_lump_on_string_column(data):

    result = cat_lump(data.A, n=2)

    target = ["a", "a", "a", "a", "b", "b", "b", "Other", "Other", "Other"]
    assert result.tolist() == target


def test_cat_lump_on_categorical_column(data):

    result = cat_lump(data.B, n=2)

    target = ["a", "a", "a", "a", "b", "b", "b", "Other", "Other", "Other"]
    assert result.tolist() == target

def test_cat_lump_with_prop(data):

    result_hi = cat_lump(data.B, prop=0.3)

    target = ["a", "a", "a", "a", "b", "b", "b", "Other", "Other", "Other"]
    assert result_hi.tolist() == target

    result_lo = cat_lump(data.B, prop=0.1)

    target = ["a", "a", "a", "a", "b", "b", "b", "c", "c", "d"]
    assert result_lo.tolist() == target
