'''
Scraping com Python: Coleta de dados na web
Curso Alura
https://cursos.alura.com.br/course/web-scraping-data-science-python/

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

url ='https://alura-site-scraping.herokuapp.com/hello-world.php'

response = urlopen(url)

html = response.read()

soup = BeautifulSoup(html, 'html.parser')

print(soup.find('h1', {'class': 'sub-header'}).get_text())