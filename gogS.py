import requests
from bs4 import BeautifulSoup

def get_gog_source(source : str):
    result = requests.get(source)
    src = result.content
    return BeautifulSoup(src, 'lxml')

def get_gog(source : str):
    all_links = get_gog_source(source).find_all('a')
    gogs = []
    for link_string in all_links:
        link = link_string['href']
        if link.startswith('/view/gog'):
            gog_link = 'https://tenor.com' + link
            gogs.append(gog_link)
    return gogs
