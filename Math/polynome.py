from os import stat
import constante as c


class Polynome():
    __coef = []
    __deg = 0

    #Constructeur
    def __init__(self,coef) -> None:
        self.__coef = coef
        self.__deg = len(coef)

    #Getter/Setter
    @property
    def getCoef(self):
        return self.__coef
    
    @property
    def getDegree(self):
        return self.__deg


    def setCoef(self,coef):
        self.__coef = coef
    
    def setDeg(self):
        self.__deg = len(self.getCoef)

    #Methodes
    def __PolyEqualiser(self,maxdeg):
        """
        Rajoute des 0 au polynome pour que son degré soit égale a maxdeg
        """
        coef = self.getCoef
        coef += [0 for i in range(0,maxdeg - self.getDegree)]
        self.setCoef(coef)

    def __removeZero(self):
        """
        Enlève les zéros superflus
        """
        coef = self.__coef[::-1]

        while coef !=[] and coef[0]==0:
            coef.pop(0)
        
        self.__coef = coef[::-1]

    @staticmethod
    def __max(a :int, b:int) -> int:
        """
        Trouve le max entre deux entier
        """
        max = a
        if a<b:
            max = b
        return max

    @staticmethod
    def __aff(coef,i):
        res = f'{coef}x'
        if i != 1:
            res +="^"
            res += str(i)
        res += " + "
        return res

    def round(self):
        """
        Arrondi les coefficients des polynômes a PRECISION décimales
        """
        coef = self.getCoef
        deg = self.getDegree

        for i in range(0,deg):
            coef[i] = round(coef[i],c.PRECISION)
        
        self.setCoef(coef)

    #Opération disponible pour les polynomes

    def addPolynome(self , poly2):
        """
        Additionne deux polynôme
        """

        degPoly = Polynome.__max(self.getDegree,poly2.getDegree)
        self.__PolyEqualiser(degPoly)
        poly2.__PolyEqualiser(degPoly)

        coef = self.getCoef
        coef2 = poly2.getCoef

        for i,val in enumerate(coef):
            coef[i] = val + coef2[i]
            
        self.setCoef(coef)
        self.__removeZero
        self.setDeg()
        poly2.__removeZero
        self.round
        poly2.round


    def scalMultiplication(self,scal) :
        """
        Multiplie le polynome par scal
        """

        coef = self.getCoef
        for i,val in enumerate(coef):
            coef[i] = val*scal
        self.setCoef(coef)
        self.__removeZero
        self.setDeg()
        self.round()

    def multiplicationPolynome(self,Q):
        """
        Multiplie deux polynome ensemble
        """
        degP = self.getDegree
        degQ = Q.getDegree
        degFinal = max(degQ,degP)

        self.__PolyEqualiser(2*degFinal)
        Q.__PolyEqualiser(2*degFinal)

        coefP = self.getCoef
        coefQ = Q.getCoef
        coefFinal = []

        for k in range(0,2*degFinal):
            somme = 0
            for i in range(0,k+1):
                somme += coefP[i]*coefQ[k-i]
            coefFinal.append(somme)

        self.setCoef(coefFinal)
        self.__removeZero()
        Q.__removeZero()
        self.round
        Q.round
        self.setDeg()


    #Égalité
    def __eq__(self, other):
        if isinstance(other,Polynome):
            if self.getDegree == other.getDegree:
                for i in range(0,self.getDegree):
                    if self.getCoef[i] != other.getCoef[i]:
                        return False
                return True
        return False


    #toString
    def __str__(self) -> str:
        """
        Permet l'affichage d'un polynome format correct
        """
        coef = self.getCoef
        deg =  self.getDegree
        res = ""

        if coef == []:
            return "0"
        else:
            if coef[0] != 0 or len(coef) == 1 :
                res += str(coef[0])
                res += " + "

            for i in range(1,deg):
                if coef[i] != 1 and coef[i] != 0:
                    res += Polynome.__aff(str(coef[i])+"*",i)
                elif coef[i] == 1:
                    res += Polynome.__aff("",i)
        
        return res[:-3]




        

