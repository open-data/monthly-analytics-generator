import requests
import os
from datetime import *
today = datetime.today()
last_day = (today - timedelta(days=today.day)).strftime('%Y-%m-%d')
y, m, d = last_day.split("-")
resource_link = "https://open.canada.ca/data/dataset/2916fad5-ebcc-4c86-b0f3-4f619b29f412/resource/"
province = "".join ([resource_link,"e06f06a9-d897-4a35-9b73-4c2bc1c2d5cf/download/opendataportal.siteanalytics.provincialusagebreakdown.bilingual"
                         ,m,y,".csv"]) 
country = "".join ([resource_link,"b52ee0b2-f2be-4bc5-a27a-db93a228d38b/download/opendataportal.siteanalytics.internationalusagebreakdown.bilingual"
                        ,m,y,".csv"])
urls = ["https://open.canada.ca/data/dataset/2916fad5-ebcc-4c86-b0f3-4f619b29f412/resource/02a92b0f-b26d-4fbd-9601-d27651703715/download/opendataportal.siteanalytics.totalmonthlyusage.bilingual.csv",
province,
country,
"https://open.canada.ca/data/dataset/2916fad5-ebcc-4c86-b0f3-4f619b29f412/resource/5a1b343d-2fea-4c31-8652-f77506e3ea37/download/opendataportal.siteanalytics.datasetsbyorg.bilingual.csv",
"https://open.canada.ca/data/dataset/2916fad5-ebcc-4c86-b0f3-4f619b29f412/resource/f09148f9-a09b-46ec-bf5b-52f26720f3f3/download/opendataportal.siteanalytics.datasetsbyorgbymonth.bilingual.csv",
"https://open.canada.ca/data/dataset/2916fad5-ebcc-4c86-b0f3-4f619b29f412/resource/ba980e38-f110-466a-ad92-3ee0d5a60d49/download/opendataportal.siteanalytics.top100datasets.bilingual.csv"]
  
# retreive urls from the linkFile
# with open ('linkFile.txt') as f:
#     lines = [line.rstrip('\n') for line in f]
# f.close
new_filename = ["openDataPortal.siteAnalytics.datasetsByOrg.bilingual.csv","openDataPortal.siteAnalytics.datasetsByOrgByMonth.bilingual.csv",
                "".join(["openDataPortal.siteAnalytics.internationalUsageBreakdown.bilingual",m,y,".csv"]), "".join(["openDataPortal.siteAnalytics.provincialUsageBreakdown.bilingual",m,y,".csv"]),
                "openDataPortal.siteAnalytics.top100Datasets.bilingual.csv","openDataPortal.siteAnalytics.totalMonthlyUsage.bilingual.csv"]
# CSV files downloading method / URL
def filedow (reqURL):
    try:
        req = requests.get(reqURL)
        filename =  reqURL.split('/')[-1]
        for new_name in new_filename:
            if new_name.lower() == filename:
                filename = new_name
        with open (filename, 'wb') as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        f.close
    except Exception as e:
        print(e)
 # downloading all the files      
def filedownload():
    for url in urls:
        filedow(url)

def csv_files_remove():
    for element in urls:
     os.remove(element.split('/')[-1])
filedownload()
