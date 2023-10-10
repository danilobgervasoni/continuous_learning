import requests
from bs4 import BeautifulSoup
from datetime import date

# Define a URL da página
url = 'https://onefootball.com/pt-br/jogos'

# Faz a solicitação HTTP para a página
response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Cria um objeto BeautifulSoup para analisar o HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Obtém a data de hoje no formato "dd/mm/yyyy"
    today = date.today().strftime('%d/%m/%Y')

    # Encontra todos os elementos que contêm informações dos jogos
    matches = soup.find_all('div', class_='DatePicker_wrapper__XlgZR DatePickerWrapper_wrapper__picker__h__Le')

    # Itera pelos elementos dos jogos e extrai as informações
    for match in matches:
        date = match.find('div', class_='title-7-bold DatePicker_fakeButtonText__pxlj1').text.strip()
        if  today == date:
            time = match.find('span', class_='SimpleMatchCard_simpleMatchCard__infoMessage__secondary__hisY4').text.strip()
            teams = match.find('div', class_='SimpleMatchCard_simpleMatchCard__teamsContent__vSfWK').text.strip()
            
            print(f'Data: {date}')
            print(f'Hora: {time}')
            print(f'Times: {teams}')
            print('-' * 50)
else:
    print('Falha ao acessar a página de jogos.')
