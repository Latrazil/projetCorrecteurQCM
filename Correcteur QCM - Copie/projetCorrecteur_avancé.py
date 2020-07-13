from tkinter import*#J'importe les modules dont j'aurais besoin
import operator as op#Je raccourcis operator en op 
import math#J'importe math pour faire des opérations complexes
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

#partie4 Tkinter

def Accueil():
    """" Cette fonction permet d'afficher l'accueil """
    Detruire()#Je désaffiche les widgets à l'écran avec la fonction détruire, ce que je ferais pour chacune des fonction suivantes

    Label1.config(text="Accueil",font=('System', '40', 'italic bold'),width='15')#Je configure le label1 pour qu'il affiche "Accueil" en police de caractère system, taille 40, et en italic gras avec une taille de 15 caractères

    Label1.grid(column=2,row=1,padx=20, pady=20)#Je l'affiche.

    Entree.config(font=('System', '1'))
    Entree2.config(font=('System', '1'))#Je configure la police de caractères des zones de saisie et des boutons

    Bouton.config(font=('System', '1'))
    Bouton2.config(font=('System', '1'))
    
    Entree.grid(column=0,row=2,padx=20, pady=20)# Je les affiche
    Bouton.grid(column=1, row=2, padx=20, pady=20)

    Entree2.grid(column=0,row=3, padx=20, pady=20)
    Bouton2.grid(column=1, row=3, padx=20, pady=20)
    return

def VoirNotesEleves():
    """ Cette fonction permet d'afficher les notes des élèves """
    Detruire()
    Canevas.delete(ALL)#J'efface ce qu'il y avait sur les canvas
    Canevas2.delete(ALL)
    Canevas3.delete(ALL)
    VoirNotesEleves1()#J'appelle les trois fonctions décrites plus bas
    VoirNotesEleves2()
    VoirNotesEleves3()
    return

def VoirNotesEleves1():
    """ Cette fonction permet d'afficher les notes dans l'ordre alphabétique """
    Label1.config(text="Les notes et prénoms triés selon l'ordre alphabétique",font=('System', '1'), width='45')#Je configure mon label et je l'affiche
    Label1.grid(column=0,row=1)
    corriger=corrigeGrille(lireCSV(),lireSolutionCSV())#Je fais la même chose que dans ecritureCSV pour avoir une grille de notes et prénoms 
    Notes=noteGrille(corriger)
    Canevas.config(width=((fen.winfo_width())/3)-5, height=fen.winfo_height(),scrollregion=(0, 0,(len(Notes)*15)+100 , (len(Notes)*15)+100))#Je configure la taille de mon Canevas et la zone de déplacement pour la barre 
    Canevas.grid(column=0,row=2,padx=1, pady=2)#J'affiche mon Canevas
    for i in range(len(Notes)):
        Canevas.create_text(35,(3+i)*15, text=Notes[i][0], justify='left', anchor='sw',font=('System', '1'))#J'affiche le prénom, puis :, puis la note dans le Canevas
        Canevas.create_text(120,(3+i)*15, text=":", justify='left', anchor='sw',font=('System', '1'))
        Canevas.create_text(165,(3+i)*15, text=Notes[i][1], justify='left', anchor='sw',font=('System', '1'))
    BarreDefil.config(orient='vertical', command=Canevas.yview)#Je configure ma barre de défilement en l'orientant verticalement et je lui attribue les ordonnées du Canvas pour qu'elle puisse les faire défiler
    BarreDefil.grid(column=1, row=2, sticky='ns')#Je l'affiche
    Canevas['yscrollcommand'] = BarreDefil.set#J'attribue à la commande yscrool du Canevas la barre de défilement pour lui permettre de défiler
    return

