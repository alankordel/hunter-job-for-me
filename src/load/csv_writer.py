from pathlib import Path

import pandas as pd


def save_csv(df: pd.DataFrame, path: str) -> Path:
    """Salva um DataFrame em CSV compatível com Excel no Windows."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    return output_path.resolve()
