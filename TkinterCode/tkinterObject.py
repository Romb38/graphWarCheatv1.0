import TkinterCode.tkinterMain as tkM
import traitementPolynome as tP

root = tkM.root
value = tkM.value
entry = tkM.entry
tk = tkM.tk
c = tkM.c

def clearEntryZone() -> None:
    """
    Efface toute entrée présente dans le champs de saisie
    """
    saisie = Entry_NbPoint.get()
    len_saisie = len(saisie)
    Entry_NbPoint.delete(0,len_saisie)


#Création et placement des widget
Label_NbPoint = tk.Label(tkM.root,text = "Nombre de points désirés")
Label_NbPoint.grid(column=0,row=1)

Entry_NbPoint = tk.Entry(root,textvariable=entry)
Entry_NbPoint.grid(column=1,row=1)  

Label_AlgoList = tk.Label(root, text = "Choisisez votre algorithme :")
Label_AlgoList.grid(column=0, row = 3)

BoutonRadio_AlgoList = tk.Radiobutton(root, text="Polynome",variable = value, value = 1)
BoutonRadio_AlgoList.grid(column=1,row = 3)

BoutonRadio_AlgoList2 = tk.Radiobutton(root, text ="Chute",variable = value,value = 2)
BoutonRadio_AlgoList2.grid(column=1,row=5)

BoutonRadio_AlgoList2 = tk.Radiobutton(root, text ="Pic",variable = value,value = 3)
BoutonRadio_AlgoList2.grid(column=1,row=6)

Bouton_CreerPoly = tk.Button(root,text="Créer Polynôme", command=tP.createPolynome, borderwidth = 5)
Bouton_CreerPoly.grid(column=0,row=c.NB_ALGO_INTERPOL+3)

Label_Polynome = tk.Label(root,text= "Polynôme :")
Label_Polynome.grid(column=0,row=c.NB_ALGO_INTERPOL+4)

LabelPolynome = tk.Label(root, textvariable=tkM.Polynome)
LabelPolynome.grid(column=1,row = c.NB_ALGO_INTERPOL+4)

LabelNom = tk.Label(root, text = "Made by Romb38 - r.barbier38@gmail.com", font = ('Courrier',7))
LabelNom.grid(column=0,row = c.NB_ALGO_INTERPOL+5, sticky= "W")


