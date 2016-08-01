def convert_text(html_code):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(html_code)
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    print(soup.get_text())

def site_nytimes(section):
    print("http://www.nytimes.com/pages/" + section + "/index.html")
    
webbrowser.open("http://www.nytimes.com/pages/world/index.html")