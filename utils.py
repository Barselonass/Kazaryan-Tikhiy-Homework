import requests
from config import API_BASE_URL
def fetch_data(endpoint):
	response = requests.get(f"{API_BASE_URL}/{endpoint}")
	response.raise_for_status()
	return response.json()
def format_output(data, limit=5):
	return "\n".join([f"{i+1}. {item['title']}" for i, item in enumerate(data[:limit])])
