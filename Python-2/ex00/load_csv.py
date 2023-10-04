import pandas as pd


def load(path: str):
    """function that reads the csv file, prints the shape,
and return the dataset"""
    assert type(path) is str, "path is not str"
    df = pd.read_csv(path, index_col=0)
    print("Loading dataset of dimensions", df.shape)
    return df
