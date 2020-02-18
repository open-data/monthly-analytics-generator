# This reads downloads from openDataPortal.siteAnalytics.totalMonthlyUsage.bilingual.csv

import csv

def to_html():
    final_result = open("monthly_downloads.txt", "w")
    create_intro(final_result)
    format_dates(final_result)
    get_downloads(final_result)


def get_downloads(final_result):
    final_result_string = []

    with open("openDataPortal.siteAnalytics.totalMonthlyUsage.bilingual.csv", 'rb') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)

        final_result_string = []
        final_result.write("</tr></thead><tbody><tr>\n")
        final_result.write("<th scope=\"row\" data-flot='{\"color\":\"#2572B4\"}'>Downloads</th>\n")

        for row in monthly_usage:
            final_result_string.append("<td class=\"text-left\">" + row[3] + "</td>\n")
        final_result_string.reverse()
        del final_result_string[0:len(final_result_string) - 12]
        for line in final_result_string:
            final_result.write(line)

        final_result.write("</tr></tbody></table><div class=\"clearfix\">&nbsp;</div></section>\n")

def create_intro(final_result):
    intro = """<section><h2 class="mrgn-tp-xl" id="downloads">Number of Downloads</h2>
    <p>These numbers summarize the number of downloads on the Open Government Portal. A download represents the number of times a user has clicked to download a resource for a particular dataset.</p>
    <table class="wb-charts table" data-flot='{"legend": {"show":true} }'><caption>Number of Downloads</caption>
    <thead><tr><th>&nbsp;</th>\n"""
    final_result.write(intro)

def format_dates(final_result):
    MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    final_result_string = []

    with open("openDataPortal.siteAnalytics.totalMonthlyUsage.bilingual.csv", 'rb') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)

        for row in monthly_usage:
            final_result_string.append("<th scope=\"col\"><time datetime=" + row[0] + "-" + row[1] + ">" + str(MONTHS[int(row[1])-1]) + "-" + row[0] + "</time></th>\n")
        final_result_string.reverse()
        del final_result_string[0:len(final_result_string) - 12]
        for line in final_result_string:
            final_result.write(line)