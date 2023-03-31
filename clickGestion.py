from pynput.mouse import Listener, Button

import constante as c
import methods.methode_list_constante as m



def on_click(x, y, button, pressed):
    """
    Fonction lancée lors de l'évenement mouse click
    """
    c.coordList.append((x,y,button,pressed))
  

def getListPoint( nbPoint) -> list:
    """
    Récupère nbPoint points sur l'écran quand l'utilisateur utilise le clique droit
    """
    listener = Listener(on_click=on_click)
    coordPoint = []
    listener.start()
    
    while len(coordPoint) != nbPoint:
        if len(c.coordList) != 0:
            click = c.coordList[0]
            if (click[2] == Button.right) and click[3] :
                coordPoint.append((click[0],click[1]))
            m.resetCoordList()
    listener.stop()
    
    return coordPoint


