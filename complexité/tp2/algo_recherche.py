'''
def recherche_dichotomique( element, tableau ):
    bas = 0
    haut = len(tableau)-1
    find = False
    while bas <= haut and find == False:
        milieu = (bas + haut) // 2
        if element==tableau[milieu]:
            find=True
        else:
            if element>tableau[milieu]:
                bas = milieu+1
            else:
                haut = milieu-1

    if find==True:
        indice = milieu
    else:
        indice = -1
    return indice

tableau=[10,12,15,21,25,31,35,37,42,44,49,53,61,72,75,85]
print (tableau)
chiffreAtrouver=21
print('chiffre à trouver',chiffreAtrouver)
indice=recherche_dichotomique(chiffreAtrouver,tableau)
print("la valeur", tableau[indice],"se trouve a l'indice", indice,"dans le tableau:")
'''


