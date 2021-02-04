#vai baixar o html
import requests
#Vai permitir alterar o html
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'

response = requests.get(url=url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    voto = pergunta.select_one('.vote-count-post strong')
    print(titulo.text, data.text, voto.text,sep='\t')
