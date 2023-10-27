import requests
import re

#парсит википедию и достаёт картинку города
def get_picture(city):
    wiki = requests.get(f"https://ru.wikipedia.org/wiki/{city}")
    if (wiki.text.find("город") == -1):
        raise Exception
    find_picture = re.findall(r'property="og:image" content="(.*?)"', wiki.text)
    answer = []
    for i in find_picture:
        if (i.find("jpg")):
            answer.append(i)
            break
    return answer