def VoirNotesEleves2():
    """ Cette fonction permet d'afficher les note dans l'ordre décroissant, elle est globalement pareil à la première sauf sur un point """
    Label2.config(text="Les notes et prénoms triés selon l'ordre decroissant des notes",font=('System', '1'))
    Label2.grid(column=2,row=1)
    corriger=corrigeGrille(lireCSV(),lireSolutionCSV())
    Notes=noteGrille(corriger)
    Notes.sort(key=op.itemgetter(1), reverse=True)# Je trie ma grille selon la deuxième occurence de la liste à l'intérieur de la grille(la note) grace à la fonction itemgetter d'operator puis j'inverse la grille, soit l'ordre décroissant des notes
    Canevas2.config(width=fen.winfo_width()/3-5, height=fen.winfo_height(),scrollregion=(0, 0,(len(Notes)*15)+100 , (len(Notes)*15)+100))
    Canevas2.grid(column=2,row=2,padx=1, pady=2)
    for i in range(len(Notes)):
        Canevas2.create_text(35,(3+i)*15, text=Notes[i][0], justify='left', anchor='sw',font=('System', '1'))
        Canevas2.create_text(120,(3+i)*15, text=":", justify='left', anchor='sw',font=('System', '1'))
        Canevas2.create_text(165,(3+i)*15, text=Notes[i][1], justify='left', anchor='sw',font=('System', '1'))
    BarreDefil2.config(orient='vertical', command=Canevas2.yview)
    BarreDefil2.grid(column=3, row=2, sticky='ns')
    Canevas2['yscrollcommand'] = BarreDefil2.set
    return

def VoirNotesEleves3():
    """ Cette fonction permet d'afficher les note dans l'ordre croissant, elle est globalement pareil à la première sauf sur un point """
    Label3.config(text="Les notes et prénoms triés selon l'ordre croissant des notes",font=('System', '1'))
    Label3.grid(column=4,row=1)
    corriger=corrigeGrille(lireCSV(),lireSolutionCSV())
    Notes=noteGrille(corriger)
    Notes.sort(key=op.itemgetter(1))# Je trie ma grille selon la deuxième occurence(la note) grace à la fonction itemgetter d'operator soit dans l'ordre croissant des notes
    Canevas3.config(width=((fen.winfo_width())/3)-75, height=fen.winfo_height(),scrollregion=(0, 0,(len(Notes)*15)+100 , (len(Notes)*15)+100))
    Canevas3.grid(column=4,row=2,padx=1, pady=2)
    for i in range(len(Notes)):
        Canevas3.create_text(35,(3+i)*15, text=Notes[i][0], justify='left', anchor='sw',font=('System', '1'))
        Canevas3.create_text(120,(3+i)*15, text=":", justify='left', anchor='sw',font=('System', '1'))
        Canevas3.create_text(165,(3+i)*15, text=Notes[i][1], justify='left', anchor='sw',font=('System', '1'))
    BarreDefil3.config(orient='vertical', command=Canevas3.yview)
    BarreDefil3.grid(column=5, row=2, sticky='ns')
    Canevas3['yscrollcommand'] = BarreDefil3.set
    return

def EleveMeilleur():
    """ Cette fonction permet de savoir le meilleur élève ainsi que sa note """
    Detruire()
    Canevas.delete(ALL)#J'efface le contenu de Canevas
    corriger=corrigeGrille(lireCSV(),lireSolutionCSV())
    Notes=noteGrille(corriger)
    Notes.sort(key=op.itemgetter(1),reverse=True)#Je vais la même chose que dans VoirNotesEleves2 pour avoir la note correspondante au meilleur résultat
    meilleurEleve=meilleurResultat(Notes)#J'utilise la fonction meilleurResultat pour déterminer le nom de l'élève ayant eut le meilleur résultat
    Canevas.config(width=fen.winfo_width(), height=fen.winfo_height())#Je configure mon Canevas pour lui donner la taille de la fenêtre
    Canevas.grid(column=0,row=1)#J'affiche mon Canevas
    Canevas.create_text(fen.winfo_width()/2,fen.winfo_height()/2, text="Bravo à : "+str(meilleurEleve)+" qui a obtenu une note de : "+str(Notes[0][1]), font=('System', '40', 'italic bold'), fill='orange')
    #J'écris dans le Canevas une chaine caractère comprenant le nom de l'élève et sa note qui est la seconde occurence du début de la liste triée selon l'ordre décroissant de la note
    return

