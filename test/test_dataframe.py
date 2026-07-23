from src.filters.job_filter import MatchResult
from src.models.job import Job
from src.transform.dataframe import remove_duplicates, to_dataframe


def test_remove_duplicates_by_url():
    jobs = [
        MatchResult(Job("Data Analyst", "https://example.com/1"), 5, ["sql"]),
        MatchResult(Job("Outra vaga", "https://example.com/1"), 4, ["python"]),
    ]
    dataframe, removed = remove_duplicates(to_dataframe(jobs))
    assert len(dataframe) == 1
    assert removed == 1


def test_convert_to_dataframe():
    result = MatchResult(
        Job(
            title="Data Engineer",
            url="https://example.com/1",
            technologies=["Python", "SQL"],
        ),
        match_score=8,
        matched_keywords=["data engineer", "python"],
    )
    dataframe = to_dataframe([result])
    assert dataframe.loc[0, "technologies"] == "Python, SQL"
    assert dataframe.loc[0, "match_score"] == 8
    assert "description" not in dataframe.columns
