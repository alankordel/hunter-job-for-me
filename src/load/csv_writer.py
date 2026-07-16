import pandas as pd


def save_csv(df: pd.DataFrame, path: str):
    """
    Salva um DataFrame em arquivo CSV.
    """

    df.to_csv(
        path,
        index=False,
        encoding="utf-8"
    )