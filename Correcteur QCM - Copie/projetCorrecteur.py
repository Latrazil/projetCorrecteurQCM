lAlan = ['Alan','A','D','Z','C','C','B','Z','D']
lsolution = ['solution','A','A','C','C','C','B','C','D']
def points(reponse,solution):
        if reponse==solution:
            return 3
        elif reponse!=solution:
            if reponse=='Z':
                return 0
            else:
                return -1
        

def corrige (lrep,lsol):
    """ decrire votre fonction ici """
    # en tout premier je crée une liste vide dans laquelle je vais mettre ma réponse
    resultat = []
    # ensuite j'y ajoute mon prenom
    resultat.append(lrep[0])
    for i in range(1,len(lrep)): # je parcours le reste de ma liste et je pense à 
        reponse = lrep[i]
        solution = lsol[i]
        score = points(reponse,solution)
        resultat.append(score)
    return resultat

l=['Alan',3,-1,0,3,3,3,0,3]
def note (lpoints):
    somme=0
    for i in range(1,len(lpoints)):
        somme+=lpoints[i]
    return somme

def reponseFausse(lpoints):
    rf=[]
    rf.append(lpoints[0])
    for i in range(1,len(lpoints)):
        if lpoints[i]!=3:
            rf.append(i)
    """ decrire votre fonction ici """
    return rf # pour l'instant votre fonction ne fait rien. Ligne à supprimer quand vous écrivez votre fonction


# partie 2

grille =    [ ['Alan','A','D','Z','C','C','B','Z','D'] ,
              ['Ada','B','D','B','C','Z','B','Z','A'] ,
              ['Hedy','B','D','B','C','Z','B','Z','Z']  ]
lsolution = ['solution','A','A','C','C','C','B','C','D']

def corrigeGrille(grillerep,lsol):
    grille2=[0]*len(grillerep)
    """ decrire votre fonction ici """
    for i in range(len(grillerep)):
        grille2[i]=corrige(grillerep[i],lsol)
    return grille2# pour l'instant votre fonction ne fait rien. Ligne à supprimer quand vous écrivez votre fonction

g=  [ ['Alan', 3,-1,0,3,3,3,0,3] ,
      ['Ada', -1,-1,-1,3,0,3,0,-1] ,
      ['Hedy', -1,-1,-1,3,0,3,0,0] ]

def noteGrille(grillepoints):
    """ decrire votre fonction ici """
    grille3=[0]*len(grillepoints)
    for x in range(len(grillepoints)):
        grille3[x]=[0]*2
    for i in range(len(grillepoints)):
        for j in range(len(grillepoints[i])):
            if j==0:
                grille3[i][0]=grillepoints[i][j]
            else:
                grille3[i][1]=note(grillepoints[i])
    return grille3 # pour l'instant votre fonction ne fait rien. Ligne à supprimer quand vous écrivez votre fonction

def reponseFausseGrille (grillepoints):
    grille4=[0]*len(grillepoints)
    for i in range(len(grillepoints)):
        grille4[i]=reponseFausse(grillepoints[i])
    """ decrire votre fonction ici """
    return grille4 # pour l'instant votre fonction ne fait rien. Ligne à supprimer quand vous écrivez votre fonction

def somGrille(grillepoints):
    listeSom=[]
    listeSom.append('somme')
    sommeGrille=0
    i=0
    j=1
    while j <len(grillepoints[i]):
        while i <len(grillepoints):
            sommeGrille+=grillepoints[i][j]
            i=i+1
        i=0
        listeSom.append(sommeGrille)
        sommeGrille=0
        j=j+1
    
    """ decrire votre fonction ici """
    return listeSom # pour l'instant votre fonction ne fait rien. Ligne à supprimer quand vous écrivez votre fonction

grilleNote = [ ['Alan', 14] , ['Ada', 2] , ['Hedy', 3] ]

def meilleurResultat(grillerep) :
    mr=''
    mrc=0
    for i in range(len(grillerep)):
        if mrc<grillerep[i][1]:
                mrc=grillerep[i][1]
                mr=grillerep[i][0]    
    return mr # pour l'instant votre fonction ne fait rien. Ligne à supprimer quand vous écrivez votre fonction

# partie 3 fichier
# Pensez à mettre reponse.csv et réponseQCM.csv dans le même répertoire que votre programme.
import csv
def lireSolutionCSV():
    sol=[]
    monFichierSol=open('solution.csv')
    contenu=csv.reader(monFichierSol, delimiter=";")
    for ligne in contenu:
        sol.append(ligne)
    sol2 = [elt for lst in sol for elt in lst]    
    """ decrire votre fonction ici """
    monFichierSol.close()
    return sol2 # pour l'instant votre fonction ne fait rien. Ligne à supprimer quand vous écrivez votre fonction

def lireCSV() :
    rep=[]
    monFichierRep=open('reponseQCM.csv')
    contenu=csv.reader(monFichierRep, delimiter=";")
    for lignes in contenu:
            rep.append(lignes)
    monFichierRep.close()
    """ decrire votre fonction ici """
    return rep # pour l'instant votre fonction ne fait rien. Ligne à supprimer quand vous écrivez votre fonction

def ecritureCSV():
    corriger=corrigeGrille(lireCSV(),lireSolutionCSV())
    notePrenom=noteGrille(corriger)
    monFichierNote=open('noteQCM.csv',"w")
    for i in range(len(notePrenom)):
        monFichierNote.write(str(notePrenom[i][0]))
        monFichierNote.write(';')
        monFichierNote.write(str(notePrenom[i][1]))
        monFichierNote.write('\n')
    monFichierNote.close()
    """ decrire votre fonction ici """
    return # pour l'instant votre fonction ne fait rien. Ligne à supprimer quand vous écrivez votre fonction
    
