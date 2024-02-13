# coding=utf-8
# This reads visits from openDataPortal.siteAnalytics.datasetsByOrgByMonth.bilingual.csv

import datetime
import yaml
from dateutil import relativedelta
import pandas as pd


def to_html():
   # to add hyperlinks as well
    today = datetime.date.today()
    start_month = today.month

    # Loading unpivoted datasets released by org by month and extracting only last 12 months, then pivoted
    df_ByOryByMonth = pd.read_csv(
        "opendataportal.siteanalytics.datasetsbyorgbymonth.bilingual_new.csv", encoding="utf-8")
    df_ByOryByMonth.query(
        f'{start_month}<=month_mois <= 12  and year_annee == {today.year - 1} or 1 <= month_mois < {start_month} & year_annee == {today.year}', inplace=True)
    df_ByOryByMonth.drop(['year_annee'], axis=1, inplace=True)
    df_pivot = df_ByOryByMonth.pivot(
        index=["department_ministere", "links_liens"], columns="month_mois")
    df_pivot = df_pivot['datasets_jeux_de_donnees'].reset_index()
    df_pivot.columns.name = None

    # Adding a partial total column for the last 12 months datatset release
    df_pivot['total'] = df_pivot.sum(axis=1, skipna=True, numeric_only=True)
   

    # Loading dataset released by org to get total datasets released prior than 12 months by org
    df_byOrg = pd.read_csv(
        "opendataportal.siteanalytics.datasetsbyorg.bilingual.csv", encoding="utf-8")
    df_byOrg["department_ministere"] = df_byOrg['department'] + \
        ' | ' + df_byOrg['ministere']
    df_byOrg.drop(['department', 'ministere', 'datasets',
                  'jeux_de_donnees'], axis=1, inplace=True)
    df_merged = df_pivot.merge(df_byOrg, how='left', on="department_ministere")
    #df_merged.to_csv('test_merged.csv', index=False)
    df_merged = df_merged.convert_dtypes()
    df_merged['prior'] = df_merged['total_y'] - df_merged['total_x']

    # droping partial totals and generating total per organization including prior releases
    df_merged.drop(['total_y', 'total_x'], axis=1, inplace=True)
    df_merged['total'] = df_merged.sum(axis=1, skipna=True, numeric_only=True)

    # Drop na will remove Canadian Institute of Health Information datasets which is no longer tracked in our Search.
    df_merged.dropna(inplace=True)

    # Generating total per columns to reflect total release per month.
    total_merge = df_merged.sum(axis=0, skipna=True, numeric_only=True)
    row_merge = total_merge.to_list()
    row_merge.insert(0, "Total")
    row_merge.insert(1, "")
    df_merged.loc[len(df_pivot.index)] = row_merge
    df_merged.reset_index(drop=True, inplace=True)
    df_merged = df_merged.convert_dtypes()
    #df_merged.to_csv('df_merged.csv', index=False)

    # Columns reordering  
    month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
    reorder_month = []    
    for x in range (12):        
        reorder_month.append(month_list[(start_month-1 +x)%12])
    df_merged = df_merged[['department_ministere', 'links_liens',
                           'prior', reorder_month[0], reorder_month[1], reorder_month[2], reorder_month[3],
                             reorder_month[4], reorder_month[5], reorder_month[6], reorder_month[7], reorder_month[8],
                               reorder_month[9], reorder_month[10], reorder_month[11], 'total']]
    en_to_html(df_merged)
    fr_to_html(df_merged)


def en_to_html(df_merged):
    final_result = open("datasets_released_by_month_en.txt", "w")
    create_intro_en(final_result)
    format_dates_en(final_result)
    get_rows_en(final_result, df_merged)
    final_result.close()


def fr_to_html(df_merged):
    final_result = open("datasets_released_by_month_fr.txt", "w")
    create_intro_fr(final_result)
    format_dates_fr(final_result)
    get_rows_fr(final_result, df_merged)
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


def get_rows_en(final_result, df_pivot):
    
    
    for index, row in df_pivot.iterrows():
        row = row.tolist()
        url = row[1].split("|", 1)[0]
        org = row[0].split("|", 1)[0]
        if(url != ""):
            final_result.write("<tr><th scope=\"row\"><a href=\"" + url + "\">" + org + "</a></th><td class=\"text-left\">" + '{:,}'.format(int(row[2])) + "</th><td class=\"text-left\">"
                            + '{:,}'.format(int(row[3])) + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[4])) + "</td><td class=\"text-left\">" + '{:,}'.format(
                                int(row[5])) + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[6])) + "</td><td class=\"text-left\">"
                            + '{:,}'.format(int(row[7])) + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[8])) + "</td><td class=\"text-left\">" +
                            '{:,}'.format(int(row[9])) + "</td><td class=\"text-left\">" + '{:,}'.format(
                                int(row[10])) + "</td><td class=\"text-left\">"
                            + '{:,}'.format(int(row[11])) + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[12])) + "</td><td class=\"text-left\">" + '{:,}'.format(
                                int(row[13])) + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[14]))+"</td><td class=\"text-left\">"
                            + '{:,}'.format(int(row[15])) + "</td></tr>")
        else:
            #print ("english exception")
            final_result.write("<tr><th scope=\"row\">"+ org +"</th><td class=\"text-left\">" + '{:,}'.format(int(row[2])) + "</th><td class=\"text-left\">"
                                + '{:,}'.format(int(row[3])) + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[4])) + "</td><td class=\"text-left\">" + '{:,}'.format(
                                    int(row[5])) + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[6])) + "</td><td class=\"text-left\">"
                                + '{:,}'.format(int(row[7])) + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[8])) + "</td><td class=\"text-left\">" + '{:,}'.format(
                                    int(row[9])) + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[10])) + "</td><td class=\"text-left\">"
                                + '{:,}'.format(int(row[11])) + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[12])) + "</td><td class=\"text-left\">" + '{:,}'.format(
                                    int(row[13])) + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[14]))+"</td><td class=\"text-left\">"
                                + '{:,}'.format(int(row[15])) + "</td></tr>")
    final_result.write(
        "</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")


