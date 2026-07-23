from bs4 import BeautifulSoup

from src.extract.http_client import fetch_json
from src.models.job import Job
from src.sources.base import JobSource


class RemotiveSource(JobSource):
    """Coleta vagas remotas pela API pública da Remotive."""

    URL = "https://remotive.com/api/remote-jobs"
    name = "Remotive"

    def __init__(self) -> None:
        self.invalid_count = 0

    def get_jobs(self) -> list[Job]:
        payload = fetch_json(self.URL)
        records = payload.get("jobs")

        if not isinstance(records, list):
            raise ValueError("A Remotive retornou dados em formato inesperado")

        jobs = []
        for record in records:
            try:
                jobs.append(self._to_job(record))
            except (AttributeError, TypeError, ValueError):
                self.invalid_count += 1

        return jobs

    @staticmethod
    def _to_job(record: dict) -> Job:
        description_html = record.get("description") or ""
        description = BeautifulSoup(description_html, "html.parser").get_text(
            " ", strip=True
        )

        return Job(
            title=record.get("title"),
            url=record.get("url"),
            company=record.get("company_name"),
            location=record.get("candidate_required_location"),
            work_model="Remote",
            technologies=record.get("tags") or [],
            source="Remotive",
            published_at=record.get("publication_date"),
            description=description,
        )
