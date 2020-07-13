lAlan = ['Alan','A','D','Z','C','C','B','Z','D']
lsolution = ['solution','A','A','C','C','C','B','C','D']
def points(reponse,solution):
        """ Cette fonction permet d'atribuer les points aux élèves en fonction de leurs réponses """
        if reponse==solution:#Je regarde si la solution est égale à la réponse de l'élève(réponse exacte), si oui je retourne 3
            return 3
        elif reponse!=solution:
            if reponse=='Z':#sinon je demande si la reponse est égale à Z(absence de réponse), si oui je retourne 0
                return 0
            else:# sinon, si la réponse est fausse, je retourne -1
                return -1
        

def corrige (lrep,lsol):
    """ Cette fonction retourne une liste avec les points des élèves et leurs prénoms """
    # en tout premier je crée une liste vide dans laquelle je vais mettre mon résultat
    resultat = []
    # ensuite j'y ajoute le prénom de l'élève
    resultat.append(lrep[0])
    for i in range(1,len(lrep)): # je parcours le reste de ma liste
        reponse = lrep[i]#J'attribue l'élément à la position i à l'intérieur de ma liste de reponses de l'élève à une variable reponse
        solution = lsol[i]#J'attribue l'élément à la position i à l'intérieur de ma liste de solution à une variable solution
        score = points(reponse,solution)#J'attribue ce que retourne la fonction points à une variable score que j'insers ensuite à résultat
        resultat.append(score)
    return resultat# Je retourne résultat

l=['Alan',3,-1,0,3,3,3,0,3]
def note (lpoints):
    """ Cette fonction renvoie la note totale à l'aide des points """
    somme=0#J'initialise une variable somme à zéro qui sera ma note
    for i in range(1,len(lpoints)):# Je parcours ma liste en excluant le prénom
        somme+=lpoints[i]#J'additionne à somme les points à l'index i de ma liste de points
    return somme#Je retourne somme soit la note

def reponseFausse(lpoints):
    """ Cette fonction retourne la liste des index des réponses fausses """
    rf=[]#J'initialise une liste vide nommée rf pour Réponses Fausses
    rf.append(lpoints[0])#J'y ajoute le prénom de l'élève
    for i in range(1,len(lpoints)):#Je parcours le reste de la liste de points
        if lpoints[i]!=3:#Si le point à l'index i n'est pas égale à 3, une bonne réponse, alors on ajoute l'index i à la liste rf
            rf.append(i)
    return rf # Je retourne la liste des réponses fausses


# partie 2

grille =    [ ['Alan','A','D','Z','C','C','B','Z','D'] ,
              ['Ada','B','D','B','C','Z','B','Z','A'] ,
              ['Hedy','B','D','B','C','Z','B','Z','Z']  ]
lsolution = ['solution','A','A','C','C','C','B','C','D']

def corrigeGrille(grillerep,lsol):
    """ Cette fonction corrige une grille(au lieu d'une liste seule)et retourne une grille corrigée avec les points attribués pour chaque élève """
    grille2=[0]*len(grillerep)#J'initialise une liste de la longueur de la grille de réponses
    for i in range(len(grillerep)):#Je parcours ma liste
        grille2[i]=corrige(grillerep[i],lsol)#J'assigne à l'index de la liste une nouvelle liste pour en faire une grille
                                             #faite à partir de la fonction corrige(à partir de l'index de la grille de réponses, soit la liste de réponse de l'élève,
                                             #et de la liste de solutions) qui retourne la liste des points marqués par question
    return grille2# Je retourne la deuxième grille

g=  [ ['Alan', 3,-1,0,3,3,3,0,3] ,
      ['Ada', -1,-1,-1,3,0,3,0,-1] ,
      ['Hedy', -1,-1,-1,3,0,3,0,0] ]

def noteGrille(grillepoints):
    """ Cette fonction additionne une liste à l'intérieur d'une grille de points pour retourner une grille avec la note par élève """
    grille3=[0]*len(grillepoints)#Je crée une liste de la taille de la grille de points
    for x in range(len(grillepoints)):#Je parcours ma liste
        grille3[x]=[0]*2#J'insère une liste de deux occurences pour créer une grille
    for i in range(len(grillepoints)):#Je parcours ma grille
        for j in range(len(grillepoints[i])):
            if j==0:#Je mets le prénom en début de grille3[i] car grillepoints[i][0], grillepoints[i][j] dans cette situation, est l'emplacement du prénom de l'élève 
                grille3[i][0]=grillepoints[i][j]
            else:#Je mets la note en deuxième position, note que je calcule avec la fonction note appliquée à la liste grillepoints[i]
                grille3[i][1]=note(grillepoints[i])
    return grille3 # Je retourne grille 3 soit la grille avec le prénom et la note des élèves

