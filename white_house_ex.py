# APPLY to briefings and statements from the Whitehouse web site
# https://www.whitehouse.gov/briefings-statements/

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

# by inspecting the web page, we can see that all links are between <h2></h2> tags, then <a></a>.
urls = []
# find_all will return a list. find will return the first element
for h2_tag in soup.find_all('h2'):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

print(urls)
