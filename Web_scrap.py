from bs4 import BeautifulSoup
import requests

HTML_CODE = requests.get('https://www.freshersworld.com/jobs/category/it-software-job-vacancies').text
jobs_dtr = {}
soup = BeautifulSoup(HTML_CODE, 'lxml')
jobs = soup.find_all('div', class_ = "col-md-12 col-lg-12 col-xs-12 padding-none")
i = 1
for job in jobs:
    temp = {}
    comp_name = job.find('div', class_ = 'col-md-12 col-lg-12 col-xs-12 job-desc-block').find('div', class_ = 'col-md-12 col-xs-12 col-lg-12 job_listing_alignment').find('div',class_ = 'col-md-12 col-xs-12 col-lg-12 padding-none left_move_up_new').a.h3.text
    print(comp_name)
    temp['Name'] = comp_name
    role = job.find('div', class_ = 'col-md-12 col-xs-12 col-lg-12 padding-none left_move_up_new').find('div').text
    temp['Role'] = role
    qulf = "B.E./BTech(CS,IT), MCA"
    temp['Qualification'] = qulf
    dscp = job.find('div', class_ = 'col-md-12 col-xs-12 col-lg-12 padding-none margin-top').find('span', class_ = "desc").text.strip()
    temp['Eligibilty and Description'] = dscp
    loc = job.find('div', class_ = "col-md-12 col-xs-12 col-lg-12 view-apply-container").find('div', class_ = 'col-md-5 col-xs-5 col-lg-5 padding-none').find('span',class_ = 'job-location display-block modal-open').a.text
    temp['Location'] = loc
    Lst = job.find('div', class_ = 'col-md-12 col-xs-12 col-lg-12 view-apply-container').find('div', class_ = 'col-md-9 col-xs-9 col-lg-9 padding-none padding-top-5').find('div', class_ = "col-md-4 col-xs-4 col-lg-4 padding-none").find('span', class_ = "padding-left-4").text
    temp['Last Date'] = Lst
    jobs_dtr[i] = temp
    i += 1
    print(jobs_dtr)
print(jobs_dtr)