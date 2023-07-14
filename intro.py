# coding=utf-8
import datetime, yaml

def to_html():
    create_en_intro()
    create_fr_intro()

def create_en_intro():
    final_result = open("intro_en.txt", "w")
    dt = datetime.datetime.today()
    today = dt.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    intro = """<style type="text/css">.legendColorBox{width:30px;}</style>
    <p>Explore the ways we track the progress of Open Government. Browse through statistics on download counts, visitors, as well as the increase of participation of Government of Canada departments and agencies in supplying more open datasets. 
    All statistics presented, unless otherwise noted, are as of <time datetime="2013-06-18">June&nbsp;18,&nbsp;2013</time> to <span class="nowrap"><time datetime=\"""" + lastMonth.strftime("%Y-%m-%d") +"\">" + lastMonth.strftime("%B %d, %Y") + """</time></span>. 
    To access the open data used to create the tables below, visit <a href="/data/en/dataset/2916fad5-ebcc-4c86-b0f3-4f619b29f412">Open Government Analytics</a>.</p>\n
    
    <section><div class="panel panel-default mrgn-tp-lg">
    <div class="panel-heading"><h2 class="panel-title">Table of Contents</h2></div>
    <div class="panel-body"><ul><li><a href="#visits">Number of visits</a></li>
    <li><a href="#downloads">Number of Downloads</a></li>
    <li><a href="#top10">Top 25 Downloaded Datasets</a></li>
    <li><a href="#department">Datasets by Department or Agency</a></li>
    <li><a href="#monthly">Datasets Released by Month</a></li>
    <li><a href="#visitors">Percentages of Site Visits by Province and Territory</a></li>
    <li><a href="#country">Percentages of Site Visits by Country</a></li>
    <li><a href="#visiting">Percentages of Site Visits by Foreign Country</a></li></ul></div>
    </div><div class="clearfix">&nbsp;</div></section>\n"""
    final_result.write(intro)
    final_result.close()

def create_fr_intro():
    final_result = open("intro_fr.txt", "w")
    dt = datetime.datetime.today()
    today = dt.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)

    months = yaml.full_load(open('months.yml', 'r'))
    french_month = months.get('long_form').get(lastMonth.strftime("%B"))
    french_date = lastMonth.strftime("%d ") + french_month + lastMonth.strftime(", %Y")

    intro = """<style type="text/css">.legendColorBox{width:30px;}</style>
    <p>Exploiter les moyens par l'entremise desquels nous effectuons le suivi des progrès du gouvernement ouvert. Parcourir les statistiques relatives au décompte de téléchargements, les visiteurs, de même que l'augmentation des contributions en matière de données que les ministères et les organismes du GC apportent au portail. 
    À moins d'indication contraire, toutes les statistiques présentées ont été récoltées du <time datetime="2013-06-18">18&nbsp;juin&nbsp;2013</time> au <span class="nowrap"><time datetime=\"""" + lastMonth.strftime("%Y-%m-%d") +"\">"+ french_date + """</time></span>. 
    Pour accéder aux données ouvertes qui ont été utilisées pour créer les tableaux ci-dessous, veuillez visiter <a href="/data/fr/dataset/2916fad5-ebcc-4c86-b0f3-4f619b29f412">Analyses concernant le gouvernement ouvert</a>.</p>

    <section><div class="panel panel-default mrgn-tp-lg">
    <div class="panel-heading"><h2 class="panel-title">Table des matières</h2></div>
    <div class="panel-body"><ul><li><a href="#visits">Nombre de visites</a></li>
    <li><a href="#downloads">Nombre de téléchargements</a></li>
    <li><a href="#top10">Les 25 principaux jeux de données téléchargés</a></li>
    <li><a href="#department">Jeux de données par ministère ou organisme</a></li>
    <li><a href="#monthly">Jeux de données publiés par mois</a></li>
    <li><a href="#visitors">Pourcentages des visites du site par province et territoire</a></li>
    <li><a href="#country">Pourcentages des visites du site par pays</a></li>
    <li><a href="#visiting">Pourcentages des visites du site de provenance étrangère</a></li></ul></div>
    </div><div class="clearfix">&nbsp;</div></section>\n"""
    final_result.write(intro)
    final_result.close()