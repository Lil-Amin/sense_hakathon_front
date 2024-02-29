import httpx
from settings import API_URL


def fetch_filtred_resumes(data: bytes) -> list[str]:
    response: httpx.Response = httpx.post(API_URL, data=data)
    filtred_resumes: list[str] = response.content.decode()

    return filtred_resumes
