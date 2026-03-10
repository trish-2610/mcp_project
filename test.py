import requests
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("FRED_API_KEY")

url = "https://api.stlouisfed.org/fred/series/observations"

params = {
    "series_id": "FEDFUNDS",
    "api_key": key,
    "file_type": "json"
}

print(requests.get(url, params=params).json())