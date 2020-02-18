# This reads visits from openDataPortal.siteAnalytics.top100Datasets.bilingual.csv

import csv
import datetime

def to_html():
    final_result = open("top_25.txt", "w")
    create_intro(final_result)
    get_rows(final_result)

def create_intro(final_result):
    dt = datetime.datetime.today()
    today = dt.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    intro = """<section><h2 class="mrgn-tp-xl" id="top10">Top 25 Downloaded Datasets</h2>
    <p>These are the top 25 downloaded datasets for the month of <span class="nowrap"><time datetime=\"""" + str(dt.year) + "-" + str(dt.month - 1) + "\">"+ lastMonth.strftime("%B, %Y")  +"</time></span>.</p>" + """"
    <div class="table-responsive"><table class="table">
    <thead><tr><th scope="col">Title</th>
    <th scope="col">Department</th>
    <th scope="col">Number of Downloads</th></tr></thead><tbody>\n"""
    final_result.write(intro)

def get_rows(final_result):
    final_result_string = []

    with open("openDataPortal.siteAnalytics.top100Datasets.bilingual.csv", 'rb') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)

        for row in monthly_usage:
            final_result.write("<tr><th scope=\"row\"\"><a href=\"/data/en/dataset/" + row[0] + ">" + row[1] + "</a></th><td>" + row[3] + 
                "</td><td class=\"text-center\">" + row[5] + "</td></tr>\n")
        final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")