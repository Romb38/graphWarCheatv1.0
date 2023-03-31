import tkinter as tk
import constante as c
from tkinter import StringVar, messagebox

root  = tk.Tk()
root.title("GraphWar Help")
root.resizable(False,False)
root.iconbitmap('./icon.ico')

#Variable contenu des Label
windowCheck = StringVar()
windowCheck.set("Selectionnez le coin Haut-Gauche et Bas-Droite de la fenêtre")
Polynome = StringVar()
value = StringVar()
value.set("1")
entry = StringVar()