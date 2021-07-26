from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.scientificamerican.com/physics/').text

soup = BeautifulSoup(html_text, 'lxml')

articles = soup.find_all('h2', class_ = "t_listing-title")

for article in articles:
    print(article.text)
