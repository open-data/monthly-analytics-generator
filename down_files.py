import requests
import os
# retreive urls from the linkFile
with open ('linkFile.txt') as f:
    lines = [line.rstrip('\n') for line in f]
f.close
new_filename = ["openDataPortal.siteAnalytics.datasetsByOrg.bilingual.csv","openDataPortal.siteAnalytics.datasetsByOrgByMonth.bilingual.csv",
                "openDataPortal.siteAnalytics.internationalUsageBreakdown.bilingual.csv", "openDataPortal.siteAnalytics.provincialUsageBreakdown.bilingual.csv",
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
    for line in lines:
        filedow(line)

def csv_files_remove():
    for element in lines:
     os.remove(element.split('/')[-1])
filedownload()
