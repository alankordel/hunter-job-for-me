from src.filters.job_filter import score_job
from src.models.job import Job


def test_score_compatible_job():
    job = Job(
        title="Data Analyst",
        url="https://example.com/job/1",
        location="Brazil",
        work_model="Remote",
        description="Python e SQL",
    )
    result = score_job(job)
    assert result.match_score == 9
    assert "data analyst" in result.matched_keywords


def test_penalize_senior_job():
    junior = Job(title="Python Developer", url="https://example.com/job/1")
    senior = Job(title="Senior Python Developer", url="https://example.com/job/2")
    assert score_job(senior).match_score == score_job(junior).match_score - 3
