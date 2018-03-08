import re


def check_for_correct(text):
    data = text.split('_')
    flag = False
    if data[0].isalpha() and re.match(r'^[А-Я]', data[0]):
        if re.match(r'^[А-Я].[А-Я].', data[1]):
            if data[2].isdigit():
                flag = True
    return flag



print(check_for_correct(""))
