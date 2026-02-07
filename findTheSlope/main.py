def find_slope(points):
    deltaX = points[2] - points[0]
    deltaY = points[3] - points[1]
    if deltaX == 0:
        return "undefined"
    else:
        pointGraphic = deltaY // deltaX
        return str(pointGraphic)

