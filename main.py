from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"}

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

response = get(f"{base_url}{search_term}", headers=headers)

if response.status_code != 200:
    print("Cant request page")
else:
  print(response.text)