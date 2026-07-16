import pandas as pd


def to_dataframe(data):

    rows = [
        job.__dict__
        for job in data
    ]

    return pd.DataFrame(rows)