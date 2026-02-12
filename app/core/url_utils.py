from urllib.parse import urlparse, urlunparse

def normalize_url(url: str) -> str:
    parsed = urlparse(url)

    normalized = parsed._replace(fragment="")

    return urlunparse(normalized)

