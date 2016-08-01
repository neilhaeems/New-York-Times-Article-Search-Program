def convert_text(html_code):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(html_code)
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    print(soup.get_text())

def site_nytimes(section):
    print("http://www.nytimes.com/pages/" + section + "/index.html")

def site_twitter(section):
    print("https://twitter.com/search?q=" + section + "&src=typd&lang=en")

def open_link(section):
    import webbrowser
    webbrowser.open("http://www." + section + ".com/")
    