import requests
from bs4 import BeautifulSoup

# URL do site de notícias que você deseja acessar
url = 'https://doentesporfutebol.com.br/guiadejogos/'

# Enviar uma solicitação GET para a URL
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parse o conteúdo da página com Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontre os elementos que contêm os títulos e links das notícias
    games = soup.find_all('a', class_='elementor-widget-container')  

    # Loop pelas notícias e imprima os títulos e links
    for game in games:
        titulo = game.text
        link = game['href']
        print(f'Título: {titulo}')
        print(f'Link: {link}')
else:
    print('Falha ao acessar a página de notícias.')
