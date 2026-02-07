def find_slope(points):
    # A lista 'points' contém [x1, y1, x2, y2]
    # Calculamos a variação de X (deltaX = x2 - x1) e Y (deltaY = y2 - y1)
    # The 'points' list contains [x1, y1, x2, y2]
    # We calculate the change in X (deltaX = x2 - x1) and Y (deltaY = y2 - y1)
    deltaX = points[2] - points[0]
    deltaY = points[3] - points[1]

    # Se a variação de X for zero, a reta é vertical e a inclinação é indefinida (divisão por zero)
    # If the change in X is zero, the line is vertical and the slope is undefined (division by zero)
    if deltaX == 0:
        return "undefined"
    else:
        # O coeficiente angular é a razão entre a variação de Y e a variação de X
        # Nota: // realiza uma divisão inteira em Python
        # The slope is the ratio of the change in Y to the change in X
        # Note: // performs integer division in Python
        pointGraphic = deltaY // deltaX
        return str(pointGraphic)