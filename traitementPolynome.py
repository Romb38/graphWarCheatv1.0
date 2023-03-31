import clipboard as cb

import Math.mathematic as math
import TkinterCode.tkinterObject as tkO
import methods.verification as v
import constante as c
import methods.methode_list_constante as m
import clickGestion as cg

def traitementPoints(listPoint, window) -> str:
    """
    Transforme une liste de point en une chaine de caractère contenant un polynôme passant par les points
    """

    listPoint = math.fitPointList(window, listPoint)

    nbAlgo = int(tkO.value.get())-1

    polyFinal = str(c.ALGO_INTERPOL[nbAlgo](listPoint))

    return polyFinal

def roundList(listPoint):
    listArrondie = []
    for i in listPoint:
        x = round(i[0],c.PRECISION)
        y = round(i[1],c.PRECISION)
        listArrondie.append((x,y))
    
    return listArrondie

def createPolynome() -> None:
    """
    Crée un polynome à partir de nbPoints donnés par l'utilisateur (ne fait rien si check n'est pas vérifié)
    """
    m.GetWindowRectFromName(c.FENETRE_NAME)

    nbAlgo = int(tkO.value.get())-1
    
    if nbAlgo == 1 :
        tkO.clearEntryZone()
        tkO.entry.set("2")
    
    if nbAlgo == 2 :
        tkO.clearEntryZone()
        tkO.entry.set("2")

    if not(v.check()):
        v.checkAff()
        return ""
    else:
        nbPoint = int(tkO.Entry_NbPoint.get())
        listPoint = cg.getListPoint(nbPoint)
        listPoint = roundList(listPoint)
        polynomeStr = traitementPoints(listPoint,c.window)
        if polynomeStr == "":
            tkO.tkM.messagebox.showwarning("Error","Une erreur s'est produite lors de la création dudit polynome !")
        else :
            tkO.tkM.Polynome.set(polynomeStr + "   ")
            cb.copy(polynomeStr)