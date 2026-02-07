def reverse_seq(n):
    nList = []
    # range(início, fim, passo)
    # Começamos em 'n', paramos antes de '0' (ou seja, no 1) 
    # e subtraímos 1 a cada iteração (passo -1).

    # range(start, stop, step)
    # We start at 'n', stop before '0' (which means at 1),
    # and subtract 1 at each iteration (step -1).
    for index in range(n, 0, -1):
        nList.append(index)

    return nList