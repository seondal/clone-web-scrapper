from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_page_count(keyword):
  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")

  browser = webdriver.Chrome(options=options)

  base_url = "https://kr.indeed.com/jobs?q="
  browser.get(f"{base_url}{keyword}")
  response = browser.page_source
  soup = BeautifulSoup(response, features="html5lib")

  pages = soup.find_all("div", class_="css-tvvxwd ecydgvn1")
  count = len(pages)
  if count == 0:
    return 1
  elif count >= 5:
    return 5
  else:
    return count


def extract_indeed_jobs(keyword):
  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  browser = webdriver.Chrome(options=options)

  pages = get_page_count(keyword)
  print("Found", pages, "pages")
  results = []

  for page in range(pages):
    base_url = "https://kr.indeed.com/jobs"
    final_url = f"{base_url}?q={keyword}&start={page*10}"
    browser.get(f"{final_url}")
    response = browser.page_source
    soup = BeautifulSoup(response, features="html5lib")

    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all("li", recursive=False)
    for job in jobs:
      zone = job.find("div", class_="mosaic-zone")
      if zone == None:
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
          "link": f"https://kr.indeed.com/{link}",
          "company": company.string.replace(","," "),
          "location": location.string,
          "position": title
        }
        results.append(job_data)
  return results
