#functions to be used in the data preparation process

import pandas as pd
import numpy as np

def market_columns(df):
    """Function that maps multiple entries in a column into individual columns
    and assings a score of 1 or 0 if the entry is question is within a given row.
    """
    categories = []
    for category in list(df['Market Category'].unique()):
        categories += category.split(',')

    unique = set(categories)
    for col in unique:
        df[col] = df['Market Category'].apply(lambda x: 1 if col in x.split(',') else 0)
    df.drop('Market Category', axis=1, inplace=True)
    return df
