echo 'import requests
from config import API_BASE_URL

def fetch_data(endpoint):
    response = requests.get(f"{API_BASE_URL}/{endpoint}")
    response.raise_for_status()
    return response.json()

def format_output(data):
    return "\n".join([f"- {item['\''title'\'']}" for item in data[:5]])' > utils.py

