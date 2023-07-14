# coding=utf-8
import monthly_visits, monthly_downloads,top_25, dep_or_agency, datasets_released_by_month, intro,down_files, os, datetime, yaml
import percentages_of_site_visits_by_foreign_country, percentages_of_site_vistis_prov_terr, percentages_of_site_visits_by_country

def main():
    down_files.filedownload()
    intro.to_html()
    monthly_visits.to_html()
    monthly_downloads.to_html()
    top_25.to_html()
    dep_or_agency.to_html()
    datasets_released_by_month.to_html()
    percentages_of_site_vistis_prov_terr.to_html()
    percentages_of_site_visits_by_country.to_html()
    percentages_of_site_visits_by_foreign_country.to_html()
    final_html_en()
    final_html_fr()
    down_files.csv_files_remove()

def final_html_en():
    filenames = ['intro_en.txt', 'monthly_visits_en.txt', 'monthly_downloads_en.txt', 'top_25_en.txt', 
        'dep_or_agency_en.txt', 'datasets_released_by_month_en.txt', 'percentages_of_site_visits_prov_terr_en.txt',
        'percentages_of_site_visits_country_en.txt', 'percentages_of_site_visits_by_foreign_country_en.txt']
    with open('final_html_en.txt', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
                infile.close
            os.remove(fname)

def final_html_fr():
    filenames = ['intro_fr.txt','monthly_visits_fr.txt', 'monthly_downloads_fr.txt', 'top_25_fr.txt', 
        'dep_or_agency_fr.txt', 'datasets_released_by_month_fr.txt', 'percentages_of_site_visits_prov_terr_fr.txt',
        'percentages_of_site_visits_country_fr.txt', 'percentages_of_site_visits_by_foreign_country_fr.txt']
    with open('final_html_fr.txt', 'w', encoding="utf-8") as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
                infile.close
            os.remove(fname)

main()