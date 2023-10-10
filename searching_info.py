import requests
from bs4 import BeautifulSoup
from datetime import date

# URL do site de notícias que você deseja acessar
url = 'https://doentesporfutebol.com.br/guiadejogos/'

# Enviar uma solicitação GET para a URL
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parse o conteúdo da página com Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Obtém a data atual
    today = date.today().strftime('%d/%m/%Y')

    # Encontra os elementos que contêm as informações dos jogos de hoje
    matches = soup.find_all('div', class_='elementor-widget-container')

    # Itera pelos elementos dos jogos
    for match in matches:
        date = match.find('span', class_='match__date').text
        if today in date:
            time = match.find('span', class_='match__time').text
            teams = match.find_all('span', class_='match__team')
            team1 = teams[0].text
            team2 = teams[1].text
            broadcast = match.find('div', class_='match__broadcast').text.strip()

            # Imprime as informações do jogo
            print(f'Match date: {date}')
            print(f'Match time: {time}')
            print(f'{team1} x {team2}')
            print(f'Broadcast channel: {broadcast}')
            print('-' * 50)
else:
    print('Failed to access the matches page.')