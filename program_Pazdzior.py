import re

def Add(numbers : str):
    numbers = numbers.replace(' ', '')
    tab = re.split(r',|\n', numbers)
    tab = [i for i in tab if i != '']
    if (len(tab) == 0):
        return 0
    tab_int = [int(n) for n in tab]
    return sum(tab_int)
