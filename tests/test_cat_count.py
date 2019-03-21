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

   result = cat_count(data.A, sort = False)

   target = pd.DataFrame({
       'f': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
       'n': {0: 4, 1: 3, 2: 2, 3: 1},
       })
   assert result.f.tolist() == target.f.tolist()

def test_cat_count_on_string_column(data):

    result = cat_count(data.A, sort = True)

    target = pd.DataFrame({
        'f': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'n': {0: 4, 1: 3, 2: 2, 3: 1},
        })
    assert result.f.tolist() == target.f.tolist()
    assert result.n.tolist() == target.n.tolist()

def test_cat_count_on_categorical_column(data):

    result = cat_count(data.B, prop = True)

    target = pd.DataFrame({
        'f': {0: 'a', 1: 'b', 2: 'c', 3: 'd'},
        'n': {0: 4, 1: 3, 2: 2, 3: 1},
        'p': {0: 0.4, 1: 0.3, 2: 0.2, 3: 0.1}
        })
    assert result.f.tolist() == target.f.tolist()
    assert result.n.tolist() == target.n.tolist()
    assert result.p.tolist() == target.p.tolist()
