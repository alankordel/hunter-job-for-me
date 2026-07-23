import requests


class HttpClientError(Exception):
    """Erro ao consultar uma fonte externa."""


def fetch_json(url: str, timeout: int = 20) -> dict:
    """Faz uma requisição GET e devolve a resposta JSON."""
    try:
        response = requests.get(
            url,
            timeout=timeout,
            headers={"User-Agent": "hunter-job-for-me/1.0"},
        )
        response.raise_for_status()
        data = response.json()
    except requests.Timeout as error:
        raise HttpClientError("A consulta à fonte excedeu o tempo limite") from error
    except requests.RequestException as error:
        raise HttpClientError(f"Não foi possível consultar a fonte: {error}") from error
    except ValueError as error:
        raise HttpClientError("A fonte retornou um JSON inválido") from error

    if not isinstance(data, dict):
        raise HttpClientError("A fonte retornou um formato inesperado")

    return data
