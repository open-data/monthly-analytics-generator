# coding=utf-8
# This reads visits from openDataPortal.siteAnalytics.internationalUsageBreakdown.bilingual.csv

import csv, re, yaml

COLOURS = ["(143, 31, 23)", "(240, 131, 0)", "(36, 124, 168)", "(91, 46, 108)", "(38, 83, 38)",
"(18, 64, 86)", "(85, 85, 85)", "(247, 212, 0)", "(217, 59, 50)", "(62, 134, 62)"]

def to_html():
    en_to_html()
    fr_to_html()

def en_to_html():
    final_result = open("percentages_of_site_visits_by_foreign_country_en.txt", "w")
    create_en_intro(final_result)
    get_country_en(final_result)
    create_en_graph(final_result)
    final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")
    final_result.close()

def fr_to_html():
    final_result = open("percentages_of_site_visits_by_foreign_country_fr.txt", "w")
    create_fr_intro(final_result)
    get_country_fr(final_result)
    create_fr_graph(final_result)
    final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")
    final_result.close()

def create_en_intro(final_result):
    intro = """<section><h2 class="mrgn-tp-xl" id="visiting">Percentages of Site Visits by Foreign Country</h2>
    <p>This graph illustrates the percentage of total of visits the Open Government Portal has by foreign country.</p>
    <table class="wb-charts wb-charts-pie table" style="display: none;" data-flot='{"series": { "pie": { "radius": 1,"label": { "radius": 1,"show": true, "threshold": 0.01 }, "innerRadius": 0.35 } }, "grid": { "hoverable": true }, "legend": {"show":false} } ' data-wb-charts='{ "height": 550, "decimal": 1, "noencapsulation": true }'>
    <caption>Percentages of Site Visits by Foreign Country</caption><thead><tr><th>&nbsp;</th>\n"""
    final_result.write(intro)

def create_fr_intro(final_result):
    intro = """<section><h2 class="mrgn-tp-xl" id="visiting">Pourcentages des visites du site de provenance étrangère</h2>
    <p>Ce graphique illustre le pourcentage du total des visites du portail du gouvernement ouvert de provenance étrangère.</p>
    <table class="wb-charts wb-charts-pie table" style="display: none;" data-flot='{"series": { "pie": { "radius": 1,"label": { "radius": 1,"show": true, "threshold": 0.01 }, "innerRadius": 0.35 } }, "grid": { "hoverable": true }, "legend": {"show":false} } ' data-wb-charts='{ "height": 550, "decimal": 1, "noencapsulation": true }'>
    <caption>Pourcentages des visites du site de provenance étrangère</caption><thead><tr><th>&nbsp;</th>\n"""
    final_result.write(intro)

def get_country_en(final_result):
    country_en = ""

    with open("openDataPortal.siteAnalytics.internationalUsageBreakdown.bilingual.csv", 'r') as f:
        country_csv = csv.reader(f)
        next(country_csv, None)
        next(country_csv, None)

        for x in range(10):
            row = next(country_csv, None)
            country_en = re.split('\| |, |\/', row[0])[0]
            final_result.write("<th scope=\"col\">"+ country_en + "</th>\n")
    final_result.write("<th scope=\"col\">Other</th></tr></thead><tbody><tr><th scope=\"row\">Percentages of Site Visits by Foreign Country</th>")


def get_country_fr(final_result):
    country_fr = ""

    with open("openDataPortal.siteAnalytics.internationalUsageBreakdown.bilingual.csv", 'r', encoding='utf-8') as f:
        country_csv = csv.reader(f)
        next(country_csv, None)
        next(country_csv, None)

        for x in range(10):
            row = next(country_csv, None)
            country_fr = re.split('\| |, |\/', row[0])[1]
            final_result.write("<th scope=\"col\">"+ country_fr + "</th>\n")
    final_result.write("<th scope=\"col\">Autres</th></tr></thead><tbody><tr><th scope=\"row\">Pourcentages des visites du site de provenance étrangère</th>")

