dice = [5, 1, 3, 4, 1]
sum = 0
counter = [0, 0, 0, 0, 0, 0]
points = [1000, 200, 300, 400, 500, 600]
extra = [100, 0, 0, 0, 50, 0]

for die in dice:
    counter[die-1] += 1 # eu uso die - 1 para que eu posso contar dentro da
                        # lista as incidencias dentro dos locais certos.
                        # Ex: se eu só usava o 6 para alimentar o índice, daria o erro
                        # IndexError: list index out of range, pq ele iria para a 7ª
                        # posição da lista. 0, 1, 2, 3, 4, 5, '6' -> 7ª posição...

for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)
print (sum)

# foi criado a lista counter de eventos de repetição/aparição dos números
# é percorrido dentro dela com o for (i, count) e verificando quem ja apareceu ou
# se repetiu 3x ou mais e se repetiu 3x ou mais, sum recebe o valor de points[i] se não
# recebe 0, e soma tudo com extra[i] e o que restou das repetições caso seja maior que 3
# count % 3 == ?.
# se repetiu 4x, count % 3 == 1, ai é 1 * extra[i], supondo que seja na posição 4, daria 50.