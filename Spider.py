from lxml import html
import requests

#Link do Site que quer pegar o dado
page = requests.get('https://www.icarros.com.br/ranking-de-satisfacao/seda/1.html')
tree = html.fromstring(page.content)

#Colocar o primeiro elemento aonde se encontra o dado que quer pegar no meu caso estava dentro de uma div - e dentro da class="textopqn"
buyers = tree.xpath('//div[@class="textopqn"]/text()') 
buyers1 = tree.xpath('//a[@class="linkcatalogo"]/text()') 
buyers2 = tree.xpath('//h4[@itemprop="average"]/text()') 

#Imprimir na tela o dado capturado !!
print ('Posição\n\n', buyers,'\n')
print ('Modelo\n\n', buyers1,'\n')
print ('Notas\n\n', buyers2)




