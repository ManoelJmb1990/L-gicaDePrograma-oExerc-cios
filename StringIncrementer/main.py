"""A sua função é criar um programa que leia string e incremente para
criar novas strings.

number = 0
se string[-1] == int:
    number += string[-1]
    insert(-1, number)


    vamos tentar resolver com re (Expressões Regulares)"""

import re

entrada = "foobar23bla50"

valor_numerico = re.search(r'\d+$', entrada).group()
valor_numerico = int(valor_numerico) + 1

entrada = re.search(r'[a-zA-Z]+', entrada).group()

wordCombination = entrada + str(valor_numerico)
print(wordCombination)
