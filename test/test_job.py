import pytest

from src.models.job import Job


def test_create_valid_job():
    job = Job(title="Data Analyst", url="https://example.com/job/1")
    assert job.title == "Data Analyst"
    assert job.technologies == []


@pytest.mark.parametrize(
    ("title", "url"),
    [
        ("", "https://example.com/job/1"),
        ("Data Analyst", ""),
        (None, "https://example.com/job/1"),
    ],
)
def test_reject_invalid_job(title, url):
    with pytest.raises(ValueError):
        Job(title=title, url=url)
