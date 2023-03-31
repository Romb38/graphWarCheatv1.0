Bonjour,

Voici un petit logiciel permettant de tracer des courbes facilment sur GraphWar


Il fonctionne très simplement :
    - Vous indiquez le nombre de points par lequel vous voulez que votre courbe passe
    - Vous lancer la création du polynôme
    - Vous retournez sur la fenêtre de GraphWar
    - Vous faites des clics droits aux différents points ou la fonction devra passer (autant que de point désiré)

    /!\ Le premier point doit impérativement être votre personnage /!\

Le polynôme apparaitra directement dans votre presse-papier, alors vous n'aurez qu'a appuyer sur ctrl + V dans la barre de création et c'est fini !

(Pour l'instant cela ne fonctionne que sur le mode simple, nous ajouteront ceux avec les équations différentielles plus tard)

--------------------------------------------------------------------
Les différents algorythmes :

 - Interpolation Polynomiale -> Crée un polynome à partir de l'algorythme de Lagrange
 - Chute -> Ne demande que 2 points et créer une fonction qui va horizontalement avant de chuter proche du point désigné
 - Pic -> Ne demande que 2 points et fait une ligne droite avec un pic sur le deuxième point selectionné

---------------------------------------------------------------------
Quelques conseils :
 - Lorsque vous utilisez l'interpolation de Lagrange, ne placez pas plus de 3 points sinon votre courbe risque de s'échapper du cadre

 - Ne placez pas vos points trop proches (sur la même colone/ligne) sinon des erreurs peuvent se créer

 - Si votre courbe fait n'importe quoi, se réferer aux conseils
-----------------------------------------------------------------------

-- Romb38 --
(r.barbier38@gmail.com)