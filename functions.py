#functions to be used in the data preparation process

import pandas as pd
import numpy as np

def split_market_categories(df):
    """Function that splits each car's market category into a single list
    containing all market categories."""
    categories = []
    for category in df['Market Category']:
        categories += category.split(',')
    return categories

def market_columns(df):
    """Function that maps multiple entries in a column into individual columns
    and assings a score of 1 or 0 if the entry is question is within a given row.
    """
    unique = set(split_market_category(df))
    for col in unique:
        df[col] = df['Market Category'].apply(lambda x: 1 if col in x.split(',') else 0)
    df.drop('Market Category', axis=1, inplace=True)
    return df