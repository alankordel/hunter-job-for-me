import requests


def fetch_page(url: str) -> str:
    """
    Requisição HTTP GET e retorna o HTML da página.
    """

    response = requests.get(url)

    return response.text