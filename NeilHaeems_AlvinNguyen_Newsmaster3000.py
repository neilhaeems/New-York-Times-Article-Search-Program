import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# lines 4-6: lists of appropriate search terms and subcategories for NYT
search_terms = ["world", "US", "politics", "nyregion", "business", "technology", "science", "health", "sports", "education", "obituaries", "todayspaper"]
sub_categories = {'africa':'world/africa', 'americas':'world/americas', 'asia':'world/asia', 'europe':'world/europe', 'middle east':'world/middleeast', 'dealbook':'dealbook', 'markets':'research/markets', 'economy':'business/economy', 'energy and environment':'business/energy-environment', 'media':'business/media', 'personal tech':'technology/personaltech', 'entreprenuership':'smallbusiness', 'environment':'science/earth', 'space':'science/space', 'cosmos':'science/space'}

# takes url as input and outputs html
def convert_text(url):
    response = requests.get(url)
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    link_only = soup.h2.a
    return link.get('href')

# soup.get_text()

# returns link for nytimes with category term
def site_nytimes(section):
    search_url = "http://www.nytimes.com/pages/" + str(section) + "/index.html"
    return search_url

# takes in html file of category page and returns url of specific article
def get_article(html_file):
    html_doc = str(html_file)
    only_h2_tags = SoupStrainer("h2")
    return (BeautifulSoup(html_doc, "html.parser", parse_only=only_h2_tags).prettify())

# returns date of article on NYT
def date_article(url):
    response = requests.get(url)
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    date = soup.p.string
    print(date[1:-1])

# returns link for nytimes with subcategory term
def site_nytimes_sub(section):
    search_url = "http://www.nytimes.com/pages/" + sub_categories[section] + "/index.html"
    return search_url

# given NYT category page, returns list of h2 and h3 links
#def link_lister(search_url):
    

# returns twitter link with search term
def site_twitter(section):
    return "https://twitter.com/search?q=" + section + "&src=typd&lang=en"

# opens website in browser
def open_link(website):
    import webbrowser
    webbrowser.open("http://www." + website + ".com/")

# nytimes API
from nytimesarticle import articleAPI
api = articleAPI('85b8431c544c4ebc87dc462227bfd371')
import requests
import json

# user interface for final project - this is what users interact with
print("Welcome to Newsmaster 3000!")
repeat = True
while repeat == True:
    source = input("Input a search term for a news article: ")
    if source in search_terms:
        site_nytimes(source)
        print("categories work")
        # run url into h2 and h3 finder
        # get first h2 html file
        # simplify html file
        # print snippet
        # ask user option - more articles, read full article, twitter
    elif source in sub_categories:
        site_nytimes_sub(source)
        print("sub categories work")
        # run url into h2 and h3 finder
        # get first h2 html file
        # simplify html file
        # print snippet
        # ask user option - more articles, read full article, twitter
    elif source == "exit" or source == "exit()":
        repeat = False
    else:
        print("Invalid search term. Please try again.")
        