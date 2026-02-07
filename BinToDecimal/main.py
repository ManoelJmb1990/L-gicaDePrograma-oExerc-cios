inp = "1011"
totalBin = 0
for i, value in enumerate(reversed(inp)):
    value = int(value) * (2 ** i)
    totalBin += value

print(totalBin)


# Other Solution

def bin_to_decimal(inp):
    return int(inp, 2)