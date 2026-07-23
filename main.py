from src.sources.books_source import BooksSource
from src.transform.dataframe import to_dataframe
from src.load.csv_writer import save_csv


def main():
    source = BooksSource()

    jobs = source.get_jobs()

    df = to_dataframe(jobs)

    save_csv(
        df,
        "data/processed/jobs.csv"
    )

    print(df.head())


if __name__ == "__main__":
    main()