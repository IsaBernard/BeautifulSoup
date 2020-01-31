"""
BeautifulSoup Tutorial - Web Scraping in Python.
YouTube: https://www.youtube.com/watch?v=87Gx3U0BDlo
GitHub: web_scraping_and_automation/beautiful_soup/beautiful_soup_and_requests.py

"""

import requests
from bs4 import BeautifulSoup


result = requests.get("https://www.google.com/")

# status_code just let's us know if the page was accessible or not: 200 response is present (OK).
print(result.status_code)

# check the HTTP header.
# print(result.headers)

# store the page content of the website accessed from requests to a variable:
src = result.content
# print(src)

# We create a BeautifulSoup object based on the source variable we created above:
soup = BeautifulSoup(src, 'lxml')

# We can now access specific info directly from the page source.
# Here we ask for the list of all the links on the page (all of the <a></a> tags):
links = soup.find_all("a")
# print(links)
# print("\n")

# Perhaps we just want to extract the link that contains the test 'About' on the page.
# We can use the built-in "text" function to access the text content between the <a></a> tags.
# for link in links:
#     if "About" in link.text:
#         print(link)
#         print(link.attrs['href'])

