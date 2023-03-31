import ctypes
import constante as c


def GetWindowRectFromName(name:str)-> tuple:
    """
    Récupère la taille de la fenêtre de jeu 
    """

    hwnd = ctypes.windll.user32.FindWindowW(0, name)
    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.pointer(rect))

    clearWindow()
    c.window.append((rect.left+c.DEFAULT_LEFT_SPACE,rect.top+c.DEFAULT_TOP_SPACE))
    c.window.append((rect.right-c.DEFAULT_RIGHT_SPACE,rect.bottom-c.DEFAULT_BOTTOM_SPACE))

def clearWindow():
    """
    Rend la variable window vide
    """
    while c.window != []:
        c.window.pop()

def resetCoordList():
    """
    Rends vide la liste globale coordList
    """
    while len(c.coordList) != 0:
        c.coordList.pop()


def splitXY(listPoint : list):
    """
    Sépare une liste de points donné en deux liste de coordoonée X et Y
    """
    X = []
    Y = []
    for i in listPoint :
        X.append(i[0])
        Y.append(i[1])
    
    return (X,Y)
