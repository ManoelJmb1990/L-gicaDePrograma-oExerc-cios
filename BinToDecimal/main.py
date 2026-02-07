inp = "1011"
totalBin = 0

# O loop 'enumerate' percorre a string invertida para que o índice 'i'
# corresponda à potência de 2 correta (da direita para a esquerda).
# The 'enumerate' loop iterates through the reversed string so that
# index 'i' matches the correct power of 2 (from right to left).
for i, value in enumerate(reversed(inp)):
    # Cada dígito (0 ou 1) é multiplicado por 2 elevado à posição 'i'.
    # Each digit (0 or 1) is multiplied by 2 raised to the power of position 'i'.
    value = int(value) * (2 ** i)

    # Somamos o resultado ao total.
    # We add the result to the total.
    totalBin += value

print(totalBin)


# --- Solução Alternativa / Alternative Solution ---

def bin_to_decimal(inp):
    # O Python já possui uma função nativa 'int()' que aceita a base como segundo argumento.
    # Python already has a built-in 'int()' function that accepts the base as a second argument.
    return int(inp, 2)