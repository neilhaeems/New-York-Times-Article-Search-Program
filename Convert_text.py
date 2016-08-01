def convert_text(html_code):
    x = []
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(html_code)
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
x = input('Type a website here: ')
convert_text(x)


#below - I'm going to try and break up the code

def site_twitter(section):
    print("https://twitter.com/search?q=" + section + "&src=typd&lang=en")  

#use "https://twitter.com/ " to see # get printed instead of links