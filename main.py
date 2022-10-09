from extractors.indeed import extract_indeed_jobs
from extractors.remoteok import extract_remoteok_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

keyword = input("What do you want to search for?")

# indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
remoteok = extract_remoteok_jobs(keyword)
jobs = wwr + remoteok

save_to_file(keyword, jobs)





