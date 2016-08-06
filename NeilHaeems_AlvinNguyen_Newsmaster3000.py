import requests
import webbrowser
from bs4 import BeautifulSoup
from bs4 import SoupStrainer


# lines 6-10: lists of appropriate search terms and subcategories
search_terms = ("world", "US", "politics", "nyregion", "business", "technology", "science", "health", "sports", "education", "obituaries", "todayspaper");
sub_categories = {'africa':'world/africa', 'americas':'world/americas', 'asia':'world/asia', 'europe':'world/europe', 'middle east':'world/middleeast', 'dealbook':'dealbook', 'markets':'research/markets', 'economy':'business/economy', 'energy and environment':'business/energy-environment', 'media':'business/media', 'personal tech':'technology/personaltech', 'entreprenuership':'smallbusiness', 'environment':'science/earth', 'space':'science/space', 'cosmos':'science/space', 'tech': "technology"}
appropriate_another_article = ("another", "another article", "similar", "similar article", "another similar article", "read another similar article");
appropriate_full_article = ("full", "full article", "open", "open in browser", "browser", "open the full article");
appropriate_social_media = ("social media", "twitter", "posts", "read social media posts", "read social media posts about this topic");
appropriate_search_again = ("search again", "new search", "new term", "search new article", "new article");


# returns link for nytimes with category term
def site_nytimes(section):
    search_url = "http://www.nytimes.com/pages/" + str(section) + "/index.html"
    return str(search_url)


# returns link for nytimes with subcategory term
def site_nytimes_sub(section):
    search_url = "http://www.nytimes.com/pages/" + sub_categories[section] + "/index.html"
    return str(search_url)


# returns twitter link with search term
def site_twitter(section):
    return str("https://twitter.com/search?q=" + section + "&src=typd&lang=en")


# takes url as input, converts to html, parses, and finds article url
def get_article(url):
    response = requests.get(url)
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    try:
        link_only = soup.h2.a
    except AttributeError:
        link_only = soup.h3.a
    return link_only.get('href')


# opens website in browser
def open_link(website):
    webbrowser.open(website)


# returns date of article on NYT
def date_article(url):
    response = requests.get(url)
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    date = soup.p.string
    print(date[1:-1])

# gives user options for what to do after they read an article
def what_next():
    ask_again = True
    while ask_again == True:
        next_step = input("Do you want to read another similar article, search again, open the full article, or see social media posts about this topic?: ").lower()
        if next_step in appropriate_search_again:
            ask_again = False
        elif next_step in appropriate_another_article:
            #run another article
            pass
        elif next_step in appropriate_full_article:
            open_link(article)
            ask_again = False
        elif next_step in appropriate_social_media:
            #print twitter post
            pass
        elif next_step == "exit" or next_step == "exit()":
            ask_again = False
            repeat = False
        else:
            print("Sorry, your input was not valid")


# given NYT category page, returns list of h2 and h3 links
#def link_lister(search_url):
    




##------------------------------------------------------------------------------##

# user interface for final project - this is what users interact with
print("Welcome to Newsmaster 3000!")
repeat = True
while repeat == True:
    source = input("Input a search term for a news article: ").lower()
    if source in search_terms:
        url = site_nytimes(source)
        article = get_article(url)
        print(article)
        # article is parsed
        # print snippet
        what_next()
    elif source in sub_categories:
        url = site_nytimes_sub(source)
        article = get_article(url)
        print(article)
        # aricle is parsed
        # print snippet
        what_next()
    elif source == "exit" or source == "exit()":
        repeat = False
    else:
        print("Invalid search term. Please try again.")
        