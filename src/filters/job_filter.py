from dataclasses import dataclass

from src.config.settings import (
    INTEREST_LOCATIONS,
    MINIMUM_MATCH_SCORE,
    NEGATIVE_TITLE_TERMS,
    POSITIVE_KEYWORDS,
)
from src.models.job import Job


@dataclass
class MatchResult:
    job: Job
    match_score: int
    matched_keywords: list[str]


def score_job(job: Job) -> MatchResult:
    """Calcula uma pontuação simples de compatibilidade para a vaga."""
    title = job.title.casefold()
    description = (job.description or "").casefold()
    location = (job.location or "").casefold()
    work_model = (job.work_model or "").casefold()

    title_matches = [word for word in POSITIVE_KEYWORDS if word.casefold() in title]
    description_matches = [
        word for word in POSITIVE_KEYWORDS
        if word.casefold() in description and word not in title_matches
    ]

    score = len(title_matches) * 3 + len(description_matches)
    if any(place.casefold() in location for place in INTEREST_LOCATIONS):
        score += 2
    if "remote" in work_model or "remoto" in work_model:
        score += 2
    if any(term.casefold() in title for term in NEGATIVE_TITLE_TERMS):
        score -= 3

    return MatchResult(
        job=job,
        match_score=score,
        matched_keywords=title_matches + description_matches,
    )


def filter_jobs(jobs: list[Job]) -> list[MatchResult]:
    """Mantém apenas vagas que atingem a pontuação mínima."""
    results = [score_job(job) for job in jobs]
    return [result for result in results if result.match_score >= MINIMUM_MATCH_SCORE]
