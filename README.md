# Monthly Analytics Generator
This generates the HTML for the monthly analytics found at https://open.canada.ca/en/content/open-government-analytics

## Instructions:

1) Download this repo https://github.com/open-data/monthly-analytics-generator/archive/master.zip and unzip it. ___OR___ clone the repository: `git clone https://github.com/open-data/monthly-analytics-generator.git`

2) Download the up-to-date analytics found at https://open.canada.ca/data/en/dataset/2916fad5-ebcc-4c86-b0f3-4f619b29f412. Place these CSV files you've just downloaded into the same folder as the unzipped repo.

    You will need:
    - Number of Visits, Downloads	
    - Datasets Released by Month	
    - Top 100 Downloaded Datasets (for the month prior)	
    - Datasets by Department or Agency
    - Percentages of Site Visits by Province and Territory	
    - Percentages of Site Visits by Country	

    ___This can be done automatically by running the___ `get_resources.sh` ___script.___

3) run `pip install pyyaml` _(required once, note: pip2)_

4) run `pip install python-dateutil` _(required once, note: pip2)_

5) run `python2 create_html_analytics.py`

6) Copy all HTML from the final **two** `.txt` files generated and paste this in the Drupal `source` section of the editing admin on https://open.canada.ca/en/content/open-government-analytics. Each file contains one language, so paste the HTML from the file ending in `en` on the English page, and the HTML from the file ending in `fr` on the French page.

7) Submit these as **drafts** first to ensure everything looks correct. Once confirmed, save the pages as newly published content.
