from extractors.indeed import extract_indeed_jobs
from extractors.remoteok import extract_remoteok_jobs

keyword = input("What do you want to search for?")

# indeed = extract_indeed_jobs(keyword)
wwr = extract_remoteok_jobs(keyword)
jobs = wwr

file = open(f"{keyword}.csv", "w")
file.write("Position, Company, Tags \n")

for job in jobs:
  file.write(f"{job['position']},{job['company']},{job['location']}\n")
  print(job)
  print("\n")
  
file.close()




