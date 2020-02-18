# This reads visits from openDataPortal.siteAnalytics.datasetsByOrg.bilingual.csv

import csv
import datetime
import calendar

def to_html():
    final_result = open("dep_or_agency.txt", "w")
    create_intro(final_result)
    get_rows(final_result)

def create_intro(final_result):
    dt = datetime.datetime.today()
    today = dt.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    intro = """<section><h2 class="mrgn-tp-xl" id="department">Datasets by Department or Agency</h2>
    <p>These numbers represent the breakdown of raw datasets on the Open Government Portal by department or agency. These numbers were captured on <time datetime=\"""" + lastMonth.strftime("%Y-%m-%d") +"\">" + lastMonth.strftime("%B ") + str(calendar.monthrange(lastMonth.year, lastMonth.month)[1]) + ", " + lastMonth.strftime("%Y") + """.</time> 
    <a href="#monthly">See how much we have grown since <time datetime="2013-06-18">June&nbsp;18,&nbsp;2013</time></a>.</p>
    <div class="table-responsive"><table class="table">
    <thead><tr><th scope="col">Government of Canada Department or Agency</th>
    <th scope="col">Number of datasets</th></tr></thead>\n<tbody>"""
    final_result.write(intro)

def get_rows(final_result):
    final_result_string = []

    with open("openDataPortal.siteAnalytics.datasetsByOrg.bilingual.csv", 'rb') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)
        total = 0

        for row in monthly_usage:
            final_result.write("<tr><th scope=\"row\"><a href=\"" + row[2] + "\">" + row[0] + "</a></th><td class=\"text-center\">" + row[4] + "</td></tr>\n")
            total += int(row[4])
        final_result.write("<tfoot><tr><th class=\"text-left\" scope=\"row\">Total</th><td class=\"text-center\">" + str(total) + "</td></tr></tfoot>")
        final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")