def create_en_graph(final_result):
    count = 0
    total = 0.0

    with open("openDataPortal.siteAnalytics.internationalUsageBreakdown.bilingual.csv", 'r') as f:
        country_csv = csv.reader(f)
        next(country_csv, None)
        next(country_csv, None)
        decimal = 0.0

        for x in range(10):
            big_total = total_all()
            row = next(country_csv, None)
            decimal = round(float((float(row[1])/big_total)*100), 2)
            final_result.write("<td class=\"text-center\">"+ str(decimal) + "</td>\n")
            count += int(row[1])
            total += decimal

    final_result.write("<td class=\"text-center\">" + str(100-total) + "</td>")
    final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")
    
    final_result.write("""<div class="table-responsive"><table class="table"><caption class="text-left"><strong>Total and percentages of Site Visits by Foreign Country</strong></caption>
    <thead><tr><th class="text-center" style="width: 50px;" scope="col">Chart colour</th><th class="text-left" scope="col">Country</th><th class="text-center" scope="col">Visits</th><th class="text-center" scope="col">Percentage of Total Visits</th></tr></thead>
    <tfoot><tr><th class="text-left" colspan="2" scope="row">Total Number of Visits by Foreign Countries</th><td class="text-center"><strong>""" + '{:,}'.format(big_total) + """</strong></td><td>&nbsp;</td></tr></tfoot><tbody>""")

    with open("openDataPortal.siteAnalytics.internationalUsageBreakdown.bilingual.csv", 'r') as f:
        country_csv = csv.reader(f)
        next(country_csv, None)
        next(country_csv, None)

        for x in range(10):
            row = next(country_csv, None)
            final_result.write("<tr><td class=\"text-left\" style=\"background-color: rgb" + COLOURS[x] +";\">&nbsp;</td><td class=\"text-left\">"+ re.split('\| |, |\/', row[0])[0] + "</td><td class=\"text-center\">" + '{:,}'.format(int(row[1])) + 
            "</td><td class=\"text-center\">" + row[2] + "</td></tr>\n")
        final_result.write("<tr><td class=\"text-left\" style=\"background-color: rgb(134, 174, 202);\">&nbsp;</td><td class=\"text-left\">Other</td><td class=\"text-center\">" + '{:,}'.format(total_all()-count) + "</td><td class=\"text-center\">" + str(100-total) + "%</td></tr>")

def create_fr_graph(final_result):
    count = 0
    total = 0
    with open("openDataPortal.siteAnalytics.internationalUsageBreakdown.bilingual.csv", 'r', encoding='utf-8') as f:
        country_csv = csv.reader(f)
        next(country_csv, None)
        next(country_csv, None)
        decimal = 0.0

        for x in range(10):
            big_total = total_all()
            row = next(country_csv, None)
            decimal = round(float(((float(row[1]))/big_total)*100), 2)
            final_result.write("<td class=\"text-center\">"+ str(decimal) + "</td>\n")
            count += int(row[1])
            total += decimal

    final_result.write("<td class=\"text-center\">" + str(100-total) + "</td>")
    final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")
    
    final_result.write("""<div class="table-responsive"><table class="table"><caption class="text-left"><strong>Total et pourcentages des visites de provenance étrangère</strong></caption>
    <thead><tr><th class="text-center" style="width: 50px;" scope="col">Couleur de la charte</th><th class="text-left" scope="col">Pays</th><th class="text-center" scope="col">Visites</th><th class="text-center" scope="col">Pourcentages du nombre total de visites</th></tr></thead>
    <tfoot><tr><th class="text-left" colspan="2" scope="row">Nombre total de visites de provenance étrangère</th><td class="text-center"><strong>""" + '{:,}'.format(big_total).replace(',', ' ') + """</strong></td><td class="text-center">&nbsp;</td></tr></tfoot><tbody>""")

    with open("openDataPortal.siteAnalytics.internationalUsageBreakdown.bilingual.csv", 'r', encoding='utf-8') as f:
        country_csv = csv.reader(f)
        next(country_csv, None)
        next(country_csv, None)
        fr_value = ""

        for x in range(10):
            row = next(country_csv, None)
            fr_value = row[2].split(".", 1)[0] + "," + row[2].split(".", 1)[1]
            final_result.write("<tr><td class=\"text-left\" style=\"background-color: rgb" + COLOURS[x] +";\">&nbsp;</td><td class=\"text-left\">"+ re.split('\| |, |\/', row[0])[1] + "</td><td class=\"text-center\">" + '{:,}'.format(int(row[1])).replace(',', ' ') + 
            "</td><td class=\"text-center\">" + fr_value + "</td></tr>\n")
        final_result.write("<tr><td class=\"text-left\" style=\"background-color: rgb(134, 174, 202);\">&nbsp;</td><td class=\"text-left\">Autres</td><td class=\"text-center\">" + '{:,}'.format(total_all()-count).replace(',', ' ') + "</td><td class=\"text-center\">" + str(100-total).split(".", 1)[0] + "," + row[2].split(".", 1)[1] + "</td></tr>")

def total_all():
    with open("openDataPortal.siteAnalytics.internationalUsageBreakdown.bilingual.csv", 'r', encoding='utf-8') as f:
        country_csv = csv.reader(f)
        next(country_csv, None)
        next(country_csv, None)
        
        total = 0

        for row in country_csv:
            total += int(row[1])
    return total