def ElevePire():
    """ Cette fonction permet de savoir quel élève a eut le moins bon score et sa note, elle est globalement semblable à EleveMeilleur mais possède certaines différences """
    Detruire()
    Canevas.delete(ALL)#J'efface le contenu de Canevas
    corriger=corrigeGrille(lireCSV(),lireSolutionCSV())
    Notes=noteGrille(corriger)
    Notes.sort(key=op.itemgetter(1))#Je fais la même chose que dans VoirNotesEleves3 pour avoir la note et le prénom correspondante au pire résultat
    pireEleve=Notes[0][0]#J'attribue le prénom de l'élève ayant le pire résultat qui est la première occurence de la liste croissante de notes
    Canevas.config(width=fen.winfo_width(), height=fen.winfo_height())
    Canevas.grid(column=0,row=1)
    Canevas.create_text(fen.winfo_width()/2,fen.winfo_height()/2, text=str(pireEleve)+" a obtenu une note de : "+str(Notes[0][1]), font=('System', '40','italic bold'), fill='blue')
    #J'écris dans le Canevas une chaine caractère comprenant le nom de l'élève et sa note qui est la seconde occurence du début de la liste triée selon l'ordre croissant de la note
    return

def VoirReponsesEleves():
    """ Cette fonction permet de voir les réponses proposées par les élèves """
    Detruire()
    Canevas.delete(ALL)
    Label3.config(text="Les réponses des élèves",font=('System', '1'))
    Label3.grid(column=2,row=1)
    Reponse=lireCSV()#J'utilise lireCSV pour avoir une grille avec les prénoms et les réponses des élèves
    Canevas.config(width=((fen.winfo_width())/2), height=fen.winfo_height(),scrollregion=(0, 0,(len(Reponse)*15)+100 , (len(Reponse)*15)+100))
    Canevas.grid(column=2,row=2,padx=20, pady=2)
    for i in range(len(Reponse)):#Je parcours ma grille
        Canevas.create_text(35,(3+i)*15, text=Reponse[i][0], justify='left', anchor='sw',font=('System', '1'))#Je mets en premier le prénom de l'élève, qui n'occura qu'une fois par parcours de grille
        Canevas.create_text(120,(3+i)*15, text=":", justify='left', anchor='sw',font=('System', '1'))#Je mets le : pour séparer les réponses du prénom de l'élève
        for j in range(1,len(Reponse[i])):#Je parcours le reste des réponses en excluant le prénom
            Canevas.create_text(120+10*j,(3+i)*15, text=Reponse[i][j], justify='left', anchor='sw',font=('System', '1'))#J'écris les réponses des élèves dans le Canevas
    BarreDefil.config(orient='vertical', command=Canevas.yview)
    BarreDefil.grid(column=3, row=2, sticky='ns')
    Canevas['yscrollcommand'] = BarreDefil.set
    return

def VoirReponsesFausses():
    """ Cette focntion permet de voir les numéros des questions auxquelles les élèves ont répondu faux, elle est semblable dans la forme à la fonction précedente """
    Detruire()
    Canevas.delete(ALL)
    Label3.config(text="Les réponses fausses des élèves")
    Label3.grid(column=1,row=1)
    ReponseFausse=corrigeGrille(lireCSV(),lireSolutionCSV())#Je fais la même chose que dans ecritureCSV pour avoir une grille de notes et prénoms 
    ReponseFausse=reponseFausseGrille(ReponseFausse)#J'utlise la fonction reponseFausseGrille sur ma grille pour avoir l'index des réponses fausses
    Canevas.config(width=((fen.winfo_width())/2), height=fen.winfo_height(),scrollregion=(0, 0,(len(ReponseFausse)*15)+100 , (len(ReponseFausse)*15)+100))
    Canevas.grid(column=1,row=2,padx=20, pady=2)
    for i in range(len(ReponseFausse)):
        Canevas.create_text(35,(3+i)*15, text=ReponseFausse[i][0], justify='left', anchor='sw',font=('System', '1'))#Cette partie est similaire à la fonction du dessus à part que ceux sont l'index des réponses fausses qui sont mises et non les réponses des élèves
        Canevas.create_text(120,(3+i)*15, text=":", justify='left', anchor='sw',font=('System', '1'))
        for j in range(1,len(ReponseFausse[i])):
            Canevas.create_text(120+10*j,(3+i)*15, text=ReponseFausse[i][j], justify='left', anchor='sw',font=('System', '1'))
    BarreDefil.config(orient='vertical', command=Canevas.yview)
    BarreDefil.grid(column=2, row=2, sticky='ns')
    Canevas['yscrollcommand'] = BarreDefil.set
    return

