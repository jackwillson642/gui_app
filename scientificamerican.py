from bs4 import BeautifulSoup
import requests

# pages_soup is the list that contains the soup of html for all the pages
pages_soup = []
category = 'physics'
# category = 'math'
# category = 'space'
html_text = requests.get('https://www.scientificamerican.com/%s/' % category).text
pages_soup.append(BeautifulSoup(html_text, 'lxml'))

# headings, dates and summaries are in the following lists 
headings = []
dates = []
summaries = []
for soup in pages_soup:
    articles = soup.find_all('article', class_ = "listing-wide")
    for article in articles:
        headings.append(article.a.h2.text)
        dates.append(article.find('div', class_ = 't_meta').text)
        summaries.append(article.p.text)


def get_headings():
    return headings

def get_dates():
    return dates

def get_summaries():
    return summaries
