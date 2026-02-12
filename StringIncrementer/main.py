import re

string = "foobar99"

if len(string) > 0 and re.search(r"\d+", string):

    string = string[::-1]  # Utilizei uma técnica chamada Slicing para inverter a string
    numeric_value = re.search(r'\d+', string).group()
    # Através da expressão regular
    # extraí o primeiro evento numérico

    stringSize = len(numeric_value)
    # peguei o tamanho da string numeric_value para usar como argumento no zfill

    string = string[len(numeric_value):]
    # Essa também é uma forma de Slicing.
    # This too is a form of slicing
    string = string[::-1]

    numeric_value = int(numeric_value[::-1]) + 1  # coloquei os números na ordem novamente
    numeric_value = str(numeric_value)
    numeric_value = numeric_value[::-1].zfill(stringSize) #conferir a necessidade de inverter aqui
    # Completei com zeros usando o argumento o tamanho original do int

    string = string + numeric_value
    print(string)
elif len(string) > 0:
    numeric_value = "1"
    string += numeric_value
    print(string)

else:
    numeric_value = 1
    print(numeric_value)