def VoirReponsesOrdreReusite():
    """ Cette fonction permet de voir l'ordre de réussite des question du questionnaire """
    Detruire()
    Canevas.delete(ALL)
    ReponseFausse=corrigeGrille(lireCSV(),lireSolutionCSV())#Je fais la même chose que dans ecritureCSV pour avoir une grille de notes et prénoms 
    OrdreReusite=somGrille(ReponseFausse)#J'additionne les points des eleves grace à la fonction somGrille
    for i in range(len(OrdreReusite)):#Je parcours ma liste
        if i!=0:#J'exclue somme
            OrdreReusite[i]=[i,int(OrdreReusite[i])]#Je met le numero des questions devant les resultats de somGrille
    OrdreReusite.remove('somme')#J'enlève somme
    OrdreReusite.sort(key=op.itemgetter(1))#Je trie ma grille selon la deuxième occurence
    Canevas.create_text(20,fen.winfo_height()/2, text="Les questions des moins au plus réussies : ", justify='left', anchor='sw',font=('System', '25'))
    for i in range(len(OrdreReusite)):#Je parcours ma grille
        Canevas.create_text(fen.winfo_width()/2-75+i*70,fen.winfo_height()/2, text=str(OrdreReusite[i][0])+"|", justify='left', anchor='sw',font=('System', '27'))#Je mets les question des moins au plus réussies
    Canevas.config(height=fen.winfo_height(),width=fen.winfo_width())
    Canevas.grid(column=0, row=1)
    return

def VoirSolution():
    """ Cette fonction permet de voir la solution des questions du questionnaire """
    Detruire()
    Canevas.delete(ALL)
    Label3.config(text="La solution")
    Label3.grid(column=1,row=1)
    Solution1=lireSolutionCSV()#Je recupère une liste Solution1 grace à la fonction lireSolutionCSV
    Solution1.insert(1,':')#J'insert un : à la deuxième occurence, soit juste après "solution"
    Solution1=" ".join(Solution1)#Je transforme ma liste en chaine de caractères séparés par un espace
    Canevas.config(width=fen.winfo_width(), height=fen.winfo_height())
    Canevas.grid(column=0,row=1)
    Canevas.create_text(fen.winfo_width()/2,fen.winfo_height()/2, text=str(Solution1), font=('System', 30))#J'affiche ma chaine de caractère sur le Canevas
    return

def rechercher():
    """Cette fonction permet de rechercher la note avec le prénom d'un élève"""
    Canevas.delete(ALL)
    Canevas.config(width=fen.winfo_width()/2, height=fen.winfo_height()/4)
    Canevas.grid(column=2,row=2,padx=20, pady=20)
    corriger=corrigeGrille(lireCSV(),lireSolutionCSV())
    longueur=noteGrille(corriger)#Je fais la même chose que dans ecritureCSV pour avoir une grille de notes et prénoms 
    for i in range(len(longueur)):#Je parcours ma grille
        if longueur[i][0]==recherche.get():#Si le prénom, soit la première ocurence de la liste dans la grille, est le même que celui recherché alors j'affiche le prénom et la note soit la deuxième occurence 
            Canevas.create_text(fen.winfo_width()/4,fen.winfo_height()/8,text=str(longueur[i][0])+' a une note de '+str(longueur[i][1]),font=('System', 30))
            return#Je ferme la fonction
    Canevas.create_text(fen.winfo_width()/4,fen.winfo_height()/8,text=recherche.get()+' n\'existe pas',font=('System', 30))#Sinon si il n'y a pas de prénom correspondant je dis que le prénom n'existe pas
    return

