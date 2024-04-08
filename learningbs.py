from bs4 import BeautifulSoup as bs
import requests

NUM_PAGES = 114
sublinks = []

for page in range(NUM_PAGES):
    link = f"http://airfoiltools.com/search/index?m%5BtextSearch%5D=&m%5BmaxCamber%5D=&m%5BminCamber%5D=&m%5BmaxThickness%5D=18&m%5BminThickness%5D=8.5&m%5Bgrp%5D=&m%5Bsort%5D=11&m%5Bpage%5D={page}&m%5Bcount%5D=1132"

    response = requests.get(link)

    site = bs(response.content, "html.parser")

    #print(site.prettify())

    #print(site.find_all("a"))

    for a_tag in site.find_all("a"):
        text = a_tag.get_text()
        if "Airfoil details" in text:
            #print(a_tag["href"])
            sublinks.append("http://airfoiltools.com" + a_tag["href"])

with open('sublinks','w') as file:
    for sublink in sublinks:
        file.write('%s\n' % sublink)

