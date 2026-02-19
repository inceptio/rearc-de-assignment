import requests

from utils.config import DATAUSA_BSA_URL


def fetch_datausa_population():
    response_format="jsonrecords"
    url = f"{DATAUSA_BSA_URL}/data.{response_format}"
    params = {
        "cube": "acs_yg_total_population_1",
        "drilldowns": "Year,Nation",
        "locale": "en",
        "measures": "Population"
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)

        print("Request URL:", response.url)
        print("Status Code:", response.status_code)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print("HTTP Error:", e)
        print("Raw response:", response.text[:500])
        return None
