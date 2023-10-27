import requests
from bs4 import BeautifulSoup

#парсит сайт с достопримечательностями и достаёт названия + картинки
def get_attraction(city):
    wiki = requests.get(f"https://posmotrim.by/section/{city}.html")
    soup = BeautifulSoup(wiki.text, 'html.parser')
    answer_text = soup.find_all('div', class_="post-title")
    answer_img = soup.find_all('div', class_ = "post-img")
    imageSources = []
    for ans1 in answer_img:
            a = ans1.find_all('a')
            for x in a:
                    img = x.find_all('img')
                    for y in img:
                            imageSources.append(y.get('src'))
    textSources = []
    for ans1 in answer_text:
            h3 = ans1.find_all('h3')
            for ans2 in h3:
                    a = ans2.find_all('a')
                    for ans3 in a:
                            textSources.append(ans3.get_text())
    return (textSources, imageSources)


