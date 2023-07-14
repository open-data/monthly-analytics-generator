# This reads visits from openDataPortal.siteAnalytics.provincialUsageBreakdown.bilingual.csv
# coding=utf-8

import csv, yaml

COLOURS = ["(143, 31, 23)", "(240, 131, 0)", "(36, 124, 168)", "(91, 46, 108)", "(38, 83, 38)",
"(18, 64, 86)", "(85, 85, 85)", "(247, 212, 0)", "(217, 59, 50)", "(62, 134, 62)", "(134, 174, 202)"
,"(35, 68, 126)", "(153, 153, 153)", "(237, 194, 64)"]

def to_html():
    en_to_html()
    fr_to_html()

def en_to_html():
    final_result = open("percentages_of_site_visits_prov_terr_en.txt", "w")
    create_en_intro(final_result)
    get_prov_terr_en(final_result)
    create_en_graph(final_result)
    final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")
    final_result.close()

def fr_to_html():
    final_result = open("percentages_of_site_visits_prov_terr_fr.txt", "w")
    create_fr_intro(final_result)
    get_prov_terr_fr(final_result)
    create_fr_graph(final_result)
    final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")
    final_result.close()

def create_en_intro(final_result):
    intro = """<section><h2 class="mrgn-tp-xl" id="visitors">Percentages of Site Visits by Province and Territory</h2>			
    <p>This graph illustrates the percentage of total of visits the Open Government Portal has received from Canadian provinces and territories.</p>			
    <table class="wb-charts wb-charts-pie table" style="display: none;" data-flot='{"series": { "pie": { "radius": 1,"label": { "radius": 1,"show": true, "threshold": 0.01 }, "innerRadius": 0.35 } }, "grid": { "hoverable": true }, "legend": {"show":false} } ' data-wb-charts='{ "height": 550, "decimal": 1, "noencapsulation": true }'>			
    <caption>Percentages of Site Visits by Province and Territory</caption><thead><tr><th>&nbsp;</th>\n"""
    final_result.write(intro)

def create_fr_intro(final_result):
    intro = """<section><h2 class="mrgn-tp-xl" id="visitors">Pourcentages des visites du site par province et territoire</h2>
    <p>Ce graphique illustre le pourcentage du total des visites du portail du gouvernement ouvert par province et territoire.</p>
    <table class="wb-charts wb-charts-pie table" style="display: none;" data-flot='{"series": { "pie": { "radius": 1,"label": { "radius": 1,"show": true, "threshold": 0.01 }, "innerRadius": 0.35 } }, "grid": { "hoverable": true }, "legend": {"show":false} } ' data-wb-charts='{ "height": 550, "decimal": 1, "noencapsulation": true }'>
    <caption>Pourcentages des visites du site par province et territoire</caption><thead><tr><th>&nbsp;</th>\n"""
    final_result.write(intro)

def get_prov_terr_en(final_result):
    final_result_string = []
    prov_terr_en = ""

    with open("openDataPortal.siteAnalytics.provincialUsageBreakdown.bilingual.csv", 'r') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)

        for row in monthly_usage:
            prov_terr_en = row[0].split("|", 1)[0]
            final_result.write("<th scope=\"col\">"+ prov_terr_en + "</th>\n")
    final_result.write("</tr></thead><tbody><tr><th scope=\"row\">Percentages of Site Visits by Province and Territory</th>")


def get_prov_terr_fr(final_result):
    final_result_string = []
    prov_terr_fr = ""

    with open("openDataPortal.siteAnalytics.provincialUsageBreakdown.bilingual.csv", 'r', encoding='utf-8') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)

        for row in monthly_usage:
            prov_terr_fr = row[0].split("|", 1)[1]
            final_result.write("<th scope=\"col\">"+ prov_terr_fr + "</th>\n")
    final_result.write("</tr></thead><tbody><tr><th scope=\"row\">Pourcentages des visites du site par province et territoire</th>")

def create_en_graph(final_result):
    count = 0

    with open("openDataPortal.siteAnalytics.provincialUsageBreakdown.bilingual.csv", 'r', encoding='utf-8') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)
        decimal = 0.0

        for row in monthly_usage:
            decimal = float(row[2].split("%", 1)[0])/100
            final_result.write("<td class=\"text-center\">"+ str(decimal) + "</td>\n")
            count += int(row[1])

    final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")
    
    final_result.write("""<div class="table-responsive"><table class="table"><caption class="text-left"><strong>Total and percentages of site visits by Province and Territory</strong></caption>
    <thead><tr><th class="text-center" style="width: 50px;" scope="col">Chart colour</th><th class="text-left" scope="col">Region</th><th class="text-center" scope="col">Visits</th><th class="text-center" scope="col">Percentage of Total Visits</th></tr></thead>
    <tfoot><tr><th class="text-left" colspan="2" scope="row">Total Number of Visits in Canada</th><td class="text-center"><strong>""" + '{:,}'.format(count) + """</strong></td><td class="text-center">&nbsp;</td></tr></tfoot><tbody>""")

    with open("openDataPortal.siteAnalytics.provincialUsageBreakdown.bilingual.csv", 'r', encoding='utf-8') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)
        count = 0

        for x in range(14):
            row = next(monthly_usage, None)
            final_result.write("<tr><td class=\"text-left\" style=\"background-color: rgb"+ COLOURS[x] +";\">&nbsp;</td><td class=\"text-left\">"+ row[0].split("|", 1)[0] + "</td><td class=\"text-center\">" + '{:,}'.format(int(row[1])) + 
            "</td><td class=\"text-center\">" + row[2] + "</td></tr>\n")
            

def create_fr_graph(final_result):
    count = 0
    with open("openDataPortal.siteAnalytics.provincialUsageBreakdown.bilingual.csv", 'r', encoding='utf-8') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)
        decimal = 0.0

        for row in monthly_usage:
            decimal = float(row[2].split("%", 1)[0])/100
            final_result.write("<td class=\"text-center\">"+ str(decimal) + "</td>\n")
            count += int(row[1])

    final_result.write("</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")
    
    final_result.write("""<div class="table-responsive"><table class="table"><caption class="text-left"><strong>Total et pourcentages des visites par province et territoire</strong></caption>
    <thead><tr><th class="text-center" style="width: 50px;" scope="col">Couleur de la charte</th><th class="text-left" scope="col">Région</th><th class="text-center" scope="col">Visites</th><th class="text-center" scope="col">Pourcentages du nombre total de visites</th></tr></thead>
    <tfoot><tr><th class="text-left" colspan="2" scope="row">Nombre total de visiteurs au Canada</th><td class="text-center"><strong>""" + '{:,}'.format(count).replace(',', ' ') + """</strong></td><td class="text-center">&nbsp;</td></tr></tfoot><tbody>""")

    with open("openDataPortal.siteAnalytics.provincialUsageBreakdown.bilingual.csv", 'r', encoding='utf-8') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)
        fr_value = ""
        count = 0

        for x in range(14):
            row = next(monthly_usage, None)
            fr_value = row[2].split(".", 1)[0] + "," + row[2].split(".", 1)[1]
            final_result.write("<tr><td class=\"text-left\" style=\"background-color: rgb" + COLOURS[x] +";\">&nbsp;</td><td class=\"text-left\">"+ row[0].split("|", 1)[1] + "</td><td class=\"text-center\">" + '{:,}'.format(int(row[1])).replace(',', ' ') + 
            "</td><td class=\"text-center\">" + fr_value + "</td></tr>\n")
            
        


