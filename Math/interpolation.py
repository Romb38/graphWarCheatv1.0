from this import s
from pkg_resources import declare_namespace
import Math.polynome as poly
from methods.methode_list_constante import splitXY

"""
A faire : Comprendre puis implementer l'interpolation trigonometrique
Trouver comment faire une fonction en L
"""
RESSEREMENT = 50
PRECISION = 5

def Lagrange(listPoint : list):
    """
    Créer un polynôme à partir de l'interpolation de Lagrange
    """
    deg = len(listPoint)

    polyFinal = poly.Polynome([0])

    for i in range(0,deg):
        l_i = poly.Polynome([1])
        for j in range(0,deg):
            if i != j:
                x_i = listPoint[i][0]
                x_j = listPoint[j][0]
                try :
                    a = 1/(x_i-x_j)
                except ZeroDivisionError :
                    return ""
                b = -x_j*a
                P = poly.Polynome([b,a])
                l_i.multiplicationPolynome(P)
        y_i = listPoint[i][1]
        l_i.scalMultiplication(y_i)
        polyFinal.addPolynome(l_i)

    polyFinal.round()
    return polyFinal

#Ajout de l'interpolation trigonometrique (voir avec thomas)

def pic(listPoint : list):
    pic = listPoint[1]
    decalage = -1*pic[0]

    hauteurPerso = listPoint[0][1]
    hauteur = abs(pic[1] - hauteurPerso)
    hauteur = round(hauteur,PRECISION)

    if pic[1]<hauteurPerso:
        hauteur *= -1

    if decalage>0 :
        decalage = f'+{decalage}'
    
    res = f'{hauteur}*sin({RESSEREMENT}*(x{decalage}))/({RESSEREMENT}*(x{decalage}))'
    return res

def chute(listePoint : list):
    """
    Crée une fonction du type 1/(x-10)
    """
    placePerso = listePoint[0]
    chute = listePoint[1]
    sens = 1

    if placePerso[1] < chute[1]:
        sens = -1

    foncFin = f'{sens}/(x{-1*(chute[0]+0.1)})'

    return foncFin

"""
WOK :
- Ajout de l'interpolation trigonometrique

X - Methode des moindres carrés

"""