def rechercher2():
    """Cette fonction permet de rechercher les prénoms d'élèves à partir de la note"""
    Canevas2.delete(ALL)
    nombre=0#J'initialise une variable nombre à zéro
    corriger=corrigeGrille(lireCSV(),lireSolutionCSV())
    longueur=noteGrille(corriger)#Je fais la même chose que dans ecritureCSV pour avoir une grille de notes et prénoms 
    for i in range(len(longueur)):#Je parcours ma grille
        if str(longueur[i][1])==recherche2.get():#Si la deuxième occurence soit la note est égale à la note recherchée alors j'affiche les prénoms liés à cette note
            Canevas2.create_text(fen.winfo_width()/4,(nombre+3)*15,text=str(longueur[i][0]), justify='left', anchor='sw',font=('System', '1'))
            nombre=nombre+1#J'additionne un à "nombre" pour que ce dernier soit au dessus de zéro, cela me renseigne si il y a bien une occurence au moins, je compte aussi ainsi le nombre d'élèves
    if nombre==0:#Si il n'y pas d'occurence, je dis que la note n'existe pas
        Canevas2.create_text(fen.winfo_width()/4,fen.winfo_height()/8,text='Cette note n\'existe pas',font=('System', 30))
    else:#Sinon je dis le nombre d'élève ayant eu cette note
        Canevas2.create_text(fen.winfo_width()/6,45,text=str(nombre)+' élèves ont une note de '+str(recherche2.get())+ " : " ,font=('System', 10))
        BarreDefil2.config(orient='vertical', command=Canevas2.yview)
        BarreDefil2.grid(column=3, row=3, sticky='ns')
        Canevas2['yscrollcommand'] = BarreDefil2.set

    Canevas2.config(width=fen.winfo_width()/2, height=fen.winfo_height()/4,scrollregion=(0, 0,(nombre*15)+100 , (nombre*15)+100))
    Canevas2.grid(column=2,row=3,padx=20, pady=20)
    return

def VoirStatistiques():
    """ Cette fonction permet de connaitre la moyenne et l'écart type des notes du questionnaire """
    Detruire()
    Canevas.delete(ALL)
    Canevas2.delete(ALL)
    moyenne=0#J'initialise mes deux variable à zéro
    ecarttype=0
    corriger=corrigeGrille(lireCSV(),lireSolutionCSV())
    listeNotesEleves=noteGrille(corriger)#Je fais la même chose que dans ecritureCSV pour avoir une grille de notes et prénoms 
    longueur1=len(listeNotesEleves)#Je crée une variable longueur pour ne par avoir à écrire len(listeNotesEleves)
    for i in range(longueur1):#Je parcours ma liste
        moyenne+=listeNotesEleves[i][1]#J'ajoute la note des élèves à "moyenne" pour avoir le total des notes
    moyenne/=longueur1#Je divise ce total des notes stocké dans "moyenne" par "longueur" pour obtenir la moyenne
    for i in range(longueur1):#Je parcours ma liste
        ecarttype+=((listeNotesEleves[i][1]-moyenne)*(listeNotesEleves[i][1]-moyenne))#J'applique la formule de la variance qui est (x-moyenne)^2 divisée par longueur1 soit grand N
    ecarttype/=longueur1
    ecarttype=math.sqrt(ecarttype)#Pour trouver l'écart type j'utilise la fonction sqrt de math soit racine carrée sur la variance

    Canevas.config(height=fen.winfo_height()/2,width=fen.winfo_width())

    Canevas2.config(height=fen.winfo_height()/2,width=fen.winfo_width())

    Canevas.grid(row=1,column=1,padx=10, pady=2)
    Canevas.create_text(fen.winfo_width()/3,fen.winfo_height()/4,text='La moyenne de la classe est de '+str("{:.2f}".format(moyenne)), font=('System',30))#J'utilise format pour n'afficher que deux chiffres après la virgule
    Canevas2.grid(row=2,column=1,padx=10, pady=2)
    Canevas2.create_text(fen.winfo_width()/3,fen.winfo_height()/4,text='L\'écart type de la classe est de '+str("{:.2f}".format(ecarttype)), font=('System',30))
    
    return

