# coding=utf-8
# This reads downloads from openDataPortal.siteAnalytics.totalMonthlyUsage.bilingual.csv

import csv

def to_html():
    en_to_html()
    fr_to_html()

def en_to_html():
    final_result = open("monthly_downloads_en.txt", "w")
    create_intro_en(final_result)
    format_dates_en(final_result)
    get_downloads_en(final_result)
    final_result.close()

def fr_to_html():
    final_result = open("monthly_downloads_fr.txt", "w")
    format_dates_fr(final_result)
    get_downloads_fr(final_result)
    final_result.close()


def get_downloads_en(final_result):
    final_result_string = []

    with open("openDataPortal.siteAnalytics.totalMonthlyUsage.bilingual.csv", 'r') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)

        final_result_string = []
        final_result.write("</tr></thead><tbody><tr>\n")
        final_result.write("<th scope=\"row\" data-flot='{\"color\":\"#2572B4\"}'>Downloads</th>\n")

        for row in monthly_usage:
            final_result_string.append("<td class=\"text-left\">" + '{:,}'.format(int(row[3])) + "</td>\n")
        final_result_string.reverse()
        del final_result_string[0:len(final_result_string) - 12]
        for line in final_result_string:
            final_result.write(line)

        final_result.write("</tr></tbody></table><div class=\"clearfix\">&nbsp;</div></section>\n")

def get_downloads_fr(final_result):
    final_result_string = []

    with open("openDataPortal.siteAnalytics.totalMonthlyUsage.bilingual.csv", 'r') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)

        final_result_string = []
        final_result.write("</tr></thead><tbody><tr>\n")
        final_result.write("<th scope=\"row\" data-flot='{\"color\":\"#2572B4\"}'>Téléchargements</th>\n")

        for row in monthly_usage:
            final_result_string.append("<td class=\"text-left\">" + '{:,}'.format(int(row[3])).replace(',', ' ') + "</td>\n")
        final_result_string.reverse()
        del final_result_string[0:len(final_result_string) - 12]
        for line in final_result_string:
            final_result.write(line)

        final_result.write("</tr></tbody></table><div class=\"clearfix\">&nbsp;</div></section>\n")

def create_intro_en(final_result):
    intro = """<section><h2 class="mrgn-tp-xl" id="downloads">Number of Downloads</h2>
    <p>These numbers summarize the number of downloads on the Open Government Portal. A download represents the number of times a user has clicked to download a resource for a particular dataset.</p>
    <table class="wb-charts table" data-flot='{"legend": {"show":true} }'><caption>Number of Downloads</caption>
    <thead><tr><th>&nbsp;</th>\n"""
    final_result.write(intro)

def create_intro_fr(final_result):
    intro = """<section><h2 class="mrgn-tp-xl" id="downloads">Nombre de téléchargements</h2>
    <p>Voici un graphique représentant le nombre de téléchargements à partir du portail du gouvernement ouvert. Un téléchargement représente le nombre de fois qu'un utilisateur a cliqué pour télécharger une ressource à partir d'un jeu de données en particulier.</p>
    <table class="wb-charts table" data-flot='{"legend": {"show":true} }'><caption>Nombre de téléchargements</caption>
    <thead><tr><th>&nbsp;</th>\n"""
    final_result.write(intro)

def format_dates_en(final_result):
    MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    final_result_string = []

    with open("openDataPortal.siteAnalytics.totalMonthlyUsage.bilingual.csv", 'r') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)

        for row in monthly_usage:
            final_result_string.append("<th scope=\"col\"><time datetime=" + row[0] + "-" + row[1] + ">" + str(MONTHS[int(row[1])-1]) + "-" + row[0] + "</time></th>\n")
        final_result_string.reverse()
        del final_result_string[0:len(final_result_string) - 12]
        for line in final_result_string:
            final_result.write(line)

def format_dates_fr(final_result):
    MONTHS = ["janv.", "févr.", "mars", "avril", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."]
    final_result_string = []

    with open("openDataPortal.siteAnalytics.totalMonthlyUsage.bilingual.csv", 'r') as f:
        monthly_usage = csv.reader(f)
        next(monthly_usage, None)

        for row in monthly_usage:
            final_result_string.append("<th scope=\"col\"><time datetime=" + row[0] + "-" + row[1] + ">" + str(MONTHS[int(row[1])-1]) + " -" + row[0] + "</time></th>\n")
        final_result_string.reverse()
        del final_result_string[0:len(final_result_string) - 12]
        for line in final_result_string:
            final_result.write(line)