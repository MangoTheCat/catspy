import pandas as pd

from forcats.functions import cat_count

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

def test_cat_count_on_string_column(data):
    result = (cat_count(data.A, sort=False)
        .set_index('f')
        .sort_index()
        .rename_axis(None)
    )
    
    target = pd.DataFrame({
        'n': {'a': 4, 'b': 3, 'c': 2, 'd': 1}
    })
    
    pd.testing.assert_frame_equal(result, target)


def test_cat_count_on_string_column_sort(data):

    result = cat_count(data.A, sort = True)

    target = pd.DataFrame({
        'f': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'n': {0: 4, 1: 3, 2: 2, 3: 1},
        })
    pd.testing.assert_frame_equal(result, target)


def test_cat_count_on_categorical_column(data):

    result = cat_count(data.B, prop = True)
    
    target = pd.DataFrame({
        'f': pd.Categorical(['a', 'b', 'c', 'd']),
        'n': [4, 3, 2, 1],
        'p': [0.4, 0.3, 0.2, 0.1]
        })
    
    pd.testing.assert_frame_equal(result, target)

def test_cat_count_on_categorical_column_sort(data):

    result = cat_count(data.B, sort = True)
    
    target = pd.DataFrame({
        'f': pd.Categorical(['a', 'b', 'c', 'd']),
        'n': [4, 3, 2, 1]
        })
    pd.testing.assert_frame_equal(result, target)