def VoirGraphiqueBaton():
    """ Cette fonction permet d'afficher un graphique en baton des notes du questionnaire"""
    Detruire()
    Canevas.delete(ALL)
    corriger=corrigeGrille(lireCSV(),lireSolutionCSV())#Je fais la même chose que dans ecritureCSV pour avoir une grille de notes et prénoms 
    listeNotesEleves=noteGrille(corriger)
    listeNotesEleves.sort(key=op.itemgetter(1))#Je trie selon l'ordre croissant des notes
    longueur1=len(listeNotesEleves)
    listeNotes1=[]#J'initialise 2 listes vides, la première me servira à avoir toutes les différentes notes qu'ont eut les élèves, la deuxième me servira à compter le nombre d'élèves pour chacune de ces notes
    listeNombre=[]
    x=0#J'initialise 1 variable, l'index, à zéro
    listeNotes1.append(listeNotesEleves[0][1])#J'initialise la liste des notes par la valeur la plus basse(1ère de la liste car triée par ordre croissant) 
    listeNombre.append(1)#J'initialise le compteur du nombre d'élèves à un
    for i in range(longueur1):#Je parcours ma liste
        if listeNotes1[x]!=listeNotesEleves[i][1]:# Si la note d'un élève n'est plus égale à la note stockée dans listeNotes1 alors
            listeNotes1.append(listeNotesEleves[i][1])#je rajoute cette note à listeNotes1
            listeNombre.append(1)#Je réinitialise le compteur du nombre d'élèves à un pour chacune des notes
            x+=1#en incrémentant l'index
        else:
            listeNombre[x]+=1#Sinon j'incrémente le compteur du nombre d'élèves de un pour cette note
    Canevas.create_line(325,fen.winfo_height()-50,325,(fen.winfo_height()-50)-max(listeNombre)*1.5, fill='black')#Je crée les axes de légende
    for i in range(len(listeNombre)):#Je parcours la liste de nombres d'élèves ayant eu une note
        Canevas.create_rectangle((i*20)+325,fen.winfo_height()-50,((i+1)*20)+325,(fen.winfo_height()-50)-listeNombre[i]*1.5, outline='black')#Je crée les rectangles du diagramme en batons
        Canevas.create_text((i*20)+333,fen.winfo_height()-15, text= str(listeNotes1[i]))#J'écris les légendes horizontales
        Canevas.create_text(310,(fen.winfo_height()-50)-listeNombre[i]*1.5, text=str(listeNombre[i]),font=('Helvetica',5))#J'écris les légendes verticales
    Canevas.config(height=fen.winfo_height(), width=fen.winfo_width())
    Canevas.grid(row=1,column=0,padx=20)
    return

def VoirPourcentages():
    """ Cette fonction permet d'afficher l'accueil pour les pourcentages """
    Detruire()

    Canevas.delete(ALL)
    Canevas2.delete(ALL)
    Canevas3.delete(ALL)

    Entree2.config(font=('System',15))
    Bouton3.config(font=('System',15))
       
    Entree2.grid(column=0, row=1, padx=10, pady=10)
    Bouton3.grid(column=1, row=1,padx=10, pady=10)
    return


