import constante as c
import TkinterCode.tkinterObject as tkO


def check() -> bool:
    """
    S'assure de l'existence du nombre de point demandé et/ou de l'existence des coordonnées de la fenêtre
    """

    nbPointStr = tkO.Entry_NbPoint.get()
    try:
        nbPoint = int(nbPointStr) 
        getCheck = c.window[0] == (c.DEFAULT_LEFT_SPACE,c.DEFAULT_TOP_SPACE) and c.window[1] == (-c.DEFAULT_RIGHT_SPACE,-c.DEFAULT_BOTTOM_SPACE)
        return (nbPoint > 0) and (c.window != []) and (tkO.value.get() != "") and not(getCheck)
    except ValueError:
        return False



def checkAff() -> None:
    """
    Si il y a une erreur de check, affiche un message d'erreur
    """

    if not(check()):
        tkO.tkM.messagebox.showwarning("Error","Vous n'avez pas ouvert GraphWar\n OU \n Votre nombre de points est invalide !")




