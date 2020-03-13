from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

url ='https://www.aluraose.com.br'
headers ={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}


try:
    req = Request(url, headers = headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.find('title').get_text())

# na aula o prof orientou a manter nessa ordem os erros pois cai no segundo e não exibe o 403
except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)

