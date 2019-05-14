import pandas as pd

from catspy.functions import cat_anon

import pytest


@pytest.fixture()
def data():

    # First column is as strings, second is as pandas categorical data type,
	# third is a ten-level string series
    df = pd.DataFrame(
        {
            "A": ["a", "a", "a", "a", "b", "b", "b", "c", "c", "d"],
            "B": pd.Categorical(["a", "a", "a", "a", "b", "b", "b", "c", "c", "d"]),
            "C": list('abcdefghij')
        }
    )
    return df


def test_cat_anon_on_string_column(data):

    result = cat_anon(data.A)

    target = ['1', '1', '1', '1', '2', '2', '2', '3', '3', '4']
    assert result.tolist() == target

    result_pre = cat_anon(data.A, 'Person_')

    target = ['Person_1', 'Person_1', 'Person_1', 'Person_1', 
              'Person_2', 'Person_2', 'Person_2', 'Person_3', 
              'Person_3', 'Person_4']
    assert result_pre.tolist() == target


def test_cat_anon_on_categorical_column(data):

    result = cat_anon(data.B)

    target = ['1', '1', '1', '1', '2', '2', '2', '3', '3', '4']
    assert result.tolist() == target

    result_pre = cat_anon(data.B, 'Country_')

    target = ['Country_1', 'Country_1', 'Country_1', 'Country_1', 
              'Country_2', 'Country_2', 'Country_2', 'Country_3', 
              'Country_3', 'Country_4']
    assert result_pre.tolist() == target


def test_cat_anon_on_10_level_column(data):

    result = cat_anon(data.C)

    target = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
    assert result.tolist() == target

    result_pre = cat_anon(data.C, 'Religion_')

    target = ['Religion_01', 'Religion_02', 'Religion_03', 'Religion_04', 
              'Religion_05', 'Religion_06', 'Religion_07', 'Religion_08', 
              'Religion_09', 'Religion_10']
    assert result_pre.tolist() == target
