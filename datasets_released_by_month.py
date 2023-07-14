# coding=utf-8
# This reads visits from openDataPortal.siteAnalytics.datasetsByOrgByMonth.bilingual.csv

import csv, datetime, yaml
from dateutil import relativedelta

def to_html():
    en_to_html()
    fr_to_html()

def en_to_html():
    final_result = open("datasets_released_by_month_en.txt", "w")
    create_intro_en(final_result)
    format_dates_en(final_result)
    get_rows_en(final_result)
    final_result.close()

def fr_to_html():
    final_result = open("datasets_released_by_month_fr.txt", "w")
    create_intro_fr(final_result)
    format_dates_fr(final_result)
    get_rows_fr(final_result)
    final_result.close()

def create_intro_en(final_result):
    intro = """<section><h2 class="mrgn-tp-xl" id="monthly">Datasets Released by Month</h2>
    <p>The following table represents the number of datasets that have been published each month since the Open Government Portal's relaunch on <time datetime="2013-06-18">June&nbsp;18,&nbsp;2013</time>.</p>
    <div class="table-responsive"><table class="table small"><thead><tr><th scope="col">Government of Canada Department or Agency</th>\n"""
    final_result.write(intro)

def create_intro_fr(final_result):
    intro = """<section><h2 class="mrgn-tp-xl" id="monthly">Jeux de données publiés par mois</h2>
    <p>Le tableau qui suit présente le nombre de jeux de données qui ont été publiés chaque mois depuis le relancement du portail du gouvernement ouvert, soit le <time datetime="2013-06-18">18&nbsp;juin&nbsp;2013</time>.</p>
    <div class="table-responsive"><table class="table small"><thead><tr><th scope="col">Ministère ou organisme du gouvernement du Canada</th>\n"""
    final_result.write(intro)

def get_rows_en(final_result):
    final_result_string = []
    count = 0

    with open("openDataPortal.siteAnalytics.datasetsByOrgByMonth.bilingual.csv", 'r') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)
        
        for row in monthly_usage:
            count+=1

    with open("openDataPortal.siteAnalytics.datasetsByOrgByMonth.bilingual.csv", 'r') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)
        total = 0

        for x in range(count-1):
            row = next(monthly_usage, None)
            url = row[1].split("|", 1)[0]
            org = row[0].split("|", 1)[0]
            final_result.write("<tr><th scope=\"row\"><a href=\"" + url + "\">" + org + "</a></th><td class=\"text-left\">" + '{:,}'.format(int(row[2])) + "</th><td class=\"text-left\">"
            + '{:,}'.format(int(row[3])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[4])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[5])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[6])) +"</td><td class=\"text-left\">" 
            + '{:,}'.format(int(row[7])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[8])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[9])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[10])) +"</td><td class=\"text-left\">"
            + '{:,}'.format(int(row[11])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[12])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[13])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[14])) +"</td><td class=\"text-left\">"
            + '{:,}'.format(int(row[15])) +"</td></tr>")
        row = next(monthly_usage, None)
        final_result.write("<tr><th scope=\"row\">Total</th><td class=\"text-left\">" + '{:,}'.format(int(row[2])) + "</th><td class=\"text-left\">"
            + '{:,}'.format(int(row[3])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[4])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[5])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[6])) +"</td><td class=\"text-left\">" 
            + '{:,}'.format(int(row[7])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[8])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[9])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[10])) +"</td><td class=\"text-left\">"
            + '{:,}'.format(int(row[11])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[12])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[13])) +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[14])) +"</td><td class=\"text-left\">"
            + '{:,}'.format(int(row[15])) +"</td></strong></td></tr>")
        final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")

def get_rows_fr(final_result):
    final_result_string = []
    count = 0

    with open("openDataPortal.siteAnalytics.datasetsByOrgByMonth.bilingual.csv", 'r',encoding='utf-8') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)
        
        for row in monthly_usage:
            count+=1

    with open("openDataPortal.siteAnalytics.datasetsByOrgByMonth.bilingual.csv", 'r', encoding='utf-8') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)
        total = 0

        for x in range(count-1):
            row = next(monthly_usage, None)
            url = row[1].split("|", 1)[1]
            org = row[0].split("|", 1)[1]
            final_result.write("<tr><th scope=\"row\"><a href=\"" + url + "\">" + org + "</a></th><td class=\"text-left\">" + '{:,}'.format(int(row[2])).replace(',', ' ') + "</th><td class=\"text-left\">"
            + '{:,}'.format(int(row[3])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[4])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[5])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[6])).replace(',', ' ') +"</td><td class=\"text-left\">" 
            + '{:,}'.format(int(row[7])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[8])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[9])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[10])).replace(',', ' ') +"</td><td class=\"text-left\">"
            + '{:,}'.format(int(row[11])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[12])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[13])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[14])).replace(',', ' ') +"</td><td class=\"text-left\">"
            + '{:,}'.format(int(row[15])).replace(',', ' ') +"</td></tr>")
        row = next(monthly_usage, None)
        final_result.write("<tr><th scope=\"row\">Total</th><td class=\"text-left\">" + '{:,}'.format(int(row[2])).replace(',', ' ') + "</th><td class=\"text-left\">"
            + '{:,}'.format(int(row[3])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[4])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[5])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[6])).replace(',', ' ') +"</td><td class=\"text-left\">" 
            + '{:,}'.format(int(row[7])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[8])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[9])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[10])).replace(',', ' ') +"</td><td class=\"text-left\">"
            + '{:,}'.format(int(row[11])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[12])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[13])).replace(',', ' ') +"</td><td class=\"text-left\">" + '{:,}'.format(int(row[14])).replace(',', ' ') +"</td><td class=\"text-left\">"
            + '{:,}'.format(int(row[15])).replace(',', ' ') +"</td></strong></td></tr>")
        final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")

def format_dates_en(final_result):
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

def format_dates_fr(final_result):
    dt = datetime.datetime.today()
    today = dt.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)
    lastYear = (datetime.datetime.now() - datetime.timedelta(days=364)).replace(day=1)

    months = yaml.full_load(open('months.yml', 'r', encoding='utf-8'))
    french_month = months.get('short_form').get(lastMonth.strftime("%b"))
    french_date = french_month + lastMonth.strftime("- %Y")

    final_result_string = []

    final_result_string.append("<th scope=\"col\">Avant <time datetime=\"" + lastYear.strftime("%Y-%m-%d") + "\"></time>" + french_date +"</th>\n")
    for x in range(0, 12):
        time_date = (datetime.datetime.strptime(str(lastYear + relativedelta.relativedelta(months=x)), '%Y-%m-%d %H:%M:%S.%f'))
        string_date = time_date.strftime("%Y-%m").split(" ", 1)[0]
        french_date = months.get('short_form').get(time_date.strftime("%b"))
        word_date = french_date + time_date.strftime("- %Y")

        final_result_string.append("<th scope=\"col\"><time datetime=\"" + string_date + "\">" + word_date + "</time></th>\n")
    for line in final_result_string:
        final_result.write(line)
    final_result.write("<th scope=\"col\">Nombre de nouveaux jeux de données</th>\n</tr></thead><tbody>")