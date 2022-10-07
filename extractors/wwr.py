from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"}

    url = f"https://remoteok.com/remote-{keyword}-jobs"
    response = get(url, headers=headers)

    if response.status_code != 200:
        print("Can't request website")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("td", class_="company position company_and_position")
        jobs.pop(0)
        results = []
        for job in jobs:
            title = job.find("h2", itemprop="title")
            name = job.find("h3", itemprop="name")
            tags = job.find_all("div", class_="location")
            tag_data = []
            for tag in tags:
                tag_data.append(tag.string)
                job_data = {
                    "title": title.string,
                    "name": name.string,
                    "tags": tag_data
                }
                results.append(job_data)
    return results