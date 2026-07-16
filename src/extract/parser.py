from bs4 import BeautifulSoup

from src.models.job import Job


def parse_jobs(html: str):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    jobs = []

    cards = soup.find_all(
        "article",
        class_="product_pod"
    )

    for card in cards:

        title = (
            card
            .find("h3")
            .find("a")
            .get("title")
        )

        url = (
            card
            .find("h3")
            .find("a")
            .get("href")
        )

        job = Job(
            title=title,
            url=url
        )

        jobs.append(job)

    return jobs