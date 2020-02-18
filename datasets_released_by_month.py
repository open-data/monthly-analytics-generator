# This reads visits from openDataPortal.siteAnalytics.datasetsByOrgByMonth.bilingual.csv

import csv
import datetime
from dateutil import relativedelta

def to_html():
    final_result = open("datasets_released_by_month.txt", "w")
    create_intro(final_result)
    format_dates(final_result)
    get_rows(final_result)

def create_intro(final_result):
    intro = """<section><h2 class="mrgn-tp-xl" id="monthly">Datasets Released by Month</h2>
    <p>The following table represents the number of datasets that have been published each month since the Open Government Portal's relaunch on <time datetime="2013-06-18">June&nbsp;18,&nbsp;2013</time>.</p>
    <div class="table-responsive"><table class="table small"><thead><tr><th scope="col">Government of Canada Department or Agency</th>\n"""
    final_result.write(intro)

def get_rows(final_result):
    final_result_string = []

    with open("openDataPortal.siteAnalytics.datasetsByOrgByMonth.bilingual.csv", 'rb') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)
        total = 0

        for row in monthly_usage:
            url = row[1].split("|", 1)[0]
            org = row[0].split("|", 1)[0]
            final_result.write("<tr><th scope=\"row\"><a href=\"" + url + "\">" + org + "</a></th><td class=\"text-left\">" + row[2] + "</th><td class=\"text-left\">"
            + row[3] +"</td><td class=\"text-left\">" + row[4] +"</td><td class=\"text-left\">" + row[5] +"</td><td class=\"text-left\">" + row[6] +"</td><td class=\"text-left\">" 
            + row[7] +"</td><td class=\"text-left\">" + row[8] +"</td><td class=\"text-left\">" + row[9] +"</td><td class=\"text-left\">" + row[10] +"</td><td class=\"text-left\">"
            + row[11] +"</td><td class=\"text-left\">" + row[12] +"</td><td class=\"text-left\">" + row[13] +"</td><td class=\"text-left\">" + row[14] +"</td><td class=\"text-left\">"
            + row[15] +"</td></tr>")
            total += int(row[4])
        final_result.write("<tfoot><tr><th class=\"text-left\" scope=\"row\">Total</th><td class=\"text-center\">" + str(total) + "</td></tr></tfoot>")
        final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")

def format_dates(final_result):
    dt = datetime.datetime.today()
    today = dt.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)
    lastYear = (datetime.datetime.now() - datetime.timedelta(days=364)).replace(day=1)

    final_result_string = []

    final_result_string.append("<th scope=\"col\">Prior to <time datetime=\"" + lastYear.strftime("%Y-%m-%d") + "\"></time>" + lastYear.strftime("%b-%Y") +"</th>\n")
    for x in range(0, 12):
        time_date = (datetime.datetime.strptime(str(lastYear + relativedelta.relativedelta(months=x)), '%Y-%m-%d %H:%M:%S.%f'))
        string_date = time_date.strftime("%Y-%m").split(" ", 1)[0]
        word_date = time_date.strftime("%b-%Y")

        final_result_string.append("<th scope=\"col\"><time datetime=\"" + string_date + "\">" + word_date + "</time></th>\n")
    for line in final_result_string:
        final_result.write(line)
    final_result.write("<th scope=\"col\">Total number of new datasets</th>\n</tr></thead><tbody>")