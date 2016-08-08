import requests
import webbrowser
import random
from datetime import date
from bs4 import BeautifulSoup
from bs4 import SoupStrainer


# lines 6-15: lists, tuples, and dictionaries of appropriate search terms and subcategories, used in functions below
search_terms = ("world", "US", "politics", "nyregion", "business", "technology", "science", "health", "sports", "education", "obituaries", "todayspaper");
sub_categories = {'africa':'world/africa', 'americas':'world/americas', 'asia':'world/asia', 'europe':'world/europe', 'middle east':'world/middleeast', 'dealbook':'dealbook', 'markets':'research/markets', 'economy':'business/economy', 'energy and environment':'business/energy-environment', 'media':'business/media', 'personal tech':'technology/personaltech', 'entrepreneurship':'business/smallbusiness', 'environment':'science/earth', 'space':'science/space', 'cosmos':'science/space', 'tech': "technology"}
appropriate_another_article = ("another", "another article", "similar", "similar article", "another similar article", "read another similar article");
appropriate_full_article = ("full", "full article", "open", "open in browser", "browser", "open the full article");
appropriate_social_media = ("social media", "twitter", "posts", "read social media posts", "read social media posts about this topic");
appropriate_search_again = ("search again", "new search", "new term", "search new article", "new article");
list_of_similar_articles = []


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


# alorithm that takes url as input and returns html file
def html_file(url):
    response = requests.get(url)
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    return soup


# algorithm that takes url as input, converts to html, parses html, and finds url of headlining article
def get_article(url):
    response = requests.get(url)
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    try:
        link_only = soup.h2.a
    except AttributeError:
        link_only = soup.h3.a
    return link_only.get('href')


# algorithm that adds urls to the global variable "list_of_similar_articles", if given search page url
def add_link_to_list(url):
    response = requests.get(url)
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    for link in soup.find_all('a'):
        list_of_similar_articles.append(link.get('href'))
    return (list_of_similar_articles)


# takes in list of URLs from above and keeps only the articles
def keep_links():
    return([str(x) for x in list_of_similar_articles if year_with_slashes() in str(x)])


# returns string of /year/ for next funtion
def year_with_slashes():
    return "/" + str(date.today().year) + "/"


# procedure that chooses random item from list_of_similar_articles for user
def similar_link(list):
    return (random.choice(list))


# opens website in browser
def open_link(website):
    webbrowser.open(website)

# algorithm that returns the title and a description of the article, if given the url for the article
def get_info(url):
    soup = html_file(url)
    title = "Title: " + soup.title.string[:-21]
    snippet = "Description: " + str(soup.find(itemprop="description"))[15:-45]
    print(title + '\n' + snippet)


# twitter


# gives user options for what to do after they read an article
def what_next(page):
    url = str(page)
    ask_again = True
    article = get_article(url)
    while ask_again == True:
        next_step = input("Do you want to read another similar article, search again, open the full article, or see social media posts about this topic?: ").lower()
        if next_step in appropriate_search_again:
            return "search again"
            ask_again = False
        elif next_step in appropriate_another_article:
            x = add_link_to_list(url)
            y = keep_links() 
            url = similar_link(y)
            get_info(url)
        elif next_step in appropriate_full_article:
            open_link(article)
        elif next_step in appropriate_social_media:
            #print twitter post
            pass
            return "social media"
        elif next_step == "exit" or next_step == "exit()":
            return "quit"
            ask_again = False 
        else:
            print("Sorry, your input was not valid")




##------------------------------------------------------------------------------##

# user interface for final project - this is what users interact with
print("Welcome to Newsmaster 3000!")
repeat = True
while repeat == True:
    list_of_similar_articles = []
    source = input("Input a search term for a news article: ").lower()
    if source in search_terms:
        url = site_nytimes(source)
        html_doc = html_file(url)
        article = get_article(url)
        get_info(article)
        status = what_next(url)
        if status == "quit":
            repeat = False
    elif source in sub_categories:
        url = site_nytimes_sub(source)
        article = get_article(url)
        get_info(article)
        status = what_next(url)
        if status == "quit":
            repeat = False
    elif source == "exit" or source == "exit()":
        repeat = False
    else:
        print("Invalid search term. Please try again.")
