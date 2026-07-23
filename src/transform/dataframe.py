import pandas as pd

from src.filters.job_filter import MatchResult
from src.models.job import Job


OUTPUT_COLUMNS = [
    "title", "company", "location", "work_model", "source", "url",
    "technologies", "match_score", "matched_keywords", "published_at",
]


def to_dataframe(data: list[Job] | list[MatchResult]) -> pd.DataFrame:
    """Converte vagas ou resultados de compatibilidade em DataFrame."""
    rows = []
    for item in data:
        if isinstance(item, MatchResult):
            row = item.job.__dict__.copy()
            row["match_score"] = item.match_score
            row["matched_keywords"] = ", ".join(item.matched_keywords)
        else:
            row = item.__dict__.copy()

        row["technologies"] = ", ".join(row.get("technologies") or [])
        row.pop("description", None)
        rows.append(row)

    columns = OUTPUT_COLUMNS if data and isinstance(data[0], MatchResult) else None
    return pd.DataFrame(rows, columns=columns)


def remove_duplicates(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    """Remove duplicados por URL e, como alternativa, pelos dados principais."""
    if df.empty:
        return df, 0

    original_count = len(df)
    result = df.drop_duplicates(subset=["url"], keep="first")
    result = result.drop_duplicates(
        subset=["title", "company", "location"], keep="first"
    )
    return result, original_count - len(result)


def sort_jobs(df: pd.DataFrame) -> pd.DataFrame:
    """Ordena vagas por compatibilidade e data de publicação."""
    if df.empty:
        return df

    result = df.copy()
    result["_published_at"] = pd.to_datetime(
        result["published_at"], errors="coerce", utc=True
    )
    result = result.sort_values(
        by=["match_score", "_published_at"],
        ascending=[False, False],
        na_position="last",
    )
    return result.drop(columns=["_published_at"]).reset_index(drop=True)
