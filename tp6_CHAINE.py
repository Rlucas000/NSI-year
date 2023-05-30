#----------------------------------------------------------------------
'''
#Exercice 2

#2.1

def compteLettre(lettre,chaine):
    c = chaine.count(lettre)
    print("il y a", c,"e dans la phrase:")
    print(chaine)

compteLettre('e','je vais au cine ce soir')
'''
#----------------------------------------------------------------------
'''
#2.2

def compteLettre(lettre,chaine):
    total = 0
    for i in range(len(chaine)):
        if chaine[i] == lettre:
            total += 1
    return total


print(compteLettre('e','je vais au cine ce soir'))
'''
#----------------------------------------------------------------------
'''
#ou

def compteLettre(lettre,chaine):
    total = 0
    for i in chaine:
        if i == lettre:
            total += 1
    return total

print(compteLettre('e','je vais au cine ce soir'))
'''
#----------------------------------------------------------------------
'''
#Excercice 3

def fonctionpremierMot(chaine):
    c = chaine.find(" ")
    print(chaine[0:c])


fonctionpremierMot("enfin il arrête de pleuvoir ")
'''
#----------------------------------------------------------------------

#Exercice 4











