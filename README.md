**WORK IN PROGRESS - FINISHING UP THE CODE FOR THIS**

# Monthly Analytics Generator
This generates the HTML for the monthly analytics found at https://open.canada.ca/en/content/open-government-analytics

## Instructions:

1) Download the up-to-date analytics found at https://open.canada.ca/data/en/dataset/2916fad5-ebcc-4c86-b0f3-4f619b29f412.

You will need:
- Number of Visits, Downloads	
- Datasets Released by Month	
- Top 100 Downloaded Datasets (for the month prior)	
- Datasets by Department or Agency
- Percentages of Site Visits by Province and Territory	
- Percentages of Site Visits by Country	

2) Download this repo https://github.com/open-data/monthly-analytics-generator/archive/master.zip and unzip it. Place the CSV files you've just downloaded into the same folder as the unzipped repo. 

3) run `pip install pyyaml`

4) run `python create_html_analytics.py`

5) Copy all HTML from the final **two** `.txt` files generated and paste this in the Drupal `source` section of the editing admin on https://open.canada.ca/en/content/open-government-analytics. Each file contains one language, so paste the HTML from the file ending in `en` on the English page, and the HTML from the file ending in `fr` on the French page.

6) Submit these as **drafts** first to ensure everything looks correct. Once confirmed, save the pages as newly published content.
