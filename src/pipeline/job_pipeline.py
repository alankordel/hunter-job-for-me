from src.extract.http_client import fetch_page
from src.extract.parser import parse_jobs
from src.transform.dataframe import to_dataframe
from src.load.csv_writer import save_csv


def run_pipeline():

    print("Iniciando pipeline...")

    html = fetch_page(
        "https://books.toscrape.com/"
    )

    jobs = parse_jobs(html)

    df = to_dataframe(jobs)

    save_csv(
        df,
        "data/processed/jobs.csv"
    )

    print(
        f"Pipeline finalizado. {len(df)} registros salvos."
    )