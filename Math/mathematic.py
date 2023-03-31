
import constante as c

def fitPoint(window, point):
    """
    Ramène un point présent dans la fenêtre dans l'ensemble [X_MIN,X_MAX]x[Y_MIN,Y_MAX]
    """
    ptHautGauche = window[0]
    ptBasDroite = window[1]

    xHG = ptHautGauche[0]
    yHG = ptHautGauche[1]
    xBD = ptBasDroite[0]
    yBD = ptBasDroite[1]

    x = point[0] - xHG
    y = point[1] - yBD

    xBD -= xHG
    yHG -= yBD
    x = (x * (c.X_MAX- c.X_MIN))/xBD - c.X_MAX
    y = (y * (c.Y_MAX - c.Y_MIN))/yHG - c.Y_MAX

    x = round(x,c.PRECISION)
    y = round(y,c.PRECISION)

    return (x,y)

def fitPointList(window, listPoint) -> list:
    """
    Ramène une liste de point dans l'ensemble [X_MIN,X_MAX]x[Y_MIN,Y_MAX]
    """
    treatedPointList = []
    for point in listPoint :
        treatedPointList.append(fitPoint(window,point))
    return treatedPointList
