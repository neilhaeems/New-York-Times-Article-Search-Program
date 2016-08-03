# takes html text as input and outputs simple text
def convert_text(html_code):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(html_code)
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    print(soup.get_text())

# prints link for nytimes with category term
def site_nytimes(section):
    print("http://www.nytimes.com/pages/" + section + "/index.html")
# we will need to incorporate http://query.nytimes.com/search/sitesearch/?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage#/democrat/

# prints twitter link with search term
def site_twitter(section):
    print("https://twitter.com/search?q=" + section + "&src=typd&lang=en")

# opens website in browser
def open_link(website):
    import webbrowser
    webbrowser.open("http://www." + website + ".com/")

# nytimes API
from nytimesarticle import articleAPI
api = articleAPI('85b8431c544c4ebc87dc462227bfd371')
import requests
import json

article_search_base_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json"


articles = api.search(q = 'Obama', fq = {'headline':'Obama', 'source':['Reuters','AP', 'The New York Times']}, begin_date = 20111231, facet_field = ['source','day_of_week'], facet_filter = True)
