from diploma.config_data.config import API_KEY, HOST_API
from diploma.api.util.api_collections import KinoPoiskAPI


api_key = API_KEY
site_api = KinoPoiskAPI(api_key=api_key)

query = "Inception"
headers = {
    "X-API-KEY": api_key,  # Добавляем API-ключ
    "accept": "application/json"
}

url = f"{HOST_API}/movie"  # Добавляем endpoint
params = {"name": query, "limit": 5}  # Используем name вместо query

site_api = KinoPoiskAPI(api_key=api_key)

if __name__ == "__main__":
    response = site_api.get(url, headers=headers, params=params)
    # print(response.json())




