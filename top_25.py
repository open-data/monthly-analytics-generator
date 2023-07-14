# coding=utf-8
# This reads visits from openDataPortal.siteAnalytics.top100Datasets.bilingual.csv

import csv, datetime, yaml


def to_html():
    en_to_html()
    fr_to_html()

def en_to_html():
    final_result = open("top_25_en.txt", "w")
    create_intro_en(final_result)
    get_rows_en(final_result)
    final_result.close()

def fr_to_html():
    final_result = open("top_25_fr.txt", "w")
    create_intro_fr(final_result)
    get_rows_fr(final_result)
    final_result.close()
   

def create_intro_en(final_result):
    dt = datetime.datetime.today()
    today = dt.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    intro = """<section><h2 class="mrgn-tp-xl" id="top10">Top 25 Downloaded Datasets</h2>
    <p>These are the top 25 downloaded datasets for the month of <span class="nowrap"><time datetime=\"""" + lastMonth.strftime("%Y-%m-%d") + "\">"+ lastMonth.strftime("%B, %Y")  +"</time></span>.</p> """"
    <div class="table-responsive"><table class="table">
    <thead><tr><th scope="col">Title</th>
    <th scope="col">Department</th>
    <th scope="col">Number of Downloads</th></tr></thead><tbody>\n"""
    final_result.write(intro)

def create_intro_fr(final_result):
    dt = datetime.datetime.today()
    today = dt.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    months = yaml.full_load(open('months.yml', 'r'))
    french_month = months.get('long_form').get(lastMonth.strftime("%B"))
    french_date = french_month + lastMonth.strftime(", %Y")

    intro = """<section><h2 class="mrgn-tp-xl" id="top10">Les 25 principaux jeux de données téléchargés</h2>
    <p>Voici les 25 principaux jeux de données téléchargés à partir du portail du gouvernement ouvert en fonction du nombre de téléchargements effectués au cours du mois de <span class="nowrap"><time datetime=\"""" + lastMonth.strftime("%Y-%m-%d") + "\">"+ french_date +"</time></span>.</p> """"
    <div class="table-responsive"><table class="table">
    <thead><tr><th scope="col">Titre</th>
    <th scope="col">Ministère</th>
    <th scope="col">Nombre de téléchargements</th></tr></thead><tbody>\n"""
    final_result.write(intro)

def get_rows_en(final_result):
    final_result_string = []

    with open("openDataPortal.siteAnalytics.top100Datasets.bilingual.csv", 'r') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)

        for x in range(25):
            row = next(monthly_usage, None)
            final_result.write("<tr><th scope=\"row\"><a href=\"/data/en/dataset/" + row[0] + "\">" + row[1] + "</a></th><td>" + row[3] + 
                "</td><td class=\"text-center\">" + '{:,}'.format(int(row[5])) + "</td></tr>\n")
        final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")

def get_rows_fr(final_result):
    final_result_string = []

    with open("openDataPortal.siteAnalytics.top100Datasets.bilingual.csv", 'r', encoding='utf-8') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)

        for x in range(25):
            row = next(monthly_usage, None)
            final_result.write("<tr><th scope=\"row\"><a href=\"/data/en/dataset/" + row[0] + "\">" + row[2] + "</a></th><td>" + row[4] + 
                "</td><td class=\"text-center\">" + '{:,}'.format(int(row[5])).replace(',', ' ') + "</td></tr>\n")
        final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")