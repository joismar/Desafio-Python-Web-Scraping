from bs4 import BeautifulSoup
from selenium import webdriver
import json

# -
# Observações:
# 
# As primeiras tentativas foram realizadas com o uso do Scrapy, porém 
# apresentada um erro de requests, informando que a resposta da
# requisição era inválida. 
# 
# Dessa forma recorri ao método mais fácil e rápido, Requests com BS,
# que é basicamente o Core do Scrapy. Tudo funcionou até a parte das
# imagens, que não são carregadas todas elas no primeiro GET.
# 
# Consegui resolver usando o selenium, pois com ele as requisições em 
# cascada são realizadas, me dando acesso ao ultimo carregamento da 
# página e enfim a todas as imagens.
#
# Nesse exemplo realizei programação estruturada pra ficar mais legível 
# e didático.
# -

# Instanciamento do chromedriver.exe
options = webdriver.ChromeOptions()
options.add_argument("--headless")

browser = webdriver.Chrome(options = options)

try:
    # Parte 1 e 2
    browser.get('https://lista.mercadolivre.com.br/gpon')

    soup = BeautifulSoup(browser.page_source, "html.parser")

    soup_items = soup.find_all('li', {"class": "ui-search-layout__item"})

    items = []

    # Parte 3, 4 e 5
    for item in soup_items:
        items.append({
            'titulo': item.find('h2', {'class': 'ui-search-item__title'}).text, 
            'link': item.find('a', href=True)['href'],
            'preco': item.find('span', {'class': 'price-tag-fraction'}).text,
            'frete_gratis': bool(item.findAll(text='Frete grátis')),
            'patrocinado': bool(item.findAll(text='Patrocinado')),
        })
        
        browser.get(items[-1]['link'])

        soup_item = BeautifulSoup(browser.page_source, "html.parser")

        item_images_links = [img['src'] for img in soup_item.findAll('img', {'class': 'ui-pdp-gallery__figure__image'})]

        items[-1]['imagens'] = item_images_links

        print('Captured: ' + str(items[-1]))

    with open(f'joismar_mercadolivre.json', 'w') as result_file:
        result_file.write(json.dumps(items, indent=4))

    browser.quit()

except Exception as e:
    browser.quit()
    raise(e)