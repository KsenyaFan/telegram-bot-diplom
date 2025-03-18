import requests
from typing import Dict, Optional

from diploma.config_data.config import API_KEY, HOST_API


api_key = API_KEY

class KinoPoiskAPI:
    BASE_URL = HOST_API
    TIMEOUT = 10

    def __init__(self, api_key: str):
        self.headers = {"X-API-KEY": api_key}

    def _make_request(self, endpoint: str, params: Optional[Dict] = None):
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params, timeout=self.TIMEOUT)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code, "message": response.text}

    def search_movie(self, title: str, limit: int = 5):
        """Поиск фильма по названию."""
        params = {"name": title, "limit": limit}
        return self._make_request("/v1.3/movie", params)

    def get_movies_by_rating(self, rating: int, limit: int = 5):
        """Получить фильмы с определённым рейтингом."""
        params = {"rating.kp": rating, "limit": limit}
        return self._make_request("/v1.3/movie", params)

    def get_person_by_name(self, query: str, page: int = 1, limit: int = 1):
        """Получить информацию по актеру."""
        params = {"query": query, "page": page, "limit": limit}
        return self._make_request("/v1.4/person/search", params)



# api = KinoPoiskAPI(API_KEY)
# print(api.get_person_by_name('Адам Сендлер'))
