import requests
from bs4 import BeautifulSoup

# Получение HTML страницы
url = 'https://wttr.in/'
response = requests.get(url)

if response.status_code == 200:
    print("Страница загружена")
    # Парсинг HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    weather_info = soup.text
    print("Информация о погоде:", weather_info)
else:
    print(f'Ошибка при загрузке страницы: {response.status_code}')
