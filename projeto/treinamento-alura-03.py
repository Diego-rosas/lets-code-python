from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

'''

Nessa aula o foco foi sobre o tratamento de strings e demonstrar que o urllib e open trazem um binário,
é necessário cuidar da codificação e da limpeza de caracteres desnecessários.

'''

url ='https://alura-site-scraping.herokuapp.com/'


def trata_html(pagina):
    return " ".join(pagina.split()).replace('> <', '><')


try:
    response = urlopen(url)
    html = response.read()
    # print(type(html)) # demonstra que é tipo bytes
    html = html.decode('utf-8')
    # print(type(html))
    html = trata_html(html)
    
    print(html)

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)
