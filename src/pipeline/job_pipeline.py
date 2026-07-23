import logging

from src.config.settings import OUTPUT_PATH
from src.extract.http_client import HttpClientError
from src.filters.job_filter import filter_jobs
from src.load.csv_writer import save_csv
from src.sources.remotive_source import RemotiveSource
from src.transform.dataframe import remove_duplicates, sort_jobs, to_dataframe


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def run_pipeline() -> None:
    """Executa coleta, filtro, deduplicação e exportação das vagas."""
    source = RemotiveSource()
    logger.info("Iniciando coleta de vagas...")
    logger.info("Fonte utilizada: %s", source.name)

    try:
        jobs = source.get_jobs()
    except (HttpClientError, ValueError) as error:
        logger.error("O pipeline não pôde continuar: %s", error)
        return

    logger.info("Vagas recebidas: %s", len(jobs))
    logger.info("Vagas inválidas ignoradas: %s", source.invalid_count)

    if not jobs:
        logger.warning("A fonte não retornou vagas. Nenhum arquivo foi gerado.")
        return

    compatible_jobs = filter_jobs(jobs)
    logger.info("Vagas compatíveis: %s", len(compatible_jobs))

    df = to_dataframe(compatible_jobs)
    df, duplicate_count = remove_duplicates(df)
    df = sort_jobs(df)
    logger.info("Duplicados removidos: %s", duplicate_count)

    try:
        output_path = save_csv(df, OUTPUT_PATH)
    except OSError as error:
        logger.error("Não foi possível salvar o CSV: %s", error)
        return

    logger.info("Arquivo gerado em: %s", output_path)
    logger.info("Pipeline finalizado com sucesso.")
