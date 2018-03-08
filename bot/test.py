import re


def check_for_correct(text):
    data = text.split('_')
    flag = False
    if data[0].isalpha() and re.match(r'^[А-Я]', data[0]):
        if data[1].count('.') == 2 and data[1].__len__() == 4 and data[1].endswith('.'):
            if data[2].isdigit():
                flag = True
    return flag



print(check_for_correct("Горбенко_С.І._261"))