def VoirPourcentage():
    """Cette fonction permet de calculer les pourcentages d'élève, en dessous, au dessus et égale à une note"""
    nombre=0
    nombre2=0
    nombre3=0#J'initialise mes trois variables, qui vont contenir le nombre de notes au dessus, dessous et égale à la note recherchée, à zéro

    pourcentage1=0#J'initialise mes trois variables qui vont contenir les pourcentages à zéro 
    pourcentage2=0
    pourcentage3=0
    
    Canevas.delete(ALL)
    Canevas2.delete(ALL)
    Canevas3.delete(ALL)#J'efface le contenu des Canevas
    corriger=corrigeGrille(lireCSV(),lireSolutionCSV())
    longueur=noteGrille(corriger)#Je fais la même chose que dans ecritureCSV pour avoir une grille de notes et prénoms 
    if recherche2.get().isdigit()==False:# Si la saisie n'est pas un nombre alors je la compte comme une recherche fausse
        pourcentage2=100
        pourcentage1=0
    else:#Sinon je parcours ma grille
        for i in range(len(longueur)):
            if int(longueur[i][1])>int(recherche2.get()):# Si ma note est supérieure à celle recherchée alors j'incrémente nombre
                nombre=nombre+1
            elif int(longueur[i][1])<int(recherche2.get()):# Si ma note est inférieure à celle recherchée alors j'incrémente nombre2
                nombre2=nombre2+1
            elif int(longueur[i][1])==int(recherche2.get()):# Si ma note est égale à celle recherchée alors j'incrémente nombre3
                nombre3=nombre3+1
        pourcentage1=(nombre/len(longueur))*100# Je calcule les pourcentages en fonction des nombres
        pourcentage2=(nombre2/len(longueur))*100
        pourcentage3=(nombre3/len(longueur))*100

    if (pourcentage2==100 and pourcentage1==0)or(pourcentage2==0 and pourcentage1==100):# Si un des poucentages est égal à 100% tandis que celui opposée est égal à 0% alors cela veut dire que la note demandée n'est soit qu'inférieur ou supérieur à une note possible, la rendant inexistante 
        Canevas.config(width=fen.winfo_width(), height=fen.winfo_height()/2)
        Canevas3.grid_forget()
        Canevas2.grid_forget()
        Canevas.create_text(fen.winfo_width()/4+35,fen.winfo_height()/4,text="Cette note n'est pas comprise dans l'intervalle des notes", font=('System',20) )
        Canevas.grid(column=2, row=1 ,columnspan=4,padx=20, pady=0)
    else:#Sinon j'affiche les trois pourcentages arrondi au deuxième chiffre après la virgule avec format
        Canevas.config(width=fen.winfo_width()/2, height=fen.winfo_height()/3)
        Canevas2.config(width=fen.winfo_width()/2, height=fen.winfo_height()/3)
        Canevas3.config(width=fen.winfo_width()/2, height=fen.winfo_height()/3)

        Canevas.create_text(fen.winfo_width()/4,fen.winfo_height()/8,text="Le pourcentage d'élèves ayant une note supérieure à la note rentrée est de "+str("{:.2f}".format(pourcentage1))+"%",font=('System', '16'))

        Canevas2.create_text(fen.winfo_width()/4,fen.winfo_height()/8,text="Le pourcentage d'élèves ayant une note inférieure à la note rentrée est de "+str("{:.2f}".format(pourcentage2))+"%",font=('System', '16'))

        Canevas3.create_text(fen.winfo_width()/4,fen.winfo_height()/8,text="Le pourcentage d'élèves ayant une note égale à la note rentrée est de "+str("{:.2f}".format(pourcentage3))+"%",font=('System', '16'))

        Canevas.grid(column=2, row=1 ,columnspan=4,padx=20, pady=0)
        Canevas2.grid(column=2, row=2,columnspan=4,padx=20, pady=0)
        Canevas3.grid(column=2, row=3,columnspan=4,padx=20, pady=0)
    return

def Detruire():
    """ Cette fonction efface les wigets de la fenetre pour eviter d'avoir un widget en trop lors d'un affichage """
    #J'oublie la position des widgets pour les faire disparaitre de la fenetre grace à grid_forget()
    Entree.grid_forget()
    Bouton.grid_forget()
    Entree2.grid_forget()
    Bouton2.grid_forget()
    Canevas.grid_forget()
    BarreDefil.grid_forget()
    Canevas2.grid_forget()
    BarreDefil2.grid_forget()
    Bouton3.grid_forget()
    Canevas3.grid_forget()
    BarreDefil3.grid_forget()
    Label1.grid_forget()
    Label2.grid_forget()
    Label3.grid_forget()
    return

def modeNuit():
    """ Cette fonction permet de changer la fenetre pour la passer dans un mode nuit """ 
    fen.config(bg='black')#Je configure tout pour que sa soit dans une couleur foncée

    Canevas.config(background='grey', relief='raised')
    Canevas2.config(background='grey',relief='raised')
    Canevas3.config(background='grey',relief='raised')

    Label1.config(bg='grey')
    Label2.config(bg='grey')
    Label3.config(bg='grey')

    Bouton.config(bg='grey', activebackground='grey')
    Bouton2.config(bg='grey', activebackground='grey')
    Bouton3.config(bg='grey', activebackground='grey')
 
    Entree.config(bg='grey')
    Entree2.config(bg='grey')     
    #Je n'ai pas put changer les barres de défilement et le menu, en effet windows ne le permet que si on fait une classe et je n'ai pas voulu faire trop compliqué
    return
def modeJour():
    """ Cette fonction permet de changer la fenetre pour la passer dans un mode jour """ 
    fen.config(bg='white')#Je configure tout pour que cela soit dans une couleur claire
    
    Canevas.config(background='#E4E4E4')
    Canevas2.config(background='#E4E4E4')
    Canevas3.config(background='#E4E4E4')

    Label1.config(bg='#E4E4E4')
    Label2.config(bg='#E4E4E4')
    Label3.config(bg='#E4E4E4')

    Bouton.config(bg='white', activebackground='white')
    Bouton2.config(bg='white', activebackground='white')
    Bouton3.config(bg='white', activebackground='white')
    
    Entree.config(bg='white', bd=5, relief='groove')
    Entree2.config(bg='white', bd=5, relief='groove')
    return
 
