#!/bin/bash

if [[ -x "$(command -v wget)" ]]; then

    resources="
        https://open.canada.ca/static/openDataPortal.siteAnalytics.totalMonthlyUsage.bilingual.csv
        https://open.canada.ca/static/openDataPortal.siteAnalytics.datasetsByOrgByMonth.bilingual.csv
        https://open.canada.ca/static/openDataPortal.siteAnalytics.top100Datasets.bilingual.csv
        https://open.canada.ca/static/openDataPortal.siteAnalytics.datasetsByOrg.bilingual.csv
        https://open.canada.ca/static/openDataPortal.siteAnalytics.provincialUsageBreakdown.bilingual.csv
        https://open.canada.ca/static/openDataPortal.siteAnalytics.internationalUsageBreakdown.bilingual.csv
    "

    printf "\n\033[0;36mFetching resources from open.canada.ca\033[0;0m\n\n"
    
    for resource in $resources; do

        wget $resource -O $(echo $resource | sed -E 's/https:\/\/open\.canada\.ca\/static\///g')
    
    done

    printf "\n\033[0;36mDone!\033[0;0m\n\n"

else

    printf "\n\033[0;31mCommand wget not found.\033[0;0m\n\n";

fi
