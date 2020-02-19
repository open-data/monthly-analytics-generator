import monthly_visits, monthly_downloads,top_25, dep_or_agency, datasets_released_by_month, os
import percentages_of_site_visits_by_foreign_country, percentages_of_site_vistis_prov_terr, percentages_of_site_visits_by_country

def main():
    monthly_visits.to_html()
    monthly_downloads.to_html()
    top_25.to_html()
    dep_or_agency.to_html()
    datasets_released_by_month.to_html()
    percentages_of_site_vistis_prov_terr.to_html()
    percentages_of_site_visits_by_country.to_html()
    percentages_of_site_visits_by_foreign_country.to_html()

def final_html_en():
    filenames = ['monthly_visits.txt', 'monthly_downloads.txt', 'top_25.txt', 
        'dep_or_agency.txt', 'datasets_released_by_month.txt', 'percentages_of_site_vistis_prov_terr.txt',
        'percentages_of_site_visits_by_country.txt']
    with open('final_html_en.txt', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

def final_html_fr():
    filenames = ['monthly_visits.txt', 'monthly_downloads.txt', 'top_25.txt', 
        'dep_or_agency.txt', 'datasets_released_by_month.txt', 'percentages_of_site_vistis_prov_terr.txt',
        'percentages_of_site_visits_by_country.txt']
    with open('final_html_fr.txt', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

def delete_separate_txts():
    directory = os.getcwd()
    for item in directory:
        if not item.startswith("final_html") and item.endswith(".txt"):
            os.remove(os.path.join(directory, item))


main()