def mode(event):
    """ Cette fonction permet de changer entre mode nuit et mode jour """
    global Mode#Je définis mode en global
    if Mode==True:#Si mode est sur jour alors j'execute modeNuit et je mets mode sur nuit 
        modeNuit()
        Mode=False
    else:#Sinon l'inverse
        modeJour()
        Mode=True
    return

 
fen=Tk()#Je définis ma fenetre Tkinter

Mode=True#Je définis le mode sur jour

recherche=StringVar()#Je définis les variables des entrées

recherche2=StringVar()

Label1=Label(fen)#Je définis les étiquettes

Label2=Label(fen)

Label3=Label(fen)

Canevas=Canvas(fen)#Je définis les Canevas

Canevas2=Canvas(fen)

Canevas3=Canvas(fen)

Entree=Entry(fen,textvar=recherche)#Je définis les entrées et les boutons

Bouton=Button(fen,text='Rechercher la note de cet.te élève', command=rechercher)

Entree2=Entry(fen,textvar=recherche2)

Bouton2=Button(fen,text='Rechercher les élèves à partir de la note', command=rechercher2)

Bouton3=Button(fen,text='Rechercher le pourcentages d\'élèves à partir de la note', command=VoirPourcentage)

BarreDefil=Scrollbar(fen)#Je définis les barre de défilement

BarreDefil2=Scrollbar(fen)

BarreDefil3=Scrollbar(fen)

MenuBarre=Menu(fen)#Je définis le menu principale

fen.state('zoomed')#Je définis l'état plein écran de la fenetre au départ

fen.configure(cursor='left_ptr', bd='5', menu=MenuBarre)#J'associe MenuBarre à la fenetre en temps que menu

sousMenu=Menu(MenuBarre)#Je definis les sous menus
sousMenu2=Menu(MenuBarre)
sousMenu3=Menu(MenuBarre)

MenuBarre.add_cascade(label="Accueil", command=Accueil)#Je definis un choix Accueil associé à la commande du même nom
MenuBarre.add_cascade(label="Notes des élèves", menu=sousMenu)#Je définis des choix avec des sous menu en cascade
MenuBarre.add_cascade(label="Réponses des élèves", menu=sousMenu2)
MenuBarre.add_cascade(label="Statistiques", menu=sousMenu3)
MenuBarre.add_cascade(label="Quitter", command=fen.destroy)#Je définis un choix Quitter qui détruit la fenetre

sousMenu.add_command(label='Voir les notes des élèves', command=VoirNotesEleves)#J'ajoute à chaque sous menu des choix avec des commandes associées avec les fonctions vues plus haut
sousMenu.add_command(label='Voir l\'élève ayant la meilleur note', command=EleveMeilleur)
sousMenu.add_command(label='Voir l\'élève ayant la pire note', command=ElevePire)
sousMenu.add_command(label='Charger les notes des élèves dans un fichier', command=ecritureCSV)

sousMenu2.add_command(label='Voir les réponses des élèves', command=VoirReponsesEleves)
sousMenu2.add_command(label='Voir les réponses fausses des élèves', command=VoirReponsesFausses)
sousMenu2.add_command(label='Voir les réponses du moins au plus réussi', command=VoirReponsesOrdreReusite)
sousMenu2.add_command(label='Voir la solution des réponses', command=VoirSolution)

sousMenu3.add_command(label='Voir les statistiques', command=VoirStatistiques)
sousMenu3.add_command(label='Voir les différents pourcentages d\'élèves', command=VoirPourcentages)
sousMenu3.add_command(label='Voir le graphique en bâtons', command=VoirGraphiqueBaton)

fen.title('Gestion QCM')#Je choisis le titre de ma fenetre

Accueil()#Je définis que la page sur laquelle commencera l'utillisateur sera Accueil
modeJour()#Je définis que l'on commence en mode Jour

fen.bind('<space>',mode)# J'associe la touche espace à mode

fen.mainloop()#Je mets en boucle ma fenetre