def get_rows_fr(final_result, df_pivot):
   
    try:
        for index, row in df_pivot.iterrows():
            row = row.tolist()
            url = row[1].split("|", 1)[1]
            org = row[0].split("|", 1)[1]
            final_result.write("<tr><th scope=\"row\"><a href=\"" + url + "\">" + org + "</a></th><td class=\"text-left\">" + '{:,}'.format(int(row[2])).replace(',', ' ') + "</th><td class=\"text-left\">"
                               + '{:,}'.format(int(row[3])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[4])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(
                                   int(row[5])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[6])).replace(',', ' ') + "</td><td class=\"text-left\">"
                               + '{:,}'.format(int(row[7])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[8])).replace(',', ' ') + "</td><td class=\"text-left\">" +
                               '{:,}'.format(int(row[9])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(
                                   int(row[10])).replace(',', ' ') + "</td><td class=\"text-left\">"
                               + '{:,}'.format(int(row[11])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[12])).replace(',', ' ') + "</td><td class=\"text-left\">" +
                               '{:,}'.format(int(row[13])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(
                                   int(row[14])).replace(',', ' ')+"</td><td class=\"text-left\">"
                               + '{:,}'.format(int(row[15])).replace(',', ' ') + "</td></tr>")
    except:
        #print("french exception")
        final_result.write("<tr><th scope=\"row\">"+ org +"</th><td class=\"text-left\">" + '{:,}'.format(int(row[2])).replace(',', ' ') + "</th><td class=\"text-left\">"
                           + '{:,}'.format(int(row[3])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[4])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(
                               int(row[5])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[6])).replace(',', ' ') + "</td><td class=\"text-left\">"
                           + '{:,}'.format(int(row[7])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[8])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(
                               int(row[9])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[10])).replace(',', ' ') + "</td><td class=\"text-left\">"
                           + '{:,}'.format(int(row[11])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[12])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(
                               int(row[13])).replace(',', ' ') + "</td><td class=\"text-left\">" + '{:,}'.format(int(row[14])).replace(',', ' ') + "</td><td class=\"text-left\">"
                           + '{:,}'.format(int(row[15])).replace(',', ' ')+"</td></tr>")
    final_result.write(
        "</tbody></table></div><div class=\"clearfix\">&nbsp;</div></section>")


def format_dates_en(final_result):
    df_pivot = datetime.datetime.today()
    today = df_pivot.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)
    lastYear = (datetime.datetime.now() -
                datetime.timedelta(days=364)).replace(day=1)
    final_result_string = []
    final_result_string.append("<th scope=\"col\">Prior to <time datetime=\"" + lastYear.strftime(
        "%Y-%m-%d") + "\"></time>" + lastYear.strftime("%b-%Y") + "</th>\n")    
    for x in range(0, 12):
        time_date = (datetime.datetime.strptime(
            str(lastYear + relativedelta.relativedelta(months=x)), '%Y-%m-%d %H:%M:%S.%f'))
        string_date = time_date.strftime("%Y-%m").split(" ", 1)[0]
        word_date = time_date.strftime("%b-%Y")
        # print(string_date)
        final_result_string.append(
            "<th scope=\"col\"><time datetime=\"" + string_date + "\">" + word_date + "</time></th>\n")
    for line in final_result_string:
        final_result.write(line)
    final_result.write(
        "<th scope=\"col\">Total number of new datasets</th>\n</tr></thead><tbody>")


def format_dates_fr(final_result):
    df_pivot = datetime.datetime.today()
    today = df_pivot.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)
    lastYear = (datetime.datetime.now() -
                datetime.timedelta(days=364)).replace(day=1)
    months = yaml.full_load(open('months.yml', 'r', encoding='utf-8'))
    french_month = months.get('short_form').get(today.strftime("%b"))
    french_date = french_month + lastYear.strftime("- %Y")
    final_result_string = []
    final_result_string.append("<th scope=\"col\">Avant <time datetime=\"" +
                               lastYear.strftime("%Y-%m-%d") + "\"></time>" + french_date + "</th>\n")
    
    for x in range(0, 12):
        time_date = (datetime.datetime.strptime(
            str(lastYear + relativedelta.relativedelta(months=x)), '%Y-%m-%d %H:%M:%S.%f'))
        string_date = time_date.strftime("%Y-%m").split(" ", 1)[0]
        french_date = months.get('short_form').get(time_date.strftime("%b"))
        word_date = french_date + time_date.strftime("- %Y")
        final_result_string.append(
            "<th scope=\"col\"><time datetime=\"" + string_date + "\">" + word_date + "</time></th>\n")
    for line in final_result_string:
        final_result.write(line)
    final_result.write(
        "<th scope=\"col\">Nombre de nouveaux jeux de données</th>\n</tr></thead><tbody>")
