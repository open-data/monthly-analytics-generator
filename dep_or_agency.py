# coding=utf-8
# This reads visits from openDataPortal.siteAnalytics.datasetsByOrg.bilingual.csv

import csv, datetime, yaml

def to_html():
    en_to_html()
    fr_to_html()

def en_to_html():
    final_result = open("dep_or_agency_en.txt", "w")
    create_intro_en(final_result)
    get_rows_en(final_result)
    final_result.close()

def fr_to_html():
    final_result = open("dep_or_agency_fr.txt", "w")
    create_intro_fr(final_result)
    get_rows_fr(final_result)
    final_result.close()

def create_intro_en(final_result):
    dt = datetime.datetime.today()
    today = dt.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    intro = """<section><h2 class="mrgn-tp-xl" id="department">Datasets by Department or Agency</h2>
    <p>These numbers represent the breakdown of raw datasets on the Open Government Portal by department or agency. These numbers were captured on <time datetime=\"""" + lastMonth.strftime("%Y-%m-%d") +"\">" + lastMonth.strftime("%B %d, %Y") + """.</time> 
    <a href="#monthly">See how much we have grown since <time datetime="2013-06-18">June&nbsp;18,&nbsp;2013</time></a>.</p>
    <div class="table-responsive"><table class="table">
    <thead><tr><th scope="col">Government of Canada Department or Agency</th>
    <th scope="col">Number of datasets</th></tr></thead>\n<tbody>"""
    final_result.write(intro)

def create_intro_fr(final_result):
    dt = datetime.datetime.today()
    today = dt.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    months = yaml.full_load(open('months.yml', 'r'))
    french_month = months.get('long_form').get(lastMonth.strftime("%B"))
    french_date = lastMonth.strftime("%d ") + french_month + lastMonth.strftime(", %Y")

    intro = """<section><h2 class="mrgn-tp-xl" id="department">Jeux de données par ministère ou organisme</h2>
    <p>Le tableau ci-dessous présente des jeux de données brutes tirés du portail du gouvernement ouvert en fonction des ministères et organismes. Ces données ont été recueillies le <span class="nowrap"><time datetime=\"""" + lastMonth.strftime("%Y-%m-%d") +"\">" + french_date + """.</time></span> 
    Vous pourrez <a href="#monthly">constater la croissance que nous avons connue depuis le <time datetime="2013-06-18">18&nbsp;juin&nbsp;2013</time></a>.</p>
    <div class="table-responsive"><table class="table">
    <thead><tr><th scope="col">Ministère ou organisme du gouvernement du Canada</th>
    <th scope="col">Nombre total de jeux de données</th></tr></thead>\n"""
    final_result.write(intro)
    

def get_rows_en(final_result):
    with open("openDataPortal.siteAnalytics.datasetsByOrg.bilingual.csv", 'r') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)
        total = 0

        for row in monthly_usage:
            final_result.write("<tr><th scope=\"row\"><a href=\"" + row[2] + "\">" + row[0] + "</a></th><td class=\"text-center\">" + '{:,}'.format(int(row[4])) + "</td></tr>\n")
            total += int(row[4])
        final_result.write("<tfoot><tr><th class=\"text-left\" scope=\"row\">Total</th><td class=\"text-center\">" + '{:,}'.format(int(total)) + "</td></tr></tfoot>")
        final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")

def get_rows_fr(final_result):
    with open("openDataPortal.siteAnalytics.datasetsByOrg.bilingual.csv", 'r', encoding='utf-8') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)
        total = 0

        for row in monthly_usage:
            final_result.write("<tr><th scope=\"row\"><a href=\"" + row[3] + "\">" + row[1] + "</a></th><td class=\"text-center\">" + '{:,}'.format(int(row[4])).replace(',', ' ') + "</td></tr>\n")
            total += int(row[4])
        final_result.write("<tfoot><tr><th class=\"text-left\" scope=\"row\">Total</th><td class=\"text-center\">" + '{:,}'.format(total).replace(',', ' ')  + "</td></tr></tfoot>")
        final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")