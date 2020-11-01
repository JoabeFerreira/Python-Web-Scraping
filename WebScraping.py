from bs4 import BeautifulSoup as soup #BIBLIOTECA PARA WEBSCRAPING
from urllib.request import urlopen

myUrl='https://www.newegg.com/global/br-en/Video-Cards-Video-Devices/Category/ID-38'

#Abrindo a conexão e pegando Página
cliente=urlopen(myUrl)
pageHtml=cliente.read()
cliente.close()

#Quebrando a Página
pageSoup=soup(pageHtml, 'html.parser')

# Retorna cada produto
containers = pageSoup.findAll('div', {'class':'item-container'})

# Criando o arquivo CSV
arq=open('Products.csv', 'w')
colunas='Nome_Produto, Marca, Preço, Entrega\n'
arq.write(colunas)

# Buscando todas informação de cada produto
for container in containers:
    brand = container.div.a.img['title']

    titleContain = container.findAll('a', {'class':'item-title'}) #retorna uma lista com todos que correspondem
    ProductName=titleContain[0].text

    shippingContain=container.findAll('li', {'class':'price-ship'})
    shipping=shippingContain[0].text

    priceContain=container.findAll('li', {'class':'price-current'})
    price=float(priceContain[0].text[:8].strip('$')) # To dividindo pq saiu a quantidade de ofertas tbm
    print(price)

    arq.write(f'{ProductName.replace(",", "|")}, {brand}, {price}, {shipping}\n')
arq.close()    
