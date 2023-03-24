import requests
from bs4 import BeautifulSoup
product_code = input("Podaj kod produktu: ")
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
respons = requests.get(url)
if respons.status_code == requests.codes.ok:
    page_dom = BeautifulSoup(respons.text, 'html.parser')
    opinions = page_dom.select("div.js_product-review")
    if len(opinions) > 0:
        opinions_all = []
        for opinion in opinions:
            single_opinion = {
                "opinion_id": "", #opinion.dataset.entryId
                "author": "", #.user-post__author-name
                "recomendation": "", #.recommended
                "stars": "", #.score-marker[style]
                "purchased": "", #.review-pz[title]
                "opinion_date": "", #.user-post__published:first-child[datetime]
                "purchase_date": "", #.user-post__published:last-child[datetime]
                "usefull_count": "", #.vote-yes[data-vote]
                "unusefull_count": "", #.vote-yes[data-vote]
                "content": "", #.user-post__text
                "pros": "", #review-feature__col 
                "cons": "", #review-feature__col
            }