def reponseFausseGrille (grillepoints):
    """ Cette fonction renvoie une grille avec les réponses fausses des élèves """
    grille4=[0]*len(grillepoints)#Je crée une liste de la taille de la grille de points
    for i in range(len(grillepoints)):#Je parcours ma liste
        grille4[i]=reponseFausse(grillepoints[i])#J'assigne à l'index de la deuxième liste une nouvelle liste pour en faire une grille
                                             #faite à partir de la fonction reponseFausse de l'index de la grille de points
                                             #qui retourne la liste des index de réponses fausses des élèves
    return grille4 # Je retourne grille4 soit la grille avec le prénom de l'élève et l'index de ses réponses fausses

def somGrille(grillepoints):
    """ Cette fonction additionne le total des points des élèves pour chacune des questions """
    listeSom=[]#Je crée une liste vide qui contiendra le total des points des élèves
    listeSom.append('somme')#J'ajoute somme au début de la liste
    sommeGrille=0#J'initialise une variable à zéro
    for j in range(1,len(grillepoints[0])):#Je parcours la liste dans la grille, pour traiter la question j, en excluant le prénom et j'utilise la longueur de grillepoints[0] car les listes ont toutes la même longueur
        for i in range(len(grillepoints)):#Je parcours ensuite la grille pour lire les points de chaque élève pour cette question
            sommeGrille+=grillepoints[i][j]#J'additionne à la variable les points de la question
        listeSom.append(sommeGrille)#J'insere mon ajout(sommeGrille) dans la liste que j'avais initialisée au début
        sommeGrille=0#Je remets la variable à zéro pour traiter la question suivante 
    return listeSom # Je retourne la liste

grilleNote = [ ['Alan', 14] , ['Ada', 2] , ['Hedy', 3] ]

def meilleurResultat(grillerep) :
    """ Cette fonction donne le nom de l'élève avec le meilleur résultat """
    mr=grillerep[0][0]# J'initialise avec le nom du premier élève
    mrc=grillerep[0][1]#J'initialise à la note du premier élève
    for i in range(1,len(grillerep)):#Je parcours ma grille pour chaque élève excluant le premier
        if mrc<grillerep[i][1]:# Si la variable mrc(meilleur résultat chiffre) est inférieure à la note de cet.te élève alors :
            mrc=grillerep[i][1]#Je remplace la variable mrc avec la note
            mr=grillerep[i][0]# Et je remplace le nom de l'élève ayant eu le meilleur résultat 
    return mr # A la fin je retourne le nom de l'élève ayant eu la meilleure note

# partie 3 fichier
# Pensez à mettre reponse.csv et réponseQCM.csv dans le même répertoire que votre programme.
import csv
def lireSolutionCSV():
    """ Cette fonction lit le fichier solution et renvoie une liste avec la solution """
    sol=[]#Je déclare une variable sol qui contiendra la solution des réponses
    monFichierSol=open('solution.csv')#J'ouvre mon fichier
    contenu=csv.reader(monFichierSol, delimiter=";")#Je place le contenu du fichier que je lis dans une variable
    for ligne in contenu:#Je parcours le contenu
        sol=ligne#Je j'ajoute la l'ensemble des solutions dans sol
    monFichierSol.close()#Je ferme mon fichier
    return sol # Je retourne une liste avec la solution

def lireCSV() :
    """ Cette fonction lit les réponses puis renvoie une grille avec le prénom et les réponses qui se trouvaient dans le fichier """
    rep=[]#Je déclare une variable rep qui contiendra les réponses des éléves
    monFichierRep=open('reponseQCM.csv')#J'ouvre mon fichier
    contenu=csv.reader(monFichierRep, delimiter=";")#Je place le contenu du fichier que je lis dans une variable
    for lignes in contenu:#Je parcours le contenu
        rep.append(lignes)#Je j'ajoute toutes les lignes dans rep
    monFichierRep.close()#Je ferme mon fichier
    return rep # Je retourne le contenu du fichier

def ecritureCSV():
    """ Cette fonction écrit dans le fichier noteQCM le prénom et la note de l'élève et retourne la liste avec le prénom et la note de l'élève """
    corriger=corrigeGrille(lireCSV(),lireSolutionCSV())#J'attribue à la variable "corriger" la grille résultant de la fonction corrigeGrille, utilisée sur les données renvoyées par les fonctions lireCSV et lireSolutionCSV, soit une grille corigée
    notePrenom=noteGrille(corriger)#Je note ensuite cette grille avec la fonction noteGrille qui me renvoie une grille avec le prénom et la note de chaque élève
    monFichierNote=open('noteQCM.csv',"w")#J'ouvre en mode écriture mon fichier noteQCM
    for i in range(len(notePrenom)):#Je parcours ma liste et j'écris le prénom et la note, séparés d'un point virgule et ensuite j'écris un saut de ligne. 
        monFichierNote.write(str(notePrenom[i][0]))
        monFichierNote.write(';')
        monFichierNote.write(str(notePrenom[i][1]))
        monFichierNote.write('\n')
    monFichierNote.close()#Je ferme mon fichier
    return notePrenom# Je retourne la liste des notes
