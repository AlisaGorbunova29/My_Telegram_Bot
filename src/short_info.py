from wikipedia import*

wikipedia.set_lang("ru")

#достаёт краткую информацию о городе с википедии
def summary(city):
    answer = wikipedia.summary(city)
    if (answer.find("город") != -1):
        return answer
    else:
        raise Exception('Некорректный ввод')