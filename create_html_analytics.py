import monthly_visits, monthly_downloads,top_25, dep_or_agency
import datasets_released_by_month, percentages_of_site_vistis_prov_terr, percentages_of_site_visits_by_country

def main():
    monthly_visits.to_html()
    monthly_downloads.to_html()
    top_25.to_html()
    dep_or_agency.to_html()
    datasets_released_by_month.to_html()
    percentages_of_site_vistis_prov_terr.to_html()
    percentages_of_site_visits_by_country.to_html()


main()