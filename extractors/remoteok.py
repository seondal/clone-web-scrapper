from requests import get
from bs4 import BeautifulSoup


def extract_remoteok_jobs(keyword):
  headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
  }

  url = f"https://remoteok.com/remote-{keyword}-jobs"
  response = get(url, headers=headers)

  # globe_emojis = "🌎🌍🌏"
  # country_emojis = "🇨🇦🇺🇸💃🇬🇧"

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
        tag_data.append(f"{tag.string} ")
      tag_string = "".join(tag_data)
      tag_string = tag_string.replace(",", "\n")
      # tag_string = tag_string.replace("💰", "salary:")
      # for emoji in globe_emojis:
      #   tag_string = tag_string.replace(emoji, "")
      # for emoji in country_emojis:
      #   tag_string = tag_string.replace(emoji, "")

      job_data = {
        "position": title.string.strip().replace(",", " "),
        "company": name.string.strip().replace(",", " "),
        "tags": tag_string
      }
      results.append(job_data)
  return results
