from src.extract.http_client import fetch_page
from src.extract.parser import parse_jobs
from src.sources.base import JobSource


class BooksSource(JobSource):

    URL = "https://books.toscrape.com/"

    def get_jobs(self):
        html = fetch_page(self.URL)
        jobs = parse_jobs(html)
        return jobs